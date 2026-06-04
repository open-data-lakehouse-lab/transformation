import typer
from pathlib import Path

from odl_transformation.readers.local_landing import read_local_json
from odl_transformation.transformers.weather.meteocat import MeteocatTransformer
from odl_transformation.writers.jsonl import write_bronze_jsonl
from odl_transformation.validation.records import validate_input_payload, validate_bronze_records

app = typer.Typer(help="Open Data Lakehouse Lab Transformation CLI")

@app.command()
def version() -> None:
    """Print the version of the CLI."""
    typer.echo("odl-transformation version 0.1.0")

@app.command()
def transform(
    dataset: str = typer.Option(..., "--dataset", help="Dataset ID (e.g. meteocat-weather)"),
    resource: str = typer.Option(..., "--resource", help="Resource name"),
    input_path: Path = typer.Option(..., "--input-path", help="Path to input JSON file"),
    output_dir: Path = typer.Option(..., "--output-dir", help="Directory for output files"),
) -> None:
    """Transform raw landing data into bronze records."""
    try:
        # Read
        payload = read_local_json(input_path)
        validate_input_payload(payload)
        
        # Transform (Only Meteocat supported for now)
        if "meteocat" in dataset:
            transformer = MeteocatTransformer()
        else:
            typer.echo(f"Unsupported dataset: {dataset}", err=True)
            raise typer.Exit(code=1)
            
        records = transformer.transform(resource=resource, payload=payload, dataset_id=dataset)
        validate_bronze_records(records)
        
        # Write
        output_path = write_bronze_jsonl(
            records=records, 
            output_dir=output_dir, 
            dataset_id=dataset, 
            resource=resource
        )
        
        typer.echo(f"Transformation successful. Output written to: {output_path}")
        
    except Exception as e:
        typer.echo(f"Error during transformation: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
