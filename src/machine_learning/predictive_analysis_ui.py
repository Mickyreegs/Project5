import streamlit as st
from scipy.special import inv_boxcox
import matplotlib.pyplot as plt

def predict_bitcoin_price(X_live, btc_features, btc_pipeline, boxcox_lambdas, residual_std=0.79, reference_date=None):
    """
    Predict Bitcoin price using a trained pipeline and display results in Streamlit.
    Applies inverse Box-Cox transformation and includes confidence band.
    """

    # Filter features
    X_live_btc = X_live.filter(btc_features)

    # Make prediction
    btc_prediction = btc_pipeline.predict(X_live_btc)
    predicted_transformed = btc_prediction[0]

    # Get lambda for inverse Box-Cox
    lambda_btc = boxcox_lambdas.get("Bitcoin_Close", 0)

    # Inverse transform prediction and confidence band
    predicted_price = inv_boxcox(predicted_transformed, lambda_btc)
    lower = inv_boxcox(predicted_transformed - residual_std, lambda_btc)
    upper = inv_boxcox(predicted_transformed + residual_std, lambda_btc)

    # Build statement
    statement = (
        f"The model forecasts the Bitcoin price 30 days ahead to be approximately "
        f"**${predicted_price:,.2f}**.\n\n"
        f"Expected range: **\\${lower:,.2f} - \\${upper:,.2f}**."
    )

    # model confidence
    btc_prediction_proba = btc_pipeline.predict_proba(X_live_btc) if hasattr(btc_pipeline, "predict_proba") else None
    if btc_prediction_proba is not None:
        confidence = max(btc_prediction_proba[0]) * 100
        statement += f"\n\nModel confidence: **{confidence:.2f}%**."

    # reference date
    if reference_date is not None:
        statement += f"\n\nUsing economic indicators from **{reference_date.strftime('%B %d, %Y')}**."

    # Display in Streamlit
    st.subheader("Bitcoin Price Forecast")
    st.success(statement)

    # Prediction plot and confidence band
    fig, ax = plt.subplots()
    ax.plot([0], [predicted_price], marker='o', label='Predicted Price', color='blue')
    ax.errorbar([0], [predicted_price], yerr=[[predicted_price - lower], [upper - predicted_price]], fmt='o', color='blue', capsize=10)
    ax.set_title("Bitcoin Price Forecast (30 Days Ahead)")
    ax.set_ylabel("Price (USD)")
    ax.set_xticks([])
    ax.legend()
    st.pyplot(fig)
