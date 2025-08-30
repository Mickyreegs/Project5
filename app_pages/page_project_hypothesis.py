import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from notebooks 2, 3, & 4.
    st.success(
        "* **Hypothesis 1**: Bitcoin price movements are positively correlated with tech stocks and macroeconomic indicators — **Confirmed**.  \n"
        "Correlation and PPS analysis support this. \n\n"

        "* **Hypothesis 2**: Features within the dataset will impact the 30 day price prediction for BitCoin. — **Confirmed**.  \n"
        "Key features selected by the model include **BitCoin's lagged price** and **Nasdaq's lagged price**.  \n"
    )