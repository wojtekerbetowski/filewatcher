import json
from pathlib import Path
from typing import Dict

def store(path: Path, data: Dict[str, str]) -> str:
    with path.open("w") as f:
        json.dump(data, f)

def load(path: Path) -> Dict[str, str]:
    with path.open("r") as f:
        return json.load(f)
