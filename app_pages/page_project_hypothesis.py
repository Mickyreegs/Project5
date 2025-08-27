import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from notebooks 2, 3, & 4.
    st.success(
        "* **Hypothesis 1**: Bitcoin price movements are positively correlated with tech stocks and macroeconomic indicators — **Confirmed**.  \n"
        "Correlation and PPS analysis support this. \n\n"

        "* **Hypothesis 2**: Macroeconomic factors influence Bitcoin’s 30-day forward price — **Confirmed**.  \n"
        "Key features selected by the model include **M2 Money Supply** and **Bitcoin Close**.  \n"
        "Additional influential variables identified during feature importance analysis include **Nasdaq Close** and **CPI**."
    )