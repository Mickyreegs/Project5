import plotly.graph_objects as go
from scipy.special import inv_boxcox


def plot_actual_vs_predicted_plotly(
        model,
        features,
        target,
        selected_features,
        lambda_target,
        ):

    """
    Create an interactive Plotly chart
    comparing actual vs. predicted Bitcoin prices.
    """

    preds = model.predict(features[selected_features])
    preds_bt = inv_boxcox(preds, lambda_target)
    actual_bt = inv_boxcox(target, lambda_target)

    # date was cut from the final dataset
    dates = list(range(len(target)))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=actual_bt,
        mode='lines',
        name='Actual Price',
        line=dict(color='black', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=dates,
        y=preds_bt,
        mode='lines',
        name='Ridge Regression Prediction',
        line=dict(color='blue'),
        opacity=0.7
    ))

    fig.update_layout(
        title="Bitcoin Price Prediction: Trained Model vs. Actual",
        xaxis_title="Time Index (Days)",
        yaxis_title="Bitcoin Price (USD)",
        hovermode="x unified"
    )

    return fig
