import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.machine_learning.data_management import load_btc_data, load_pkl_file
from src.machine_learning.regression_perf_eval import (
    regression_performance,
    regression_evaluation_plots
)


def page_ml_training_body():

    # load bitcoin pipeline files
    version = 'v2'
    btc_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_btc_price/{version}/btc_pipeline_rr.pkl")
    features_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_btc_price/{version}/features_train.csv")
    features_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_btc_price/{version}/features_test.csv")
    target_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_btc_price/{version}/target_train.csv")
    target_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_btc_price/{version}/target_test.csv")

    st.write("### ML Pipeline: Predict Bitcoin Price (30-day forecast)")
    # display pipeline training summary conclusions
    st.info(
        f"* Initially we chose a number of models for use in predicting the T+30 "
        f"BitCoin price movement and discovered that  **Ridge Regression was the best performer**: "
        f"0.85+ of R2 Score on train and test sets. "
        f"We first had to transform the final dataset using Box Cox to try to normalise the feature distributions. \n"
        f"* The pipeline determined that an alpha of 0.1 was optimal for this model. "
        f"The performance surpassed expectations on both the Train and Test sets.\n"
        f"* The performance can be summarised as follows:\n"
        f"  * **R²** - Explains 87.1% of the variance in Bitcoin price 30 days ahead.\n"
        f"  * **MAE** - On average, predictions were off by $8,223.37.\n"
        f"  * **MSE** - $119,391,777 - Reflects squared error magnitude.\n"
        f"  * **RMSE** - $10,926.65 - Most forecasts fall within this range.\n"
    )
    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline to predict BTC prices T+30.")
    st.write(btc_pipe)
    st.write("---")

    # show best features
    st.write("* These are the features the model was trained on.")
    selected_features = features_train.columns.to_list()
    st.write(selected_features)
    st.write("---")

    # show feature coefficients used by the model
    st.write("### Key Predictors")
    st.info(
        f"Of the features evaluated above, **Bitcoin's 30 day lagged price** and **Nasdaq's 30 day lagged price** were selected as the key predictors.\n"
        f"Higher absolute values indicate stronger influence on the predicted Bitcoin price."
    )
    st.image("outputs/datasets/figs/linear_vs_ridge_coefficients.png", caption="Feature Coefficients")
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    st.info(
        f"\n"
        f""
    )
    regression_performance(
        features_train, target_train, 
        features_test, target_test, 
        btc_pipe
    )
    regression_evaluation_plots(
        features_train, target_train, 
        features_test, target_test, 
        btc_pipe
    )
