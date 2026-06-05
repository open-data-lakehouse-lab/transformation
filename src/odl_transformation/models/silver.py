from typing import Any, Optional
from pydantic import BaseModel, Field

class SilverRecord(BaseModel):
    dataset_id: str
    source: str
    entity: str
    natural_key: Optional[str] = None
    attributes: dict[str, Any] = Field(default_factory=dict)
    source_payload: dict[str, Any] = Field(default_factory=dict)
    processing_metadata: dict[str, Any] = Field(default_factory=dict)
