import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.machine_learning.data_management import load_btc_data, load_pkl_file
from src.machine_learning.regression_perf_eval import (
    regression_performance,
    regression_evaluation_plots
)
from src.machine_learning.loaders import load_model_and_data
from src.machine_learning.plotting import plot_actual_vs_predicted_plotly



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
        f"* Initially we chose several models for use in predicting the T+30 "
        f"BitCoin price movement and discovered that "
        f"**Ridge Regression was the best performer**: \n"
        f"0.85+ of R2 Score on train and test sets. "
        f"We first had to transform the final dataset using Box Cox "
        f"in an attempt to normalise the feature distributions. \n"
        f"* The pipeline determined an alpha of 0.1 was optimal. "
        f"The performance surpassed expectations"
        f"on both the Train and Test sets.\n"
        f"* The performance can be summarised as follows:\n"
        f"  * **R²** - Explains 87.1% of the variance in Bitcoin price "
        f"30 days ahead.\n"
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

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    st.info(
        f"* BitCoin's recent history has shown "
        f"a high level of volatility.  \n"
        f"* Back in 2010, "
        f"when prices were first being determined for BitCoin, "
        f" it was very stable with a gradual increase.  \n"
        f"* 2018 saw the first spike, "
        f"followed by a reduction and a period of calm.  \n"
        f"* This was followed by 2 spikes in 2021 and 2022.  \n"
        f"* BitCoin has since reached record levels, "
        f"and as at 31/07/2025 it closed at $170,800."
    )
    st.image(
        "outputs/datasets/figs/bitcoin_price_history.png",
        caption="BitCoin Price History"
    )

    st.info(
        f"* As a result of this volatility, "
        f"BitCoin's distribution is very skewed.  \n"
        f"* See the below graph for reference."
    )
    st.image(
        "outputs/datasets/figs/bitcoin_distribution.png",
        caption="BitCoin Distribution"
    )

    st.info(
        f"* We use Box Cox transformation on the price"
        f" and a number of features to help the model.  \n"
        f"* This helped somewhat, but still isn't perfect.  "
        f"See graph below of transformed features."
    )

    st.image(
        "outputs/datasets/figs/feature_distributions_boxcox.png",
        caption="Transformed Features' Distributions"
    )

    st.info(
        f"* We proceeded to train 3 models - "
        f"Linear Regression, Rideg Regression & Lasso Regression.  \n"
        f"* Linear and Ridge were very close in comparison.  "
        f"We were able to drop Lasso early.  \n"
        f"* Both models placed a large emphasis on the lagged BitCoin"
        f" and Nasdaq close prices.  \n"
        f"* These are seen as the **key predictors**. "
    )

    st.image(
        "outputs/datasets/figs/linear_vs_ridge_coefficients.png",
        caption="Feature Coefficients"
    )

    st.info(
        f"* In the end we selected Ridge Regression "
        f"to predict our BitCoin 30 day price.  \n"
        f"* The performance very slightly edged that of Linear Regression.  \n"
        f"* The performance metrics can be seen below:  \n"
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

    st.info(
        f"* Finally, in reviewing the actual versus predicted price, "
        f"we see decent performance from the model.  \n"
        f"* The extreme volatility does at times cause misalignment, "
        f"but the overall trend is good.  \n"
        f"* We have achieved an R2 above our expectation of "
        f"0.85 and the RMSE is decent given BitCoin's volatility.  \n"
        f"* We believe this is a good model to predict future trends "
        f"for the client.  \n"
        f"* It will assist the client with decision making for "
        f"entry and exit points in crypto portfolios."
    )

    # visualise actual versus prediction
    st.header("Model Training Results")
    st.caption("Hover over points to compare actual vs. predicted prices.")

    model, features, target, selected_features = load_model_and_data()

    lambda_target = 0.1347407526217442

    fig = plot_actual_vs_predicted_plotly(
        model=model,
        features=features,
        target=target,
        selected_features=selected_features,
        lambda_target=lambda_target
    )

    st.plotly_chart(fig, use_container_width=True)

