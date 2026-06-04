from typing import Any
from odl_transformation.models.bronze import BronzeRecord
from odl_transformation.transformers.base import BaseTransformer

class MeteocatTransformer(BaseTransformer):
    def transform(
        self, 
        resource: str, 
        payload: Any, 
        dataset_id: str = "meteocat-weather"
    ) -> list[BronzeRecord]:
        
        record_type_map = {
            "stations-metadata": "station_metadata",
            "variables-metadata": "variable_metadata",
            "measured-variable": "measured_variable",
        }
        
        record_type = record_type_map.get(resource, resource)
        
        items: list[Any] = []
        
        if isinstance(payload, list):
            items = payload
        elif isinstance(payload, dict):
            # Check for known container keys
            containers = {
                "stations-metadata": ["stations", "estacions"],
                "variables-metadata": ["variables", "variables_auxiliars"],
                "measured-variable": ["data", "dades", "observations", "observacions"],
            }
            
            found_container = False
            for key in containers.get(resource, []):
                if key in payload and isinstance(payload[key], list):
                    items = payload[key]
                    found_container = True
                    break
            
            if not found_container:
                items = [payload]
        else:
            items = [payload]

        return [
            BronzeRecord(
                dataset_id=dataset_id,
                source="meteocat",
                resource=resource,
                record_type=record_type,
                payload=item if isinstance(item, dict) else {"value": item},
            )
            for item in items
        ]
