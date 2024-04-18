import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
from pandas_dataset import temperature_data, humidity_data, rainfall_data, growing_season_data
from pandas_dataset import past_crop_yield21, past_crop_yield22, farm_sizes, soil_data

# Load the DataFrames from pandas_dataset.py
temperature_df = pd.DataFrame(temperature_data)
humidity_df = pd.DataFrame(humidity_data)
rainfall_df = pd.DataFrame(rainfall_data)
growing_season_df = pd.DataFrame(growing_season_data)

# Merge the dataframes if needed
data = pd.merge(temperature_df, humidity_df, on='month')
data = pd.merge(data, rainfall_df, on='month')

# Load additional CSV files
past_crop_yield21 = pd.read_csv('past_crop_yield21_data.csv')
past_crop_yield22 = pd.read_csv('past_crop_yield22_data.csv')
farm_sizes = pd.read_csv('farm_sizes_data.csv')
soil_data = pd.read_csv('soil_characteristics_data.csv')

# Merge or concatenate additional data as needed
# For example, if you want to include past crop yield data
data = pd.concat([data, past_crop_yield21, past_crop_yield22], ignore_index=True)


# Select the relevant features and target variable
X = data[['avg_high', 'avg_low', 'humidity_level', 'rainfall_inches']]
y = data['target_variable']  # Replace 'target_variable' with your actual target column

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