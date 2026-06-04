# Transformation Design

This document describes the design principles of the `transformation` repository.

## Principles

- **Local-first**: Transformations are designed to run locally without requiring complex infrastructure.
- **Abstraction**: Use readers, transformers, and writers to decouple data sources, transformation logic, and output formats.
- **Bronze-first**: Initial focus is on creating a reliable bronze layer that preserves raw data with added metadata.

## Architecture

- **Readers**: Responsible for fetching raw data (e.g., local JSON files).
- **Transformers**: Normalize raw payloads into `BronzeRecord` models.
- **Writers**: Persist records into the desired output format (e.g., JSONL).

## Future Evolution

As the project grows, we may introduce:
- Silver and Gold layer transformations.
- Support for more complex data formats (e.g., Parquet).
- Integration with external metadata catalogs.
