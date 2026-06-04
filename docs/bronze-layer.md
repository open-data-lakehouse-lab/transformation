# Bronze Layer

The Bronze layer is the first stage of the data lakehouse transformation process.

## Characteristics

- **Raw Data Preservation**: Each record contains the original payload from the source.
- **Metadata Enrichment**: Adds ingestion and processing metadata (e.g., source, dataset ID, processing date).
- **Format**: Currently stored as local JSONL (JSON Lines) files for simplicity and human readability.

## Structure

Records follow the `BronzeRecord` Pydantic model:

- `dataset_id`: Unique identifier for the dataset.
- `source`: Origin of the data (e.g., `meteocat`).
- `resource`: Specific resource within the dataset.
- `record_type`: Type of record (e.g., `station_metadata`).
- `payload`: The raw data object.
- `ingestion_metadata`: Metadata from the ingestion phase.
- `processing_metadata`: Metadata from the transformation phase.

## Storage Layout

```text
<output-dir>/bronze/<domain>/<source>/<resource>/processing_date=YYYY-MM-DD/records.jsonl
```
