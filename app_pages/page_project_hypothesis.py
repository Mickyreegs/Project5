import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from notebooks 2, 3, & 4.
    st.success(
        f"* **Hypothesis 1**: Bitcoin price movements are "
        f"positively correlated with tech stocks and "
        f"macroeconomic indicators — **Confirmed**.  \n"
        f"Correlation and PPS analysis support this. \n\n"

        f"* **Hypothesis 2**: Features within the dataset will impact "
        f"the 30 day price prediction for BitCoin — **Confirmed**.  \n"
        f"Key features selected by the model include "
        f"**BitCoin's lagged price** and **Nasdaq's lagged price**.  \n"
    )
