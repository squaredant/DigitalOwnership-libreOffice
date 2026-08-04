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

To compare a document against a known registered hash:

```sh
python3 digitalownership-verify.py "/path/to/document.odt" --expected-hash "PASTE_SHA512_HASH" --json
```

This script does not upload the document. It reads the file locally and prints
the calculated values.
