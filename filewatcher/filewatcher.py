import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set

from . import hasher, snapshot_repository, traverser


@dataclass
class Changes:
    removed: Set[str] = field(default_factory=set)
    new: Set[str] = field(default_factory=set)
    changed: Set[str] = field(default_factory=set)


def _snapshot(directory: Path):
    files = traverser.list_files(directory)

    return {
        str(file.relative_to(directory)): hasher.hash_content(file)
        for file in files
    }


def save(directory: Path, snapshot: Path) -> None:
    """Saves a snapshot with the hashed contents to the disk"""

    data = _snapshot(directory)

    with snapshot.open("w") as f:
        json.dump(data, f)


def verify(directory: Path, snapshot: Path) -> Changes:
    """Loads the stored snapshot and verifies whether files changed"""

    with snapshot.open("r") as f:
        loaded = json.load(f)
    
    current = _snapshot(directory)
    
    return Changes(
        removed=loaded.keys() - current.keys(),
        new=current.keys() - loaded.keys(),
        changed={
            key
            for key in current.keys() & loaded.keys()
            if current[key] != loaded[key]
        },
    )
