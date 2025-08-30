import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import boxcox
import pickle
import numpy as np

from src.machine_learning.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_bitcoin_price


def page_input_prediction_body():
    """Streamlit page for live Bitcoin price prediction using user input."""

    # Load pipeline and feature list
    btc_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_btc_price/v2/btc_pipeline_rr.pkl"
    )
    btc_features_df = load_pkl_file(
        "outputs/datasets/final_features/BtcFinalFeatures_lag_boxcox.pkl"
    )
    btc_features = btc_features_df.columns.to_list()

    # Load Box-Cox lambda values (you should define or load these earlier)
    with open("outputs/transformers/boxcox_lambdas.pkl", "rb") as f:
        boxcox_lambdas = pickle.load(f)

    selected_date = st.date_input(
    "Select reference date for economic indicators",
    value=pd.Timestamp.today() - pd.Timedelta(days=30)
    )
    st.caption(f"Using data from: **{selected_date.strftime('%B %d, %Y')}**")

    # Draw input widgets
    X_live_raw = draw_bitcoin_user_inputs()

    # Run prediction when button is clicked
    if st.button("Run Predictive Analysis"):
        # Apply Box-Cox transformation using loaded lambdas
        X_live = pd.DataFrame([{
            f"{feature}_lag30_boxcox" if feature != "Real_GDP" else "Real_GDP_lag30":
            boxcox(X_live_raw[feature][0], lmbda=boxcox_lambdas[feature]) if feature != "Real_GDP" else X_live_raw[feature][0]
            for feature in X_live_raw.columns
        }])


        predict_bitcoin_price(
            X_live, 
            btc_features, 
            btc_pipeline,
            boxcox_lambdas,
            residual_std=0.79,
            reference_date=selected_date
        )


def draw_bitcoin_user_inputs():
    """Draw input widgets for Bitcoin prediction features."""
    col1, col2, col3 = st.columns(3)
    X_live = pd.DataFrame([], index=[0])

    with col1:
        X_live["Bitcoin_Close"] = st.number_input("Bitcoin Price (USD)", value=30000.0)
        X_live["Nasdaq_Close"] = st.number_input("Nasdaq Index", value=15000.0)

    with col2:
        X_live["CPI"] = st.number_input("Consumer Price Index", value=305.0)
        X_live["Retail_Sales"] = st.number_input("Retail Sales (USD)", value=710000000000.0)

    with col3:
        X_live["M2_Money_Supply"] = st.number_input("M2 Money Supply (USD)", value=21000000000.0)
        X_live["Real_GDP"] = st.number_input("Real GDP (USD)", value=22000000000000.0)

    return X_live

