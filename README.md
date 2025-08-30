# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the bring your own data project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. In your newly created repo click on the green Code button.

1. Then, from the Codespaces tab, click Create codespace on main.

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.12.1 as it inherits from the workspace, so it will be Python-3.12.1 as installed by Codespaces. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

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

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

* Thank the people who provided support through this project.