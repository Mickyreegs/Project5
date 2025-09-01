import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import boxcox
import pickle
import numpy as np
from dotenv import load_dotenv
import os
from fredapi import Fred
import yfinance as yf
import pandas as pd

from src.machine_learning.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_bitcoin_price


def get_nasdaq_close(date):
    """
    Fetch Nasdaq close prices from yfinance
    """
    next_day = pd.to_datetime(date) + pd.Timedelta(days=1)
    data = yf.download(
        "^IXIC", start=date, end=next_day.strftime('%Y-%m-%d'), progress=False)
    if not data.empty:
        return float(data["Close"].iloc[0])
    else:
        return None


load_dotenv()
fred_api_key = os.getenv("FRED_API_KEY")
fred = Fred(api_key=fred_api_key)


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

    # FRED mapping
    series_dict = {
        'CPIAUCSL': 'CPI',
        'M2SL': 'M2_Money_Supply',
        'RSAFS': 'Retail_Sales',
        'GDPC1': 'Real_GDP'
    }

    # Fetch macro data from FRED
    date_str = selected_date.strftime('%Y-%m-%d')
    defaults = {}
    for series_id, label in series_dict.items():
        data = fred.get_series(series_id)
        filtered = data[data.index <= pd.to_datetime(date_str)]
        if not filtered.empty:
            defaults[label] = float(filtered.iloc[-1])
        else:
            defaults[label] = 0.0

    # Pull in Nasdaq Close
    nasdaq_close = get_nasdaq_close(selected_date.strftime('%Y-%m-%d'))
    defaults["Nasdaq_Close"] = nasdaq_close if nasdaq_close else 0.00

    # Draw input widgets
    X_live_raw = draw_bitcoin_user_inputs(defaults)

    # Run prediction when button is clicked
    if st.button("Run Predictive Analysis"):
        # Apply Box-Cox transformation using loaded lambdas
        X_live = pd.DataFrame([
            {
                (
                    f"{feature}_lag30_boxcox"
                    if feature != "Real_GDP"
                    else "Real_GDP_lag30"
                ): (
                    boxcox(
                        X_live_raw[feature][0], lmbda=boxcox_lambdas[feature]
                    )
                    if feature != "Real_GDP"
                    else X_live_raw[feature][0]
                )

                for feature in X_live_raw.columns
            }
        ])

        predict_bitcoin_price(
            X_live,
            btc_features,
            btc_pipeline,
            boxcox_lambdas,
            residual_std=0.79,
            reference_date=selected_date
        )


def draw_bitcoin_user_inputs(defaults):
    """
    Draw input widgets for Bitcoin prediction features.
    The only user input required is BitCoin price.
    """
    col1, col2, col3 = st.columns(3)
    X_live = pd.DataFrame([], index=[0])

    with col1:
        X_live["Bitcoin_Close"] = st.number_input(
            "Bitcoin Price (USD) - User Input", value=0.00
        )
        X_live["Nasdaq_Close"] = st.number_input(
            "Nasdaq Index", value=defaults.get("Nasdaq_Close")
        )

    with col2:
        X_live["CPI"] = st.number_input(
            "Consumer Price Index", value=defaults.get("CPI")
        )
        X_live["Retail_Sales"] = st.number_input(
            "Retail Sales (USD)", value=defaults.get("Retail_Sales")
        )

    with col3:
        X_live["M2_Money_Supply"] = st.number_input(
            "M2 Money Supply (USD)", value=defaults.get("M2_Money_Supply")
        )
        X_live["Real_GDP"] = st.number_input(
            "Real GDP (USD)", value=defaults.get("Real_GDP")
        )

    st.caption(
        "BitCoin prices can be sourced from "
        "[Coin Codex](https://coincodex.com/crypto/bitcoin/).  "
        "Visit their site for the close prices on your requested date."
    )
    st.caption(
        "Macroeconomic indicators are automatically pulled from "
        "[FRED](https://fred.stlouisfed.org) based on the selected date. "
        "Visit the site for more info."
    )
    st.caption("Nasdaq Index is auto-filled using Yahoo Finance via yfinance.")

    return X_live
