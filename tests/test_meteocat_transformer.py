from odl_transformation.transformers.weather.meteocat import MeteocatTransformer

def test_transform_list_payload():
    transformer = MeteocatTransformer()
    payload = [{"a": 1}, {"a": 2}]
    records = transformer.transform("stations-metadata", payload)
    assert len(records) == 2
    assert records[0].payload == {"a": 1}
    assert records[1].payload == {"a": 2}
    assert records[0].record_type == "station_metadata"

def test_transform_dict_with_container():
    transformer = MeteocatTransformer()
    payload = {"variables": [{"id": "v1"}, {"id": "v2"}]}
    records = transformer.transform("variables-metadata", payload)
    assert len(records) == 2
    assert records[0].payload == {"id": "v1"}

def test_transform_unknown_dict():
    transformer = MeteocatTransformer()
    payload = {"unknown": "data"}
    records = transformer.transform("measured-variable", payload)
    assert len(records) == 1
    assert records[0].payload == payload
    assert records[0].record_type == "measured_variable"

def test_transform_all_resources():
    transformer = MeteocatTransformer()
    resources = ["stations-metadata", "variables-metadata", "measured-variable"]
    for res in resources:
        records = transformer.transform(res, {"k": "v"})
        assert len(records) == 1
        assert records[0].resource == res
