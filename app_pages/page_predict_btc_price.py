import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.machine_learning.data_management import load_btc_data, load_pkl_file
from src.machine_learning.regression_perf_eval import (
    regression_performance,
    regression_evaluation_plots
)


def page_predict_btc_price_body():

    # load bitcoin pipeline files
    version = 'v2'
    btc_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_btc_price/{version}/btc_pipeline_lr.pkl")
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
        f"* Initially we wanted to have a Regressor model to predict tenure for a likely "
        f"churnable prospect, but the **regressor performance did not meet project requirement**: "
        f"0.7 of R2 Score on train and test sets. "
        f"We converted the target to classes and transformed the ML task into a **classification** problem. \n"
        f"* The pipeline was tuned aiming at least 0.8 Recall on '<4 months' class, on train and test sets, "
        f"since we are interested in this project, to detect any prospect that may churn soon. "
        f"The classifer performance was 0.8 on both sets.\n"
        f"* We notice that '<4.0' and '+20.0' classes have reasonable performance levels, where "
        f"'4.0 to 20.0' performance is poor. This fact will be a limitation of our project.")
    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to predict BTC prices T+30.")
    st.write(btc_pipe)
    st.write("---")

    # show best features
    st.write("* The features the model was trained and their importance.")
    selected_features = features_train.columns.to_list()
    st.write(selected_features)
    st.write("---")

    # show feature coefficients used by the model
    st.image("outputs/datasets/figs/lr_coefficients.png", caption="Feature Coefficients")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(features_train, target_train, features_test, target_test, btc_pipe)
    regression_evaluation_plots(features_train, target_train, features_test, target_test, btc_pipe)
