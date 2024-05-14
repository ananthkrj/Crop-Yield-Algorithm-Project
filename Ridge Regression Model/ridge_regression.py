import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
from pandas_dataset import temperature_data, humidity_data, rainfall_data, growing_season_data
from pandas_dataset import (past_crop_yield21, past_crop_yield22, CropAnd_WaterProjections,
                            soil_characteristics,)

# Load the DataFrames from pandas_dataset.py
temperature_df = pd.DataFrame(temperature_data)
humidity_df = pd.DataFrame(humidity_data)
rainfall_df = pd.DataFrame(rainfall_data)
growing_season_df = pd.DataFrame(growing_season_data)

# Merge temperature, humidity, and rainfall data
data = pd.merge(temperature_df, humidity_df, on='month')
data = pd.merge(data, rainfall_df, on='month')

# Concatenate past crop yield data
past_crop_yield = pd.concat([past_crop_yield21, past_crop_yield22], ignore_index=True)
data = pd.merge(data, past_crop_yield[['Crop']], on='Crop')

# Merge Additional data (excluding AgCensus_FarmSizes)
data = pd.merge(data, CropAnd_WaterProjections, on='Crop')
data = pd.merge(data, soil_characteristics, on='Soil Horizons')

# Merge the past crop yield data with the combined DataFrame
data = pd.merge(data, past_crop_yield[['Crop', 'Year', 'Total']], on='Crop')

# Select relevant features and target variable
X = data[['avg_high', 'avg_low', 'humidity_level', 'rainfall_inches', 'soil_type']]
y = data['Total']  # Assuming 'Total' is the target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model.pkl')

# Make predictions
predictions = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
