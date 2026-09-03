# Manual Verification

The recommended verification method is the LibreOffice plugin. The standalone
script is provided for expert users who want to independently recalculate a
document fingerprint.

## Run The Verifier

```sh
python3 digitalownership-verify.py "/path/to/document.odt" --json
```

The output contains:

- `documentHash`: the local SHA-512 fingerprint.
- `hashScope`: the algorithm scope, currently `digitalownership-content-v1`.
- `registryKey`: the Ethereum contract key, when Python Keccak support is available.
- `expectedHashMatches`: true or false when `--expected-hash` is provided.

## Check A Registration Online

Use `--chain` to query the configured DigitalOwnership verification service:

```sh
python3 digitalownership-verify.py "/path/to/document.odt" --chain
```

For an email-linked registration, provide the same registration email:

```sh
python3 digitalownership-verify.py "/path/to/document.odt" --chain --email owner@example.com
```

The script sends the calculated fingerprint, and the email address when given,
to the verification service. It does not upload the document.

To compare a document against a known registered hash:

```sh
python3 digitalownership-verify.py "/path/to/document.odt" --expected-hash "PASTE_SHA512_HASH" --json
```

## Check The Downloaded Script

Before running the verifier, you can compare its SHA-256 checksum with
`RELEASE-MANIFEST.json`:

```sh
shasum -a 256 digitalownership-verify.py
```
