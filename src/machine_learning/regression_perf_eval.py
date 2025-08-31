# copied from modeling & evaluation notebook

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def regression_performance(
        features_train,
        target_train,
        features_test,
        target_test,
        model
        ):
    st.subheader("Model Evaluation Metrics")

    st.markdown("**Train Set Performance**")
    regression_evaluation(features_train, target_train, model)

    st.markdown("**Test Set Performance**")
    regression_evaluation(features_test, target_test, model)


def regression_evaluation(features, target, model):
    predictions = model.predict(features)

    st.write(f"**R² Score:** {r2_score(target, predictions):.3f}")
    st.write(
        f"**Mean Absolute Error (MAE):** "
        f"{mean_absolute_error(target, predictions):.3f}"
    )
    st.write(
        f"**Mean Squared Error (MSE):** "
        f"{mean_squared_error(target, predictions):.3f}"
    )
    st.write(
        f"**Root Mean Squared Error (RMSE):** "
        f"{np.sqrt(mean_squared_error(target, predictions)):.3f}"
    )


def regression_evaluation_plots(
        features_train,
        target_train,
        features_test,
        target_test,
        model,
        alpha_scatter=0.5
        ):
    pred_train = model.predict(features_train)
    pred_test = model.predict(features_test)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Train set plot
    sns.scatterplot(
        x=target_train.values.flatten(),
        y=pred_train.flatten(),
        alpha=alpha_scatter, ax=axes[0]
    )
    sns.lineplot(
        x=target_train.values.flatten(),
        y=target_train.values.flatten(),
        color='red', ax=axes[0]
    )
    axes[0].set_title("Train Set")
    axes[0].set_xlabel("Actual")
    axes[0].set_ylabel("Predicted")

    # Test set plot
    sns.scatterplot(
        x=target_test.values.flatten(),
        y=pred_test.flatten(),
        alpha=alpha_scatter, ax=axes[1]
    )
    sns.lineplot(
        x=target_test.values.flatten(),
        y=target_test.values.flatten(),
        color='red',
        ax=axes[1]
    )
    axes[1].set_title("Test Set")
    axes[1].set_xlabel("Actual")
    axes[1].set_ylabel("Predicted")

    plt.tight_layout()
    st.subheader("Actual vs. Predicted Scatter Plots")
    st.pyplot(fig)
