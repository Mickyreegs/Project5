import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_corr_pps_study import page_corr_pps_study_body
from app_pages.page_predict_btc_price import page_predict_btc_price_body

app = MultiPage(app_name= "BitCoin Price Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Correlation and PPS Analysis", page_corr_pps_study_body)
app.add_page("ML: BitCoin Price Analysis", page_predict_btc_price_body)

app.run() # Run the  app