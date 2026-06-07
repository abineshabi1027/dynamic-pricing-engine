import streamlit as st
import pandas as pd
import numpy as np
import time
import joblib

st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")
st.title("⚡ Real-Time Dynamic Pricing Engine")
st.markdown("Simulating live market conditions, inventory depletion, and automatic price adjustments.")

@st.cache_resource
def load_model():
    return joblib.load('pricing_model.pkl')

model = load_model()

st.subheader("Live Metrics")
col1, col2, col3, col4 = st.columns(4)
metric_price = col1.empty()
metric_inventory = col2.empty()
metric_competitor = col3.empty()
metric_demand = col4.empty()

st.subheader("Live Pricing vs Competitor Pricing")
chart_container = st.empty()

inventory = 500
competitor_price = 100.0
history = []

st.toast("Starting real-time data stream...")

for i in range(200):
   
    inventory -= np.random.randint(0, 8)
    if inventory <= 20: 
        inventory = 500 
    
    competitor_price += np.random.uniform(-1.5, 1.5) 
    demand_score = np.random.randint(3, 10)

    live_features = pd.DataFrame([[inventory, competitor_price, demand_score]], 
                                 columns=['inventory', 'competitor_price', 'demand_score'])
    
    predicted_price = model.predict(live_features)[0]

    metric_price.metric("Our Optimal Price", f"${predicted_price:.2f}")
    metric_inventory.metric("Current Inventory", f"{inventory} units")
    metric_competitor.metric("Competitor Price", f"${competitor_price:.2f}")
    metric_demand.metric("Live Demand Score", f"{demand_score} / 10")

    history.append({
        'Time': pd.Timestamp.now(), 
        'Our Predicted Price': predicted_price, 
        'Competitor Price': competitor_price
    })
    if len(history) > 40: 
        history.pop(0) 
    
    df_chart = pd.DataFrame(history).set_index('Time')
    chart_container.line_chart(df_chart, color=["#FF4B4B", "#0068C9"])

    time.sleep(1.5)

st.success("Simulation complete. Refresh the page to restart the data stream.")
