# Open Data Lakehouse Lab - Transformation

The `transformation` repository is responsible for transforming raw landing data into cleaner lakehouse-oriented layers.

## Overview

Initial scope:
- Read local landing JSON files produced by the ingestion repository.
- Normalize Meteocat payloads into bronze records.
- Write local JSONL outputs.
- Provide CLI-based transformation workflows.
- Provide tests without network access or API keys.

## Supported Meteocat Resources

- `stations-metadata`
- `variables-metadata`
- `measured-variable`

## Getting Started

### Prerequisites

- Python 3.12+

### Installation

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pip install -e .
```

### Run CLI

```bash
odl-transformation version

odl-transformation transform \
  --dataset meteocat-weather \
  --resource stations-metadata \
  --input-path ./examples/landing/meteocat/stations-metadata.json \
  --output-dir ./data
```

### Validation

```bash
bash scripts/validate.sh
```

## Bronze Layer

Schemas are currently in the **bronze** stage, meaning they are minimal normalizations of raw payloads with added metadata. They are not yet final analytics models (silver/gold).

## Licensing

See [LICENSE](LICENSE) and [NOTICE](NOTICE) files.
