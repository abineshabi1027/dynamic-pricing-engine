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


## 🏃‍♂️ Running the Project

## Step 1: Train the Model Run the training script to generate the historical data and build the XGBoost model. This will output a pricing_model.pkl file.

## Bash
python train_model.py

## Step 2: Launch the Dashboard Start the Streamlit application to view the live dynamic pricing simulation in your browser.

## Bash
streamlit run app.py
