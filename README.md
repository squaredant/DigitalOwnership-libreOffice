# DigitalOwnership LibreOffice Plugin

DigitalOwnership lets creators register a unique fingerprint of a supported
office document on Arbitrum. The document stays on the user's computer. The
public blockchain record stores the registration, not the document content.

## Download

- LibreOffice extension: [digitalownership-1.0.5.oxt](downloads/digitalownership-1.0.5.oxt)
- Compatibility alias: [digitalownership.oxt](downloads/digitalownership.oxt)
- Manual verifier: [digitalownership-verify.py](downloads/digitalownership-verify.py)

## Release Checksums

Use SHA-256 to confirm that a downloaded file matches this release:

```sh
shasum -a 256 digitalownership-1.0.5.oxt
```

Expected SHA-256 values:

```text
digitalownership-1.0.5.oxt  9d28aaf5c90a7f0abf4d4525e32d821aab474c9e2ff752564afd2e9af90cb629
digitalownership.oxt       9d28aaf5c90a7f0abf4d4525e32d821aab474c9e2ff752564afd2e9af90cb629
digitalownership-verify.py 25c546bf304343073e447fca9d7e39d140c3b5850d4882a1fd2fa6c0601d1e86
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
and checks whether it is registered on-chain. For an email-linked registration,
enter the same email address used when registering. For a wallet registration,
leave the email field empty.

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
