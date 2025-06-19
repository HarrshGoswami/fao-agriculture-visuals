
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import joblib
import os

st.set_page_config(layout="wide")
st.title("🌾 Food Production Clustering App (FAO Dataset)")

# Upload or read data
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("FAO.csv")  # fallback for local development

st.subheader("📊 Raw Data Preview")
st.write(df.head())

# Numeric feature extraction
st.sidebar.header("Feature Engineering")
numeric_df = df.select_dtypes(include='number').dropna()

if numeric_df.empty:
    st.warning("No numeric data available for clustering.")
    st.stop()

# Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_df)

# Save scaler (optional)
joblib.dump(scaler, "scaler.pkl")

# Choose number of clusters
n_clusters = st.sidebar.slider("Select number of clusters (K)", 2, 10, 3)

# Train or load model
model_path = f"kmeans_k{n_clusters}.pkl"

if os.path.exists(model_path):
    kmeans = joblib.load(model_path)
else:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(scaled_data)
    joblib.dump(kmeans, model_path)

# Predict clusters
clusters = kmeans.predict(scaled_data)
numeric_df["Cluster"] = clusters

# PCA for 2D visualization
pca = PCA(n_components=2)
reduced = pca.fit_transform(scaled_data)
reduced_df = pd.DataFrame(reduced, columns=["PCA 1", "PCA 2"])
reduced_df["Cluster"] = clusters

# Plotting
st.subheader("📈 KMeans Cluster Visualization (2D PCA)")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=reduced_df, x="PCA 1", y="PCA 2", hue="Cluster", palette="tab10", ax=ax)
plt.title("KMeans Cluster Visualization")
st.pyplot(fig)

# Show clustered data
st.subheader("🔍 Clustered Data Sample")
st.write(numeric_df.head())

# Download clustered data
csv = numeric_df.to_csv(index=False).encode()
st.download_button("📥 Download Clustered Data", csv, "clustered_output.csv", "text/csv")

st.markdown("---")
st.markdown("✅ Built with Streamlit | Clustering with KMeans | Scaled & Visualized with PCA")
