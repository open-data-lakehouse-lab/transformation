from __future__ import annotations
from pathlib import Path
from typing import Protocol, Any, List, Union
from odl_transformation.utils.dates import get_current_utc_date_str

class WritableRecord(Protocol):
    def model_dump_json(self) -> str: ...

def _write_jsonl(
    records: List[Any],
    output_dir: Union[str, Path],
    layer: str,
    dataset_id: str,
    entity: str
) -> Path:
    """Internal helper to write records to JSONL in the expected layout."""
    processing_date = get_current_utc_date_str()
    
    # Path: <output-dir>/<layer>/weather/meteocat/<entity>/processing_date=YYYY-MM-DD/records.jsonl
    target_dir = (
        Path(output_dir) 
        / layer
        / "weather" 
        / "meteocat" 
        / entity 
        / f"processing_date={processing_date}"
    )
    target_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = target_dir / "records.jsonl"
    
    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            if hasattr(record, "model_dump_json"):
                f.write(record.model_dump_json() + "\n")
            else:
                import json
                f.write(json.dumps(record) + "\n")
            
    return output_path

def write_bronze_jsonl(
    records: List[Any], 
    output_dir: Union[str, Path],
    dataset_id: str,
    resource: str
) -> Path:
    """Writes bronze records to JSONL in the expected layout."""
    return _write_jsonl(
        records=records,
        output_dir=output_dir,
        layer="bronze",
        dataset_id=dataset_id,
        entity=resource
    )

def write_silver_jsonl(
    records: List[Any],
    output_dir: Union[str, Path],
    dataset_id: str,
    entity: str
) -> Path:
    """Writes silver records to JSONL in the expected layout."""
    return _write_jsonl(
        records=records,
        output_dir=output_dir,
        layer="silver",
        dataset_id=dataset_id,
        entity=entity
    )
