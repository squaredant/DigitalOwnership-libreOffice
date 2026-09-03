# DigitalOwnership Content Hash Algorithm

Current scope: `digitalownership-content-v1`

The algorithm applies to supported ZIP-based office document packages. It opens
the document as a ZIP archive, selects stable content entries, sorts the selected
internal file names lexicographically, and builds one SHA-512 digest from a
canonical manifest of those entries.

## Supported Package Detection

- ODF package: ZIP contains `mimetype` and either `content.xml` or `META-INF/manifest.xml`.
- DOCX package: ZIP contains `[Content_Types].xml` and `word/document.xml`.
- XLSX package: ZIP contains `[Content_Types].xml` and `xl/workbook.xml`.
- PPTX package: ZIP contains `[Content_Types].xml` and `ppt/presentation.xml`.

## Selected Entries

| Format | Included entries | Excluded volatile entries |
| --- | --- | --- |
| ODT, ODS, ODP, ODG | all non-directory ZIP entries outside volatile paths | `meta.xml`, `settings.xml`, `Thumbnails/` |
| DOCX | all non-directory entries under `word/` | `word/settings.xml` |
| XLSX | all non-directory entries under `xl/` | `xl/calcChain.xml` |
| PPTX | all non-directory entries under `ppt/` | none |

## Canonical Digest Input

For each selected internal file name `name`, in sorted order:

1. Read the raw bytes of that internal file as `data`.
2. Compute `file_digest = SHA512(data).hexdigest()`.
3. Append this record to the final SHA-512 digest input:

```text
FILE\0
name encoded as UTF-8
\0
decimal byte length of data encoded as ASCII
\0
file_digest encoded as ASCII lowercase hex
\0
```

The final document hash is the lowercase hexadecimal SHA-512 digest of that
canonical manifest.

For a wallet registration, the contract registry key is derived as:

```text
keccak256(SHA-512 hash text)
```

For an email-linked registration, the service first derives a normalized
email-claim hash, then derives a distinct registry key from the document hash
and that email claim. This is why verification needs the registration email for
that workflow.
