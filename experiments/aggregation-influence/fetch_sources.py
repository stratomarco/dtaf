"""Fetch only the pinned public source files listed in sources.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path, PurePosixPath


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    manifest = json.loads(Path(__file__).with_name("sources.json").read_text())
    for entry in manifest["files"]:
        relative = PurePosixPath(entry["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Unsafe source path")
        target = args.destination / entry["path"]
        if target.exists():
            data = target.read_bytes()
            if hashlib.sha256(data).hexdigest() != entry["sha256"]:
                raise ValueError(f"Refusing to replace different file: {target}")
        else:
            with urllib.request.urlopen(entry["raw_url"], timeout=60) as response:
                data = response.read()
            if hashlib.sha256(data).hexdigest() != entry["sha256"]:
                raise ValueError(f"Digest mismatch: {target}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    print(f"Verified {len(manifest['files'])} pinned files")


if __name__ == "__main__":
    main()
