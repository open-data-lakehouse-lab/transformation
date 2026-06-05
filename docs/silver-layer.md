# Silver Layer

The Silver layer provides a local foundation for structured data records.

## Overview

Silver records are derived from Bronze JSONL records. They are intentionally minimal and schema-flexible, serving as a middle ground between raw ingested data and final analytics models.

## Record Model

Defined in `src/odl_transformation/models/silver.py`:

- `dataset_id`: ID of the dataset.
- `source`: Source system (e.g., `meteocat`).
- `entity`: Target entity (e.g., `stations`, `variables`, `measurements`).
- `natural_key`: Extracted business key for the record.
- `attributes`: Flexible dictionary of record attributes.
- `source_payload`: Original payload from the bronze record.
- `processing_metadata`: Metadata about the transformation process.

## Supported Entities

### Meteocat Weather

| Bronze Resource | Silver Entity |
|-----------------|---------------|
| `stations-metadata` | `stations` |
| `variables-metadata` | `variables` |
| `measured-variable` | `measurements` |

## Usage

To transform bronze records to silver:

```bash
odl-transformation transform-silver \
  --dataset meteocat-weather \
  --resource stations-metadata \
  --input-path ./examples/bronze/meteocat/stations-metadata.jsonl \
  --output-dir ./data
```

## Storage Layout

Silver records are stored in JSONL format:

```text
<output-dir>/silver/weather/meteocat/<entity>/processing_date=YYYY-MM-DD/records.jsonl
```

## Limitations

- Source schema is still subject to change.
- Natural keys are best-effort based on known fields.
- No complex business rules are applied at this stage.
- No deduplication strategy is implemented yet.
- This is not a final analytics model.
