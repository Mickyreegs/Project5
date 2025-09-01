# BitCoin 30-Day Forecaster

Welcome to the BitCoin 30 Day Forecaster, which aims to predict the price trend of BitCoin in 30 days based on macroeconomic and market factors.

## Dataset Content

* The dataset is made up of 3 files.  
  * BitCoin prices since inception downloaded from CoinCodex, from whom I sought permission to use their data and they approved.
    * The gentleman's name is Leo Daris, and he's a content manager at CoinCodex
  * Nasdaq, Gold and Oil prices downloaded from Yahoo Finance (yfinance) in Pyhon
  * Macroeconomic features downloaded from FRED through their API
* The 3 datasets are combined based on dates linked to the BitCoin data download.  BitCoin_Close is the target of this project.  There are various economic based columns with which to compare BitCoin's performance, from Inflation, Interest Rates, and money supply, to Nasdaq, Gold, and Oil prices.

| Variable          | Meaning                                                     | Units                                                                                |
|-------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Date              | Date (YYYY-MM-DD)                                           | Date (YYYY-MM-DD)                                                                    |
| BitCoin_Close     | Closing BitCoin price (Daily)                               | Price (USD)                                                                          |
| Nasdaq_Close      | Closing Nasdaq price (Daily)                                | Price (USD)                                                                          |
| Gold_Close        | Daily price of Gold                                         | Price (USD)                                                                          |
| Brent_Close       | Daily price of Oil                                          | Price (USD)                                                                          |
| CPI               | Consumer Price Index - Measure of Inflation                 | Index Value                                                                          |
| Ten_Year_Yield    | Interest rate paid by the US government for borrowing       | %                                                                                    |
| Fed_Funds_Rate    | Federal Reserve interest rate                               | %                                                                                    |
| M2_Money_Supply   | Money in circulation in the US economy                      | Currency (Billions)                                                                  |
| VIX               | CBOE Volatility Index - A gauge of market sentiment         | Percentage Points                                                                    |
| Consumer_Sentiment| How optimistic/pessimistic consumers feel on the economy    | Index Score                                                                          |
| Real_GDP          | Total value of goods & services produced in a country       | Currency (Billions)                                                                  |
| Unemployment_Rate | % of unemployed people actively seeking work                | %                                                                                    |
| Retail_Sales      | A measure of consumer demand                                | Currency (Billions)                                                                  |
| Debt_to_GDP       | Ratio of country's debt to GDP                              | %                                                                                    |

## Business Requirements

### Client Profile

The client is an investment firm who wish to review and anticipate the future movements/prices of BitCoin.  

The business requirements are:

* Generate a dataset that uses only statistically relevant features to reduce data collection through the use of correlation analysis, PPS, and feature importance.  Their aim is to reduce data collection costs and improve data governance, while also optimising model performance.

* Develop a model that predicts bitcoin price movements, initially set at 30 days ahead, based on macroeconomic factors, Nasdaq movements, Oil and Gold prices.  The client would like to support strategic decision making for use in entry and exit points in crypto portfolios.

## Hypothesis and how to validate?

* Hypothesis 1:
  * BitCoin price movements are positively correlated to tech stocks and various macroeconomic factors.
    * Validation requirements:
      * Perform correlation and PPS analysis to assess BitCoin's relationships to Nasdaq, Gold, Oil and a selection of macroeconomic factors
      * Visualise trends
      * Evaluate feature importance to highlight the best predictors for the model

* Hypothesis 2:
  * Features within the dataset will impact the 30 day price prediction for BitCoin.
    * Validation requirements:
      * Train multiple models using the features with the highest signals to find the best model for this task
      * Compare models using R2 - Those over 0.80 will be acceptable given BitCoin's price volatility
      * Validate predictions against the actual BitCoin prices

## The rationale to map the business requirements to the Data Visualizations and ML tasks

* Business Requirement 1 - Feature Relavance and Data Efficiency
  * We will analyse the BitCoin prices since inception
  * We will conduct a correlation study and PPS review to better understand BitCoin's linear and non-linear relationships to market and macroeconomic indicators
  * We will plot the best features against BitCoin to support interpretability and feature selection

* Business Requirement 2 - Predicitive Modeling for Strategic Forecasting
  * We want to predict BitCoin movements, not exact price, 30 days ahead by using market and macroeconomic features
  * We want to build and train a regression model and optimise performace by leveraging the best features from requirement 1
  * We want to compare train and test sets and achieve an R2 of 0.80 or more

## ML Business Case

### Client Problem

* Our client, an investment firm, currently lacks a viable method to predict BitCoin price movements using market and marcoeconomic data.
* They've advised that their current methods are far too reactive in nature and limit their abilities to make crucial decisions at the right time.

### Client Opportunity

* BitCoin's price is increasingly influenced by macroeconomic trends: inflation, money supply, the tech sector.
* We felt that a focussed review of a select few features, both market and macroeconomic based, can highlight which of those features has a greater impact on BitCoin prices.
* We can assist the client in gaining predictive insights to support their strategic decisions within their crypto portfolios

### Machine Learning Solution

* We will develop a regression model capable to predicting BitCoin price movements 30 days ahead.  The prices will not be exact, but they will assist in the decision making process of the firm.
* We require an R2 score of at least 0.80 in order to progress with the model.
* Inputs are be market based (Nasdaq, Gold, Oil) and macroeconomic (CPI, Money Supply, GDP, Consumer Sentiment etc.)
* Feature selection techniques will be used to highlight impactful inputs and reduce data collection costs.  It will also improve model performance and interpretability.
* The model will be considered a failure if after 1 year the average R2 score on test data falls below 0.80 or the RMSE exceeds $20,000.

