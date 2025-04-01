# app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
df = pd.read_csv("phishing_dataset.csv")
X = df.drop(['url', 'status'], axis=1)
y = df['status'].map({'phishing': 1, 'legitimate': 0})

# Preprocess
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# UI
st.title("🔐 AI Phishing URL Detector")
st.write("Upload a CSV file with URL data to detect phishing threats.")

uploaded_file = st.file_uploader("Choose a file", type="csv")
st.write("App is running... waiting for file input.")

if uploaded_file is not None:
    try:
        test_df = pd.read_csv(uploaded_file)
        test_features = test_df.drop(['url'], axis=1)
        test_scaled = scaler.transform(test_features)
        predictions = model.predict(test_scaled)

        test_df['Prediction'] = predictions
        test_df['Prediction'] = test_df['Prediction'].map({1: 'Phishing', 0: 'Legitimate'})

        st.success("✅ Prediction complete!")
        st.write(test_df[['url', 'Prediction']])
        st.download_button("Download Results", test_df.to_csv(index=False), file_name='results.csv')

    except Exception as e:
        st.error(f"⚠️ Something went wrong:\n\n{e}")

