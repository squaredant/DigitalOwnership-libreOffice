# DigitalOwnership LibreOffice Plugin

DigitalOwnership lets writers, innovators, scientists, and creators register a
private fingerprint of a supported office document on Arbitrum. The document
stays on the user's computer. The public blockchain record stores only a
cryptographic proof.

## Download

- LibreOffice extension: [digitalownership-1.0.1.oxt](downloads/digitalownership-1.0.1.oxt)
- Compatibility alias: [digitalownership.oxt](downloads/digitalownership.oxt)
- Manual verifier: [digitalownership-verify.py](downloads/digitalownership-verify.py)

## Release Checksums

Use SHA-256 to confirm that a downloaded file matches this release:

```sh
shasum -a 256 digitalownership-1.0.1.oxt
```

Expected SHA-256 values:

```text
digitalownership-1.0.1.oxt  a5915fb18df6db840b5d4dac6fd3441df0f5caf4577480446dc8e857b37f9a5b
digitalownership.oxt       a5915fb18df6db840b5d4dac6fd3441df0f5caf4577480446dc8e857b37f9a5b
digitalownership-verify.py 9ed4b0f054b4a0aad8783809b26f962a7c81563a8d192c6513fbd1767b1e3468
```

The same values are published in [RELEASE-MANIFEST.json](RELEASE-MANIFEST.json).

## Install

1. Download the current `.oxt` file.
2. Open LibreOffice.
3. Choose Tools, Extension Manager, Add.
4. Select the downloaded extension and accept the license.
5. Restart LibreOffice.

## Supported Software

The current plugin is for LibreOffice desktop. It supports documents opened in
LibreOffice Writer, Calc, Impress, and Draw. A Microsoft Word integration is
planned, but this package is not a Microsoft Office add-in.

## Supported File Types

- ODT, ODS, ODP, and ODG.
- DOCX, XLSX, and PPTX opened through LibreOffice.

Older formats such as DOC, XLS, RTF, TXT, and CSV should be saved as one of the
supported formats before registration. Unsupported formats are rejected by the
plugin.

## Verification

Verification is free of charge. Open a registered document in LibreOffice and
click Verify Document. The plugin recalculates the document fingerprint locally
and checks whether that fingerprint is registered on-chain.

Expert users can verify without LibreOffice by using the standalone verifier:

```sh
python3 digitalownership-verify.py "/path/to/document.odt" --json
```

The verifier prints the SHA-512 document fingerprint. When the optional Python
Keccak dependency is available, it also prints the Ethereum registry key.

## More Documentation

- [How it works](docs/how-it-works.md)
- [Manual verification](docs/manual-verification.md)
- [Hash algorithm](docs/hash-algorithm.md)
- [Security notes](SECURITY.md)
- [Changelog](CHANGELOG.md)

Official service website: https://digitalownership.squaredant.com
