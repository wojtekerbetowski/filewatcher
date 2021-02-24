from hashlib import sha1
from pathlib import Path


def hash_content(path: Path) -> str:
    with path.open("rb") as f:
        return sha1(f.read()).hexdigest()
