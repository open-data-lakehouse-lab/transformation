import pytest
from odl_transformation.transformers.weather.meteocat_silver import MeteocatSilverTransformer

def test_transform_stations_metadata():
    transformer = MeteocatSilverTransformer()
    bronze_records = [
        {"payload": {"codi": "C6", "nom": "Station 1"}},
        {"payload": {"code": "D5", "name": "Station 2"}},
        {"payload": {"station_code": "E3", "name": "Station 3"}},
        {"payload": {"id": "F2", "name": "Station 4"}},
        {"payload": {"other": "No key"}}
    ]
    
    silver_records = transformer.transform("stations-metadata", bronze_records)
    
    assert len(silver_records) == 5
    assert silver_records[0].entity == "stations"
    assert silver_records[0].natural_key == "C6"
    assert silver_records[1].natural_key == "D5"
    assert silver_records[2].natural_key == "E3"
    assert silver_records[3].natural_key == "F2"
    assert silver_records[4].natural_key is None

def test_transform_variables_metadata():
    transformer = MeteocatSilverTransformer()
    bronze_records = [
        {"payload": {"codi": "32", "nom": "Temp"}},
        {"payload": {"code": "1", "name": "Press"}},
        {"payload": {"variable_code": "2", "name": "Hum"}},
        {"payload": {"id": "3", "name": "Wind"}},
        {"payload": {"other": "No key"}}
    ]
    
    silver_records = transformer.transform("variables-metadata", bronze_records)
    
    assert len(silver_records) == 5
    assert silver_records[0].entity == "variables"
    assert silver_records[0].natural_key == "32"
    assert silver_records[1].natural_key == "1"
    assert silver_records[2].natural_key == "2"
    assert silver_records[3].natural_key == "3"
    assert silver_records[4].natural_key is None

def test_transform_measurements():
    transformer = MeteocatSilverTransformer()
    bronze_records = [
        {
            "payload": {
                "station_code": "C6", 
                "variable_code": "32", 
                "timestamp": "2024-06-05T12:00:00Z", 
                "value": 25.5
            }
        },
        {
            "payload": {
                "codiEstacio": "D5", 
                "codiVariable": "1", 
                "data": "2024-06-05T12:00:00Z", 
                "valor": 1013.2
            }
        },
        {
            "payload": {
                "station_code": "E3", 
                "timestamp": "2024-06-05T12:00:00Z", 
                "value": 10.0
            }
        },
        {
            "payload": {
                "id": "MEAS-1", 
                "value": 5.0
            }
        },
        {
            "payload": {"other": "No key"}
        }
    ]
    
    silver_records = transformer.transform("measured-variable", bronze_records)
    
    assert len(silver_records) == 5
    assert silver_records[0].entity == "measurements"
    assert silver_records[0].natural_key == "C6_32_2024-06-05T12:00:00Z"
    assert silver_records[1].natural_key == "D5_1_2024-06-05T12:00:00Z"
    assert silver_records[2].natural_key == "E3_2024-06-05T12:00:00Z"
    assert silver_records[3].natural_key == "MEAS-1"
    assert silver_records[4].natural_key is None

def test_unsupported_resource():
    transformer = MeteocatSilverTransformer()
    with pytest.raises(ValueError, match="Unsupported resource"):
        transformer.transform("unsupported", [])
