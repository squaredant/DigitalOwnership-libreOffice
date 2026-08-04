#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path


HASH_ALGORITHM = "SHA-512"
HASH_SCOPE = "digitalownership-content-v1"
ODF_VOLATILE_ENTRIES = {"meta.xml", "settings.xml"}
ODF_VOLATILE_PREFIXES = ("Thumbnails/",)
OOXML_FORMATS = {
    "docx": {
        "required": "word/document.xml",
        "prefixes": ("word/",),
        "volatile": {"word/settings.xml"},
    },
    "xlsx": {
        "required": "xl/workbook.xml",
        "prefixes": ("xl/",),
        "volatile": {"xl/calcChain.xml"},
    },
    "pptx": {
        "required": "ppt/presentation.xml",
        "prefixes": ("ppt/",),
        "volatile": set(),
    },
}


class UnsupportedDocumentFormat(RuntimeError):
    pass


def compute_document_hash(path):
    doc_path = Path(path)
    if not zipfile.is_zipfile(doc_path):
        raise UnsupportedDocumentFormat(
            f"Unsupported file format for stable DigitalOwnership hashing: {doc_path.suffix or doc_path.name}"
        )

    with zipfile.ZipFile(doc_path, "r") as package:
        names = set(package.namelist())
        if is_odf_package(names):
            return compute_package_hash(package, odf_hash_entries(package))
        ooxml_format = ooxml_format_for(names)
        if ooxml_format:
            return compute_package_hash(package, ooxml_hash_entries(package, ooxml_format))

    raise UnsupportedDocumentFormat(
        f"Unsupported ZIP-based document format for stable DigitalOwnership hashing: {doc_path.suffix or doc_path.name}"
    )


def is_odf_package(names):
    return "mimetype" in names and any(name in names for name in ("content.xml", "META-INF/manifest.xml"))


def ooxml_format_for(names):
    if "[Content_Types].xml" not in names:
        return None
    for format_name, config in OOXML_FORMATS.items():
        if config["required"] in names:
            return format_name
    return None


def odf_hash_entries(package):
    return sorted(
        info.filename
        for info in package.infolist()
        if not info.is_dir()
        and info.filename not in ODF_VOLATILE_ENTRIES
        and not info.filename.startswith(ODF_VOLATILE_PREFIXES)
    )


def ooxml_hash_entries(package, format_name):
    config = OOXML_FORMATS[format_name]
    return sorted(
        info.filename
        for info in package.infolist()
        if not info.is_dir()
        and info.filename.startswith(config["prefixes"])
        and info.filename not in config["volatile"]
    )


def compute_package_hash(package, names):
    digest = hashlib.sha512()
    for name in names:
        data = package.read(name)
        file_digest = hashlib.sha512(data).hexdigest()
        digest.update(b"FILE\x00")
        digest.update(name.encode("utf-8"))
        digest.update(b"\x00")
        digest.update(str(len(data)).encode("ascii"))
        digest.update(b"\x00")
        digest.update(file_digest.encode("ascii"))
        digest.update(b"\x00")
    return digest.hexdigest()


def ethereum_keccak256_text(text):
    try:
        from Crypto.Hash import keccak
    except ImportError:
        return None

    digest = keccak.new(digest_bits=256)
    digest.update(text.encode("utf-8"))
    return f"0x{digest.hexdigest()}"


def main():
    parser = argparse.ArgumentParser(
        description="Verify a DigitalOwnership document fingerprint locally.",
    )
    parser.add_argument("document", help="Path to a supported office document.")
    parser.add_argument("--expected-hash", help="Expected DigitalOwnership SHA-512 content hash.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    try:
        document_hash = compute_document_hash(args.document)
    except Exception as exc:
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc)}, indent=2))
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return 1

    registry_key = ethereum_keccak256_text(document_hash)
    matches = None
    if args.expected_hash:
        matches = document_hash.lower() == args.expected_hash.strip().lower()

    result = {
        "ok": matches is not False,
        "hashScope": HASH_SCOPE,
        "hashAlgorithm": HASH_ALGORITHM,
        "documentHash": document_hash,
        "registryKey": registry_key,
        "registryKeyNote": None
        if registry_key
        else "Install pycryptodome to derive the Ethereum registry key: python3 -m pip install pycryptodome",
        "expectedHashMatches": matches,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Hash scope: {result['hashScope']}")
        print(f"Hash algorithm: {result['hashAlgorithm']}")
        print(f"Document hash: {result['documentHash']}")
        if registry_key:
            print(f"Registry key: {registry_key}")
        else:
            print(result["registryKeyNote"])
        if matches is not None:
            print(f"Expected hash matches: {'yes' if matches else 'no'}")

    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
