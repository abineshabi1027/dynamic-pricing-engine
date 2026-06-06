import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import joblib

print("Generating historical e-commerce data...")

# 1. Generate 5,000 rows of fake historical data
np.random.seed(42)
n_samples = 5000

inventory = np.random.randint(10, 500, n_samples)
competitor_price = np.random.uniform(80.0, 120.0, n_samples)
demand_score = np.random.randint(1, 11, n_samples) # Scale of 1 to 10

# Rule for optimal price: 
# Base price + premium for high demand + premium for low inventory + matching competitor
optimal_price = 100.0 + (demand_score * 2.5) - (inventory * 0.05) + (competitor_price * 0.2)

# Add some random noise to make it realistic
optimal_price += np.random.normal(0, 2, n_samples)

# Create a DataFrame
df = pd.DataFrame({
    'inventory': inventory,
    'competitor_price': competitor_price,
    'demand_score': demand_score,
    'optimal_price': optimal_price
})

# 2. Train the XGBoost Model
print("Training the XGBoost model...")
X = df[['inventory', 'competitor_price', 'demand_score']]
y = df['optimal_price']

model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X, y)

# 3. Save the trained model
joblib.dump(model, 'pricing_model.pkl')
print("Model successfully trained and saved as 'pricing_model.pkl'!")
