import os
from src.data.load_data import load_data


def test_load_data():
    data_path = "data/raw"
    datasets = load_data(data_path)
    assert isinstance(datasets, dict)
    for name, df in datasets.items():
        assert not df.empty, f"{name} is empty!"
