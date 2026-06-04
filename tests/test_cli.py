from typer.testing import CliRunner
from odl_transformation.cli import app
import json

runner = CliRunner()

def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "odl-transformation version" in result.stdout

def test_transform_stations(tmp_path):
    input_file = tmp_path / "stations.json"
    input_file.write_text(json.dumps([{"codi": "123"}]))
    
    output_dir = tmp_path / "data"
    
    result = runner.invoke(app, [
        "transform",
        "--dataset", "meteocat-weather",
        "--resource", "stations-metadata",
        "--input-path", str(input_file),
        "--output-dir", str(output_dir)
    ])
    
    assert result.exit_code == 0
    assert "Transformation successful" in result.stdout
    
    # Check if file exists
    # Layout: <output-dir>/bronze/weather/meteocat/stations-metadata/processing_date=YYYY-MM-DD/records.jsonl
    # We can use glob to find it
    jsonl_files = list(output_dir.glob("**/records.jsonl"))
    assert len(jsonl_files) == 1
