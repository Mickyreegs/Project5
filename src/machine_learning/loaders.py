import joblib
import pandas as pd


def load_model_and_data():
    """
    Load the trained model and test data for prediction and visualization.
    """

    model = joblib.load(
        "outputs/ml_pipeline/predict_btc_price/v2/btc_pipeline_rr.pkl"
    )
    features = pd.read_csv(
        "outputs/ml_pipeline/predict_btc_price/v2/features_test.csv"
    )
    target = pd.read_csv(
        "outputs/ml_pipeline/predict_btc_price/v2/target_test.csv"
    ).squeeze()
    selected_features = [
        'Bitcoin_Close_lag30_boxcox',
        'Nasdaq_Close_lag30_boxcox',
        'CPI_lag30_boxcox',
        'Retail_Sales_lag30_boxcox',
        'M2_Money_Supply_lag30_boxcox',
        'Real_GDP_lag30'
    ]
    return model, features, target, selected_features
