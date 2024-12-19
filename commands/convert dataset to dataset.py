# sections: folders, ai

import pandas as pd
import sys
from pathlib import Path


def convert_dataset(input_file, output_file):
    """Convert a dataset from one format to another based on file extension."""
    try:
        # Determine input and output formats
        input_extension = Path(input_file).suffix
        output_extension = Path(output_file).suffix

        # Read the input file based on its format
        if input_extension == ".csv":
            data = pd.read_csv(input_file)
        elif input_extension == ".json":
            data = pd.read_json(input_file)
        elif input_extension == ".xlsx":
            data = pd.read_excel(input_file)
        elif input_extension == ".parquet":
            data = pd.read_parquet(input_file)
        else:
            print(f"Unsupported input format: {input_extension}")
            return

        # Write to the output file based on the specified format
        if output_extension == ".csv":
            data.to_csv(output_file, index=False)
        elif output_extension == ".json":
            data.to_json(output_file, orient="records", lines=True)
        elif output_extension == ".xlsx":
            data.to_excel(output_file, index=False)
        elif output_extension == ".parquet":
            data.to_parquet(output_file, index=False)
        else:
            print(f"Unsupported output format: {output_extension}")
            return

        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    except Exception as e:
        print(f"Error converting file: {e}")


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python convert_datasets.py <input_file> <output_file>")
        sys.exit(1)

    # Get the input and output file paths from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the input file exists
    if not Path(input_file).is_file():
        print(f"The file '{input_file}' does not exist.")
        sys.exit(1)

    # Convert the dataset
    convert_dataset(input_file, output_file)
