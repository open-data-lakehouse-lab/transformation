import json
from odl_transformation.models.bronze import BronzeRecord
from odl_transformation.writers.jsonl import write_bronze_jsonl

def test_write_bronze_jsonl(tmp_path):
    records = [
        BronzeRecord(
            dataset_id="test-ds",
            source="test-src",
            resource="test-res",
            record_type="test-type",
            payload={"k": "v"}
        )
    ]
    
    output_path = write_bronze_jsonl(
        records=records,
        output_dir=tmp_path,
        dataset_id="test-ds",
        resource="test-res"
    )
    
    assert output_path.exists()
    assert "bronze/weather/meteocat/test-res" in str(output_path)
    
    with open(output_path, "r") as f:
        line = f.readline()
        data = json.loads(line)
        assert data["payload"] == {"k": "v"}
        assert data["dataset_id"] == "test-ds"
