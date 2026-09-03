# How DigitalOwnership Works

DigitalOwnership creates a dated public record for a document fingerprint, not
for the document itself.

When a user clicks Register Document, the LibreOffice plugin calculates a
SHA-512 fingerprint locally. The document content is not uploaded to
DigitalOwnership. The plugin creates a local archive copy, checks its
fingerprint, and sends only the fingerprint to the DigitalOwnership service.

## Register With An Email Address

This is the normal workflow. Enter the email address of your DigitalOwnership
account before registering. DigitalOwnership uses its account-registration
wallet to submit the on-chain registration and links the registration to your
email account. You do not need a crypto wallet or cryptocurrency.

If the plugin needs you to sign in or link this LibreOffice installation to your
account, it opens the account page. Complete that step in the same browser and
return to LibreOffice. After the registration is complete, verify the archive
with the same email address.

## Register With A Crypto Wallet

If you leave the email address empty, the plugin opens the Web3 registration
page. It attempts to register under your connected crypto wallet. You approve
the transaction in that wallet and pay the network gas directly. If that was not
intended, return to LibreOffice and enter your email address instead.

A wallet registration creates evidence that the connected wallet controlled the
registration at that time. You are responsible for access to that wallet.

## Verify And Share

The blockchain record contains the registry key, registrant, and registration
time. The archive copy remains on your computer and is the file that should be
shared for verification. Anyone can verify its fingerprint through
DigitalOwnership, but an email-linked registration requires the registration
email address. Verify an archive before opening, editing, resaving, or
converting it.
