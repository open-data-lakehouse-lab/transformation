from typing import Any, List, Dict, Optional
from odl_transformation.models.silver import SilverRecord

class MeteocatSilverTransformer:
    def transform(
        self, 
        resource: str, 
        bronze_records: List[Dict[str, Any]], 
        dataset_id: str = "meteocat-weather"
    ) -> List[SilverRecord]:
        
        resource_map = {
            "stations-metadata": "stations",
            "variables-metadata": "variables",
            "measured-variable": "measurements",
        }
        
        if resource not in resource_map:
            raise ValueError(f"Unsupported resource for Silver transformation: {resource}")
            
        entity = resource_map[resource]
        silver_records = []
        
        for bronze in bronze_records:
            payload = bronze.get("payload", {})
            natural_key = self._extract_natural_key(resource, payload)
            
            silver_record = SilverRecord(
                dataset_id=dataset_id,
                source="meteocat",
                entity=entity,
                natural_key=natural_key,
                attributes=payload,
                source_payload=payload,
                processing_metadata={}
            )
            silver_records.append(silver_record)
            
        return silver_records

    def _extract_natural_key(self, resource: str, payload: Dict[str, Any]) -> Optional[str]:
        if resource == "stations-metadata":
            for field in ["codi", "code", "station_code", "id"]:
                if field in payload and payload[field] is not None:
                    return str(payload[field])
        
        elif resource == "variables-metadata":
            for field in ["codi", "code", "variable_code", "id"]:
                if field in payload and payload[field] is not None:
                    return str(payload[field])
        
        elif resource == "measured-variable":
            # station_code + variable_code + timestamp
            if all(f in payload for f in ["station_code", "variable_code", "timestamp"]):
                return f"{payload['station_code']}_{payload['variable_code']}_{payload['timestamp']}"
            
            # codiEstacio + codiVariable + data
            if all(f in payload for f in ["codiEstacio", "codiVariable", "data"]):
                return f"{payload['codiEstacio']}_{payload['codiVariable']}_{payload['data']}"
            
            # station_code + timestamp
            if all(f in payload for f in ["station_code", "timestamp"]):
                return f"{payload['station_code']}_{payload['timestamp']}"
            
            # id
            if "id" in payload and payload["id"] is not None:
                return str(payload["id"])
                
        return None
