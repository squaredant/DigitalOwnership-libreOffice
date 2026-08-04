# How DigitalOwnership Works

DigitalOwnership creates a dated public record for a document fingerprint, not
for the document itself.

When a user clicks Register Document, the LibreOffice plugin calculates a
SHA-512 fingerprint locally. The document content is not uploaded to
DigitalOwnership. The web app receives only the fingerprint and registers a
contract key derived from it on Arbitrum.

The blockchain record shows the registered fingerprint key, the wallet address,
and the registration time. The plugin can then store registration metadata in
the document and create a read-only archive copy for the user's own records.

## Wallet Control

The registration is associated with the wallet address used for the transaction
or signature. This does not prove legal authorship by itself, but it creates a
dated record that the user controlled that wallet address when registering the
document fingerprint.

## Credits And Direct Wallet Registration

The normal hosted workflow uses registration credits purchased through the
DigitalOwnership website. Expert users can instead register directly with their
own crypto wallet and pay Arbitrum gas themselves. Direct wallet registrations
are outside the credit, support, and refund workflow.
