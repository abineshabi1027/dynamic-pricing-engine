import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import joblib

print("Generating historical e-commerce data...")

np.random.seed(42)
n_samples = 5000

inventory = np.random.randint(10, 500, n_samples)
competitor_price = np.random.uniform(80.0, 120.0, n_samples)
demand_score = np.random.randint(1, 11, n_samples)

optimal_price = 100.0 + (demand_score * 2.5) - (inventory * 0.05) + (competitor_price * 0.2)

optimal_price += np.random.normal(0, 2, n_samples)

df = pd.DataFrame({
    'inventory': inventory,
    'competitor_price': competitor_price,
    'demand_score': demand_score,
    'optimal_price': optimal_price
})

print("Training the XGBoost model...")
X = df[['inventory', 'competitor_price', 'demand_score']]
y = df['optimal_price']

model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X, y)

joblib.dump(model, 'pricing_model.pkl')
print("Model successfully trained and saved as 'pricing_model.pkl'!")
