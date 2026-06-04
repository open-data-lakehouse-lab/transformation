import pytest
import json
from odl_transformation.readers.local_landing import read_local_json

def test_read_valid_json(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    f = d / "test.json"
    content = {"key": "value"}
    f.write_text(json.dumps(content))
    
    result = read_local_json(f)
    assert result == content

def test_read_missing_file():
    with pytest.raises(FileNotFoundError):
        read_local_json("non_existent_file.json")
