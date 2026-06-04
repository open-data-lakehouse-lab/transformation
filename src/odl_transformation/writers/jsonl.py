from __future__ import annotations
from pathlib import Path
from odl_transformation.models.bronze import BronzeRecord
from odl_transformation.utils.dates import get_current_utc_date_str

def write_bronze_jsonl(
    records: list[BronzeRecord], 
    output_dir: str | Path,
    dataset_id: str,
    resource: str
) -> Path:
    """Writes bronze records to JSONL in the expected layout."""
    processing_date = get_current_utc_date_str()
    
    # Path: <output-dir>/bronze/weather/meteocat/<resource>/processing_date=YYYY-MM-DD/records.jsonl
    # Note: Hardcoded 'weather/meteocat' for now as per requirements
    target_dir = (
        Path(output_dir) 
        / "bronze" 
        / "weather" 
        / "meteocat" 
        / resource 
        / f"processing_date={processing_date}"
    )
    target_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = target_dir / "records.jsonl"
    
    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(record.model_dump_json() + "\n")
            
    return output_path
