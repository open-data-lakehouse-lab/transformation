import json
from typing import Any
from odl_transformation.models.bronze import BronzeRecord

def validate_input_payload(payload: Any) -> None:
    if not payload:
        raise ValueError("Input payload is empty")

def validate_bronze_records(records: list[BronzeRecord]) -> None:
    if not records:
        raise ValueError("No bronze records produced")
    
    for record in records:
        try:
            json.dumps(record.model_dump())
        except (TypeError, OverflowError) as e:
            raise ValueError(f"Record is not JSON serializable: {e}")
