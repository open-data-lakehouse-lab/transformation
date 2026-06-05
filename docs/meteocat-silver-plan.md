# Meteocat Silver Transformation Plan

This document outlines the plan for implementing Silver transformations for Meteocat weather data.

## Goal

Support `bronze JSONL -> silver JSONL` for Meteocat resources.

## Implementation Details

### Model

A generic `SilverRecord` Pydantic model is used to ensure consistency across different entities while remaining flexible.

### Reader

A dedicated JSONL reader is implemented to read bronze records.

### Transformer: `MeteocatSilverTransformer`

Handles the mapping from bronze resources to silver entities.

#### Entity Mapping

- `stations-metadata` -> `stations`
- `variables-metadata` -> `variables`
- `measured-variable` -> `measurements`

#### Natural Key Extraction

Best-effort extraction based on known fields:
- Stations: `codi`, `code`, `station_code`, `id`
- Variables: `codi`, `code`, `variable_code`, `id`
- Measurements: Composite keys (station + variable + timestamp) or `id`

### Writer

The JSONL writer is updated to support the silver layer layout:
`<output-dir>/silver/weather/meteocat/<entity>/processing_date=YYYY-MM-DD/records.jsonl`

## Validation

- Automated tests for transformer logic.
- Automated tests for CLI integration.
- Manual verification with example data.

## Future Work

- Evaluate Parquet and other columnar formats for future Silver/Gold layers.
- Implement data quality checks at the Silver layer.
- Add deduplication logic.
- Develop Gold layer analytics models.