### Business Impact

* The model will enable better crypto portfolio management
* The model will reduce data collection costs for the firm
* The model will support strategic decision-making with real time forecasts

## Dashboard Design (Streamlit App User Interface)

### Page 1 - Quick Project Summary

* Here, we listed the following:
  * Jargon terms and explanations for the user
  * A quick overview of the dataset being used
  * The client business requirements

### Page 2 - Project Hypothesis

* Here, we list our 2 hypotheses and the confirmation as to whether the requirements were met or not

### Page 3 - Correlation & PPS study

* Here, we give the details of the following tests:
  * Spearman Correlation - Heatmap displayed with detailing features above a threshold of 0.60
  * Pearson Correlation - Heatmap displayed with detailing features above a threshold of 0.60
  * Predictive Power Score (PPS) - Heatmap displayed with detailing features above a threshold of 0.60

* From these tests, we determine the features to be used for modeling

### Page 4 - ML Training Overview

* Here, we described the steps involved in model selection and training, including:
  * Feature Selection
  * BitCoin history and distribution
  * Trandformed features
  * Key predictors
  * Evaluation metrics
  * Actual -v- Model prediction comparison
  * Summary

### Page 5 - Prediction Page

* This is where we will make predictions on the price trend of BitCoin in 30 days time
* The only user input will be the BitCoin price.  Users are encouraged to take this from [Coin Codex](https://coincodex.com/crypto/bitcoin/)
* Macroeconomic features will be auto-filled using the FRED API - [FRED](https://fred.stlouisfed.org)
* Nasdaq indices will be pulled from Yahoo Finance using Python's yfinance library
* This will enhance user experience, especially for those not experienced in the macroeconomic values

## Unfixed Bugs

* There are no known bugs at present.

## Deployment

### Heroku

* The live app can be found here: [BitCoin 30-Day Forecaster](https://bitcoin-30day-forecast-8d17d38cb841.herokuapp.com/)
* The runtime.txt Python version was set to Python 3.12.1
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Search for the repository name, and once it is found, click Connect.
4. Review the requirements.txt, runtime.txt and slugignore files:
   - Make sure all requirements are included and remove the redundant ones irrelevant for deployment
   - Make sure you include the correct version of Python in runtime.txt
   - You can add large files to be ignored for deployment in the slugignore file.  We chose pycache and jupyter notebooks
5. Ensure your Procfile is updated with web: sh setup.sh && streamlit run app.py
6. Be sure to have your setup.sh file ready.  This is for Streamlit
7. In the event you've hidden any API keys in a .env and applied in gitignore:
   - Ensure python-dotenv is included in your requirements.txt file
   - Go to Settings in Heroku, click Add Config Var, then insert the API Key Name and API key number and hit save.  This will ensure API calls are made seemlessly in Heroku
8. Prior to clicking deploy, make sure the branch is set to Main
9. The deployment process should happen smoothly if all deployment files are fully functional
10. You can now open the app from the button in the top right corner of Heroku

## Main Data Analysis and Machine Learning Libraries

| Library           | Use case                                                                                                                                     |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Pandas            | Used in the data cleaning and transformation processes                                                                                       |
| Numpy             | Used in numerical calculations and arrays                                                                                                    |
| Scikit-Learn      | Use to test and train regression models, evaluate performance and build pipelines                                                            |
| XG Boost          | Used for Gradient Boosting regression                                                                                                        |
| Matplotlib        | Used for generating plots                                                                                                                    |
| Plotly            | Used for generating interactive plots                                                                                                        |
| Streamlit         | Interactive dashboard for use in displaying outputs, running the final pipeline, rendering widgets, and deployment to Heroku                 |
| yfinance          | Fetches Nasdaq, Oil and Gold price information                                                                                               |
| FRED API          | Retrieves values for macroeconomic dataset and inputs from FRED website                                                                      |

## Credits

### Content

* [Code Institute Malaria Detector Walkthrough Project](https://github.com/Code-Institute-Solutions/WalkthroughProject01)
* [Code Institute Churnometer Walkthrough Project](https://github.com/Code-Institute-Solutions/churnometer)
  * Chunks of code were applied to the BitCoin project from the Churnometer - Specifically regression code and transformers
* [FRED](https://fred.stlouisfed.org)
  * Data obtained via API
* [Coin Codex](https://coincodex.com/crypto/bitcoin/)
  * Approval requested and approved by Leo Daris - Content Manager at Coin Codex
* Yahoo Finance via yfinance Python Library
* Code Institute - Data Analysis and Machine Learning Toolkit Module
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [python.org](https://docs.python.org/3/)
* [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)
* [Plotly](https://plotly.com/python/financial-charts/)
* [Scikit-Learn](https://scikit-learn.org/stable/user_guide.html)
* [Numpy](https://numpy.org/doc/stable/)
* [Streamlit](https://docs.streamlit.io/develop/api-reference)
* [W3 Schools](https://www.w3schools.com/)

## Acknowledgements (optional)

* A big thank you to the Code Institute for delivering a course relevant to miltiple industries, and providing the tools required to progress in the realm of Data Science and Machine Learning.  I would recommend this course to anyone.
