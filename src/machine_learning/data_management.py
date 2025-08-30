import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_btc_data():
    df = pd.read_pickle("outputs/datasets/final_features/BtcFinalFeatures_lag_boxcox.pkl")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)