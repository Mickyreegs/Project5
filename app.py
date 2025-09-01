import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_corr_pps_study import page_corr_pps_study_body
from app_pages.page_ml_training import page_ml_training_body
from app_pages.page_input_prediction import page_input_prediction_body

# Create an instance of the app
app = MultiPage(app_name="BitCoin Price Predictor")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Correlation and PPS Analysis", page_corr_pps_study_body)
app.add_page("ML: BitCoin ML Model Training", page_ml_training_body)
app.add_page("ML: BitCoin 30 Day Prediction", page_input_prediction_body)

# Run the  app
app.run()
