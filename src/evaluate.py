from sklearn.metrics import classification_report, accuracy_score
import pandas as pd


def evaluate_model(y_true: pd.Series, y_pred: pd.Series) -> dict:
    """Compute evaluation metrics for sentiment predictions."""
    report = classification_report(y_true, y_pred, output_dict=True)
    accuracy = accuracy_score(y_true, y_pred)
    return {"accuracy": accuracy, "report": report}
