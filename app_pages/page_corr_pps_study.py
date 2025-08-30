import streamlit as st

def page_corr_pps_study_body():
    st.title("Correlation and PPS Analysis")

    st.markdown("""
    This section explores how various features relate to Bitcoin price using:
    - **Spearman Correlation**: tells us the monotonic relationship between features i.e. as one increases, the other increases or decreases, but not necessarily at the same rate.
    - **Pearson Correlation**: Measures linear relationships
    - **Predictive Power Score (PPS)**: Detects predictive strength, even for non-linear patterns
    """)

    st.write("---")

    # Spearman Correlation
    st.subheader("Spearman Correlation")
    st.image("outputs/datasets/figs/spearman.png", caption="Spearman Correlation Heatmap")
    st.markdown("""
    Spearman correlation is ideal for identifying monotonic trends. 
    It shows strong associations between Bitcoin price and macro indicators like Nasdaq and CPI.
    """)

    st.write("---")

    # Pearson Correlation
    st.subheader("Pearson Correlation")
    st.image("outputs/datasets/figs/pearson.png", caption="Pearson Correlation Heatmap")
    st.markdown("""
    Pearson correlation highlights linear relationships. 
    While some features show strong linear ties to Bitcoin price, others may be better captured by non-linear models.
    """)

    st.write("---")

    # Predictive Power Score (PPS)
    st.subheader("Predictive Power Score (PPS)")
    st.image("outputs/datasets/figs/pps.png", caption="PPS Heatmap")
    st.markdown("""
    PPS reveals predictive strength regardless of linearity. 
    It helps identify features that may not correlate strongly but still carry predictive value.
    """)

    # Signal Scores
    st.subheader("Filtered Features with Strong Predictive Signal")
    st.markdown("""
    These features have high scores across all three metrics — PPS, Pearson, and Spearman.
    We will take the top 5 for modeling purposes.
    """)

    st.dataframe(filtered_features.style.format({"Signal": "{:.3f}", "PPS": "{:.3f}", "Pearson": "{:.3f}", "Spearman": "{:.3f}"}))


    st.write("---")
    st.markdown("Use this analysis to understand which features are most influential in forecasting Bitcoin price.")

