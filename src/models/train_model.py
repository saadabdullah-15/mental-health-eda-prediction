from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model(X_train, y_train):
    """Trains a Random Forest model."""
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluates the model."""
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)
