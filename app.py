import io
import joblib
import pandas as pd
import streamlit as st
from src.esp.train import train_and_eval
from src.esp.evaluate import plot_metrics

st.set_page_config(page_title="ESP ML App", layout="centered")

st.title("ESP Project – ML Trainer")
st.write("Upload a CSV, choose a target, pick a model, train, and download the pipeline.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Preview:", df.head())

    with st.form("train"):
        target = st.selectbox("Target column", options=df.columns)
        model_name = st.selectbox(
            "Model",
            options=["Random Forest", "SVM", "KNN", "MLP", "Logistic Regression", "Gradient Boosting"],
            index=0,
        )
        test_size = st.slider("Test size", 0.1, 0.4, 0.2, 0.05)
        submitted = st.form_submit_button("Train")
    if submitted:
        with st.spinner("Training..."):
            pipe, metrics = train_and_eval(df, target, model_name, test_size=test_size)
        st.success("Done!")

        st.subheader("Metrics")
        st.json(metrics)

        fig = plot_metrics(metrics)
        st.pyplot(fig)

        # Download trained pipeline
        buf = io.BytesIO()
        joblib.dump(pipe, buf)
        st.download_button(
            "Download trained pipeline (.joblib)",
            data=buf.getvalue(),
            file_name="esp_pipeline.joblib",
            mime="application/octet-stream",
        )
else:
    st.info("Upload a CSV file to get started.")
