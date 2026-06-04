# Meteocat Transformation Plan

This document outlines the strategy for transforming Meteocat weather data.

## Supported Resources

- `stations-metadata`: Information about weather stations.
- `variables-metadata`: Definitions of measured variables.
- `measured-variable`: Actual measurements from stations.

## Current Strategy

- **Generic Normalization**: We identify common container keys (e.g., `stations`, `variables`, `dades`) to extract lists of records.
- **Bronze Records**: We wrap each extracted item in a `BronzeRecord` model.

## Future Enhancements

- **Schema Verification**: Validate that raw payloads match expected source schemas.
- **Variable-code Enrichment**: Map internal Meteocat codes to standardized names.
- **Silver Layer**: Flatten and type-cast records into a more analytical format.
- **Gold Layer**: Aggregated views for dashboards and analytics.
