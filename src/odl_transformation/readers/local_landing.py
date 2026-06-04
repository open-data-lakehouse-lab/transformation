from __future__ import annotations
import json
from pathlib import Path
from typing import Any

def read_local_json(path: str | Path) -> Any:
    """Reads a JSON file from local filesystem."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"JSON file not found: {p}")
    
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)
