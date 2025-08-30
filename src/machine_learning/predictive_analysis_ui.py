import streamlit as st

def predict_bitcoin_price(X_live, btc_features, btc_pipeline):
    """
    Predict Bitcoin price using a trained pipeline and display results in Streamlit.
    """

    X_live_btc = X_live.filter(btc_features)

    # Make prediction
    btc_prediction = btc_pipeline.predict(X_live_btc)
    btc_prediction_proba = btc_pipeline.predict_proba(X_live_btc) if hasattr(btc_pipeline, "predict_proba") else None

    # Format prediction
    predicted_price = btc_prediction[0]
    statement = (
        f"The model forecasts the Bitcoin price 30 days ahead to be approximately "
        f"**${predicted_price:,.2f}**."
    )

    if btc_prediction_proba is not None:
        confidence = max(btc_prediction_proba[0]) * 100
        statement += f" The model's confidence in this prediction is **{confidence:.2f}%**."
        
    st.subheader("Bitcoin Price Forecast")
    st.markdown(statement)