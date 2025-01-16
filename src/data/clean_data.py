import os
import sys
import pandas as pd
from src.data.load_data import load_data

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, project_root)


def clean_data(dataframes):
    """
    Cleans the datasets by handling missing values and standardizing column names.

    Args:
        dataframes (dict): A dictionary of DataFrames to clean.

    Returns:
        dict: Cleaned DataFrames.
    """
    cleaned_data = {}
    for name, df in dataframes.items():
        print(f"\nCleaning {name}...")

        # Check for missing values
        print(f"Missing values in {name}:\n{df.isnull().sum()}")

        # Handle missing values
        df.fillna(method="ffill", inplace=True)  # Forward fill as an example
        df.fillna(method="bfill", inplace=True)  # Backward fill as a backup
        print(f"Missing values handled in {name}.")

        # Standardize column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        print(f"Column names standardized for {name}.")

        # Save cleaned DataFrame
        cleaned_data[name] = df

    return cleaned_data


def main():
    # Paths
    raw_path = os.path.join(project_root, "data", "raw")
    processed_path = os.path.join(project_root, "data", "processed")
    os.makedirs(processed_path, exist_ok=True)

    # Load raw data
    print("Loading raw data...")
    datasets = load_data(raw_path)

    # Clean data
    print("Cleaning datasets...")
    cleaned_datasets = clean_data(datasets)

    # Save cleaned data
    print("Saving cleaned datasets...")
    for name, df in cleaned_datasets.items():
        output_file = os.path.join(processed_path, f"{name}_cleaned.csv")
        df.to_csv(output_file, index=False)
        print(f"Cleaned {name} saved to {output_file}.")


if __name__ == "__main__":
    main()
