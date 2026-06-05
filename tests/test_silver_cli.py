import json
from pathlib import Path
from typer.testing import CliRunner
from odl_transformation.cli import app

runner = CliRunner()

def test_transform_silver_stations(tmp_path):
    output_dir = tmp_path / "data"
    input_path = Path("examples/bronze/meteocat/stations-metadata.jsonl")
    
    result = runner.invoke(app, [
        "transform-silver",
        "--dataset", "meteocat-weather",
        "--resource", "stations-metadata",
        "--input-path", str(input_path),
        "--output-dir", str(output_dir)
    ])
    
    assert result.exit_code == 0
    assert "Silver transformation successful" in result.stdout
    
    # Check output exists and is valid
    # Path: <output-dir>/silver/weather/meteocat/stations/processing_date=YYYY-MM-DD/records.jsonl
    silver_files = list(output_dir.glob("silver/weather/meteocat/stations/*/records.jsonl"))
    assert len(silver_files) == 1
    
    with open(silver_files[0], "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
        record = json.loads(lines[0])
        assert record["entity"] == "stations"
        assert record["natural_key"] == "C6"

def test_transform_silver_unsupported_resource(tmp_path):
    output_dir = tmp_path / "data"
    input_path = Path("examples/bronze/meteocat/stations-metadata.jsonl")
    
    result = runner.invoke(app, [
        "transform-silver",
        "--dataset", "meteocat-weather",
        "--resource", "unsupported",
        "--input-path", str(input_path),
        "--output-dir", str(output_dir)
    ])
    
    assert result.exit_code != 0
    assert "Error during silver transformation" in result.stdout

def test_transform_silver_unsupported_dataset(tmp_path):
    output_dir = tmp_path / "data"
    input_path = Path("examples/bronze/meteocat/stations-metadata.jsonl")
    
    result = runner.invoke(app, [
        "transform-silver",
        "--dataset", "unsupported",
        "--resource", "stations-metadata",
        "--input-path", str(input_path),
        "--output-dir", str(output_dir)
    ])
    
    assert result.exit_code != 0
    assert "Unsupported dataset for silver" in result.stdout
