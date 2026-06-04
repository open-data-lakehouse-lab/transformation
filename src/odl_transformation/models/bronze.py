from typing import Any
from pydantic import BaseModel, Field

class BronzeRecord(BaseModel):
    dataset_id: str
    source: str
    resource: str
    record_type: str
    payload: dict[str, Any]
    ingestion_metadata: dict[str, Any] = Field(default_factory=dict)
    processing_metadata: dict[str, Any] = Field(default_factory=dict)
