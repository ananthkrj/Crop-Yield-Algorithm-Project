import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
from pandas_dataset import temperature_df, humidity_df, rainfall_df, past_crop_yield_df, CropAnd_WaterProjections_df, soil_characteristics_df

# Add a 'crop' column to each DataFrame
temperature_df['crop'] = 'All'
humidity_df['crop'] = 'All'
rainfall_df['crop'] = 'All'
past_crop_yield_df['crop'] = past_crop_yield_df['Crop']
CropAnd_WaterProjections_df['crop'] = CropAnd_WaterProjections_df['Crop']
soil_characteristics_df['crop'] = 'All'

# Merge the DataFrames based on the 'crop' column
merged_df = pd.merge(temperature_df, humidity_df, on='crop')
merged_df = pd.merge(merged_df, rainfall_df, on='crop')
merged_df = pd.merge(merged_df, past_crop_yield_df, on='crop', how='left')
merged_df = pd.merge(merged_df, CropAnd_WaterProjections_df, on='crop', how='left')
merged_df = pd.merge(merged_df, soil_characteristics_df, on='crop', how='left')

# Handle missing values in the target variable
merged_df = merged_df.dropna(subset=['Total'])  # Remove rows with missing values
# merged_df['Total'] = merged_df['Total'].fillna(0)  # Impute missing values with 0

# Print the number of rows before and after dropping rows (optional for checking)
print(f"Number of rows before dropping missing values: {merged_df.shape[0]}")
merged_df = merged_df.dropna(subset=['Total'])
print(f"Number of rows after dropping missing values: {merged_df.shape[0]}")

# If you decide to impute missing values instead of dropping rows
# merged_df['Total'] = merged_df['Total'].fillna(merged_df['Total'].mean())

# Select relevant features and target variable
X = merged_df[['avg_high', 'avg_low', 'rainfall_inches', 'humidity_level', 'pH']]
y = merged_df['Total']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the random forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model.pkl')

# Make predictions
predictions = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")