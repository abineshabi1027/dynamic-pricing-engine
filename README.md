# dynamic-pricing-engine
A collection of projects, assignments, and practical implementations completed during my data science and analytical  I
# ⚡ Real-Time Dynamic Pricing Engine

A machine learning-powered Streamlit dashboard that simulates real-time dynamic product pricing based on live inventory levels, competitor pricing, and market demand fluctuations. 

This project demonstrates the end-to-end lifecycle of a machine learning model, from synthetic data generation and training to deployment in a "live" streaming environment.

## 🚀 Features
* **Synthetic Data Generation:** Automatically generates a realistic e-commerce dataset incorporating demand elasticity and inventory scarcity rules.
* **Predictive Modeling:** Uses an **XGBoost Regressor** to predict the optimal price point to maximize profit margins.
* **Real-Time Simulation Loop:** Mimics live market data feeds (dropping inventory, fluctuating competitor prices) without the overhead of complex messaging queues like Kafka.
* **Live Interactive UI:** A Streamlit dashboard that updates metrics and visualizes pricing trends over time using auto-refreshing line charts.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** XGBoost, Scikit-Learn, Joblib
* **Data Manipulation:** Pandas, NumPy
* **Frontend/Deployment:** Streamlit

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone [https://github.com/vibhakar2007/dynamic-pricing-engine.git](https://github.com/vibhakar2007/dynamic-pricing-engine.git)
cd dynamic-pricing-engine
