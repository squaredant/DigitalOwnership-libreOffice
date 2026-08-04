# Security Notes

The public plugin package should never contain private keys, database
credentials, Stripe secrets, internal relayer code, or server deployment files.

Before publishing a release:

1. Rebuild the LibreOffice extension.
2. Run the plugin tests.
3. Confirm the bundled plugin configuration points to production URLs.
4. Confirm the public verifier calculates the same hash as the plugin.
5. Publish a versioned OXT filename to avoid browser cache issues.

Report security concerns through the support form on
https://digitalownership.squaredant.com/support.
