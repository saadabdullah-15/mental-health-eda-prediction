import pandas as pd


def encode_categorical(df, columns):
    """Encodes categorical columns."""
    return pd.get_dummies(df, columns=columns)


def scale_features(df, scaler):
    """Scales numerical features."""
    return scaler.fit_transform(df)
