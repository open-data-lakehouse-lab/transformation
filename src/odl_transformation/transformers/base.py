from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from odl_transformation.models.bronze import BronzeRecord

class BaseTransformer(ABC):
    @abstractmethod
    def transform(
        self, 
        resource: str, 
        payload: dict[str, Any] | list[Any], 
        dataset_id: str
    ) -> list[BronzeRecord]:
        pass
