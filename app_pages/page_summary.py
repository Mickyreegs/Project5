import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* **BitCoin Close** is the daily "
        f"BitCoin price at close of business.\n"
        f"* **Nasdaq Close** is the daily Nasdaq index price "
        f"at close of business.\n"
        f"* **Gold Close** is the daily Gold price at close of business.\n "
        f"* **CPI** is the Consumer Price Index - "
        f"An indexed measure of inflation.\n "
        f"* **Ten Year Treasury Yield** is the interest rate "
        f"paid by the US government for borrowing.\n "
        f"* **Fed Funds Rate** is the Federal Reserve interest rate. "
        f"This is the interest rate at which U.S. banks lend "
        f"reserve balances to one another overnight\n "
        f"* **M2 Money Supply** is the amount of money "
        f"in circulation in the US economy.\n "
        f"* **VIX** is the CBOE Volatility Index - "
        f"A gauge of market sentiment, or *The Fear Gauge*.\n "
        f"* **Consumer Sentiment** measures how optimistic/pessimistic "
        f"consumers feel on the economy.\n "
        f"* **Real GDP** is the total value of goods & services "
        f"produced in a country.\n "
        f"* **Unemployment Rate** is the percentage of unemployed "
        f"people actively seeking work .\n "
        f"* **Retail Sales** is a measure of consumer demand.\n "
        f"* **Debt to GDP** is the ratio of a country's debt to GDP.\n\n "

        f"**Project Dataset**\n"
        f"* The dataset represents **BitCoin closing prices** "
        f"alongside market indicators (Nasdaq, Gold & Oil prices)  "
        f"as well as macroeconomic indicators "
        f"(e.g. Money Supply, Inflation, Interest Rates, "
        f"Consumer Sentiment etc.)"
        )

    # Link to README file,
    # so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]"
        f"(https://github.com/Mickyreegs/Project5/blob/main/README.md).")

    # copied from README file -
    # "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - Generate a dataset that uses only "
        f"statistically relevant features to reduce data collection "
        f"through the use of correlation analysis, "
        f"PPS, and feature importance.  "
        f"The client aims to reduce data collection costs "
        f"and improve data governance, "
        f"while also optimising model performance.\n"

        f"* 2 - The client is interested in developing a model "
        f"that predicts bitcoin price movements, "
        f"initially set at 30 days ahead, "
        f"based on macroeconomic factors, "
        f"Nasdaq movements, Oil and Gold prices.  "
        f"The client would like to support strategic decision making "
        f"for use in entry and exit points in crypto portfolios."
        )
