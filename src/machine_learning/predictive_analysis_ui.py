import streamlit as st
from scipy.special import inv_boxcox
import plotly.graph_objects as go
import numpy as np


def predict_bitcoin_price(
        X_live,
        btc_features,
        btc_pipeline,
        boxcox_lambdas,
        residual_std=0.79,
        reference_date=None
        ):
    """
    Predict Bitcoin price using a trained pipeline
    and display results in Streamlit.
    Applies inverse Box-Cox transformation
    and includes confidence band.
    Plot the results on a Plotly chart.
    """

    # in the event of infinites or NaNs
    if not np.isfinite(X_live.values).all():
        st.warning(
            "Your input data contains NaNs or infinite values. Cleaning now..."
        )

    # Replace inf/-inf with NaN
    X_live.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Fill NaNs with median or zero (you can customize this)
    X_live.fillna(X_live.median(), inplace=True)

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
        f"The model forecasts the Bitcoin price 30 days ahead "
        f"to be approximately "
        f"**${predicted_price:,.2f}**.\n\n"
        f"Expected range: **\\${lower:,.2f} - \\${upper:,.2f}**."
    )

    # model confidence
    btc_prediction_proba = (
        btc_pipeline.predict_proba(X_live_btc)
        if hasattr(btc_pipeline, "predict_proba")
        else None
    )
    if btc_prediction_proba is not None:
        confidence = max(btc_prediction_proba[0]) * 100
        statement += f"\n\nModel confidence: **{confidence:.2f}%**."

    # reference date
    if reference_date is not None:
        statement += f"\n\nUsing economic indicators from "
        f"**{reference_date.strftime('%B %d, %Y')}**."

    # Display in Streamlit
    st.subheader("Bitcoin Price Forecast")
    st.success(statement)

    # Display out result on a graph for the user
    fig = go.Figure()

    # Predicted price
    fig.add_trace(go.Scatter(
        x=[0],
        y=[predicted_price],
        mode='markers',
        name='Predicted Price',
        marker=dict(color='blue', size=10),
        hovertext=[f"Predicted: ${predicted_price:,.2f}"],
        hoverinfo="text"
    ))

    # Lower range
    fig.add_trace(go.Scatter(
        x=[-0.2],
        y=[lower],
        mode='markers',
        name='Lower Range',
        marker=dict(color='green', size=8),
        hovertext=[f"Lower Range: ${lower:,.2f}"],
        hoverinfo="text"
    ))

    # Upper range
    fig.add_trace(go.Scatter(
        x=[0.2],
        y=[upper],
        mode='markers',
        name='Upper Range',
        marker=dict(color='red', size=8),
        hovertext=[f"Upper Range: ${upper:,.2f}"],
        hoverinfo="text"
    ))

    # Layout
    fig.update_layout(
        title="Bitcoin Price Forecast (30 Days Ahead)",
        yaxis_title="Price (USD)",
        xaxis=dict(showticklabels=False, range=[-0.5, 0.5]),
        hovermode="closest",
        showlegend=True
    )

    st.caption("Hover over points to view results.")

    st.plotly_chart(fig, use_container_width=True)
