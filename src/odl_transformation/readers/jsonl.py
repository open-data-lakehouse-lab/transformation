import json
from pathlib import Path
from typing import Any, List, Dict, Union

def read_jsonl(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Reads a local JSONL file and returns a list of dictionaries."""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"JSONL file not found: {path}")
    
    records = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON on line {line_num} of {path}: {e}")
    except Exception as e:
        if isinstance(e, (FileNotFoundError, ValueError)):
            raise e
        raise RuntimeError(f"Error reading JSONL file {path}: {e}")
        
    return records
