import pandas as pd


def load_data(filepath):
    """Loads data from a CSV file."""
    return pd.read_csv(filepath)


def clean_data(df):
    """Cleans the dataset (e.g., handle missing values)."""
    # Add cleaning logic

    # Save the cleaned dataset into data/processed/
    return df


import pandas as pd
import os


def load_data(data_path):
    """
    Loads multiple datasets for mental health analysis.

    Args:
        data_path (str): Path to the raw data directory.

    Returns:
        dict: A dictionary containing loaded DataFrames.
    """
    data_files = {
        "Data1": "1- mental-illnesses-prevalence.csv",
        "Data2": "4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv",
        "Data3": "6- depressive-symptoms-across-us-population.csv",
        "Data4": "7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv",
    }

    dataframes = {}
    for name, file in data_files.items():
        file_path = os.path.join(data_path, file)
        try:
            dataframes[name] = pd.read_csv(file_path)
            print(f"{name} loaded successfully.")
        except Exception as e:
            print(f"Error loading {name}: {e}")

    return dataframes


# Example usage
if __name__ == "__main__":
    # Adjust path to your project folder
    data_path = "data/raw"
    datasets = load_data(data_path)

    # You can save cleaned versions of the datasets into the processed folder if needed
    processed_path = "data/processed"
    os.makedirs(processed_path, exist_ok=True)
    for name, df in datasets.items():
        df.to_csv(os.path.join(processed_path, f"{name}_processed.csv"), index=False)
