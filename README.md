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
* The dataset is made up of 3 files.  2 are from Kaggle - macro_data_25yrs and nasdq - but one was downloaded from CoinCodex, from whom I sought permission to use their data and they approved.  The 3 datasets are combined based on dates linked to the economic data download.  BitCoin_Close is the target of this project.  There are various economic based columns with which to compare BitCoin's performance, from Inflation, Interest Rates, and money supply, to Nasdaq, Gold, and Oil prices.

| Variable         | Meaning                                                     | Units                                                                                |
|------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Date             | Date (YYYY-MM-DD)                                           | Date (YYYY-MM-DD)                                                                    |
| Open             | Opening Nasdaq price (Daily)                                | Price (USD)                                                                          |
| High             | Highest Nasdaq price (Daily)                                | Price (USD)                                                                          |
| Low              | Lowest Nasdaq price (Daily)                                 | Price (USD)                                                                          |
| Close            | Closing Nasdaq price (Daily)                                | Price (USD)                                                                          |
| Volume           | Number of units traded on the Nasdaq Exchange (Daily)       | Units                                                                                |
| InterestRate     | Federal Reserve interest rate                               | %                                                                                    |
| ExchangeRate     | USD Exchange Rate                                           | Currency Pair (USD/EUR)                                                              |
| VIX              | CBOE Volatility Index - A gauge of market sentiment         | Index (as %)                                                                         |
| TEDSpread        | Treasury to EUR Dollar spread - Perceived credit risk       | Basis Points (Bps)                                                                   |
| EFFR             | Effective Federal Funds Rate - Actual interest Rate         | %                                                                                    |
| Gold             | Daily price of Gold                                         | Price (USD)                                                                          |
| Oil              | Daily price of Oil                                          | Price (USD)                                                                          |
| M2_Money_Supply  | Money in circulation in the US economy                      | USD (Billions)                                                                       |
| 10YTreasuryYield | Interest rate paid by the US government pays for borrowing  | %                                                                                    |
| FedFundsRate     | Federal Reserve interest rate                               | %                                                                                    |
| CPI              | Consumer Price Index - Measure of Inflation                 | Index (as %)                                                                         |
| Inflation_Rate_% | Rate of change in CPI                                       | %                                                                                    |
| SOFR             | Secured Overnight Financing Rate - Overnight borrowing Cost | %                                                                                    |
| BitCoin_Close    | Closing BitCoin price (Daily)                               | Price (USD)                                                                          |

## Business Requirements
* The client is an investment firm who wish to use economic factors to predict the future movements/prices of BitCoin.  The business requirements are:
  * Develop a model that predicts bitcoin price movements based on macroeconomic factors, Nasdaq movements, Oil and Gold prices.  The client would like to predict BitCoin market movements for use in entry and exit points in crypto portfolios.
  * Generate a dataset that uses only relevant data to reduce data collection in the future.  Use correlation analysis, PPS, and feature importance to reduce data collection costs and improve data governance.


## Hypothesis and how to validate?

* Hypothesis 1:
  * Macroeconomic factors have influence over BitCoin price movements
    * Validation requirements:
      * Test BitCoin prices against macroeconomic factors by using Predictive Power Score (PPS)
      * Train a regression model to evaluate performance
      * Compare the trained model to a baseline model

* Hypothesis 2:
  * BitCoin prices are positively correlated to Nasdaq, Gold and Oil prices and behave similarly under various macroeconomic conditions
    * Validation requirements:
      * Use correlation analysis to assess relationships
      * Visualise trends using graphs
      * Test consistency against various macroeconomic scenarios e.g. high -v- low inflation


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


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

