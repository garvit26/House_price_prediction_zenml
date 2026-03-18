
# 🏡 House Price Prediction: End-to-End MLOps Pipeline

This project demonstrates a production-ready **MLOps framework** for predicting house prices using the Ames Housing Dataset. It features a complete **CI/CD pipeline** for machine learning, from data ingestion to real-time model serving.

## 🚀 Project Overview
The goal of this project was to move beyond a simple Jupyter notebook and build a scalable system that automates the machine learning lifecycle.

* **Pipeline Orchestration:** ZenML
* **Experiment Tracking & Model Registry:** MLflow
* **Deployment & Inference:** MLflow Models Serve
* **User Interface:** Streamlit (Web App)

---

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Libraries:** Scikit-learn, Pandas, NumPy
* **MLOps:** ZenML, MLflow
* **Frontend:** Streamlit
* **Version Control:** Git & GitHub

---

## ⚙️ Features
* **Automated CI/CD Pipeline:** Uses ZenML to handle data cleaning, feature engineering, and model training in a reproducible workflow.
* **Model Management:** Integrated MLflow for tracking parameters, metrics, and versioning model artifacts.
* **Real-time Inference:** A REST API endpoint created via MLflow to serve predictions to external applications.
* **Interactive UI:** A custom-built Streamlit dashboard allowing users to input house features and receive instant valuations.

---

## 🏃‍♂️ How to Run

### 1. Clone the Repository
```bash
git clone [https://github.com/garvit26/House_price_prediction_zenml.git](https://github.com/garvit26/House_price_prediction_zenml.git)
cd House_price_prediction_zenml
