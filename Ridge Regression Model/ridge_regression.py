import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Load the CSV files
temperature_df = pd.read_csv('temperature_data.csv')
humidity_df = pd.read_csv('humidity_data.csv')
rainfall_df = pd.read_csv('rainfall_data.csv')
growing_season_df = pd.read_csv('growing_season_data.csv')

# Merge the dataframes if needed
# For example, if you want to combine temperature, humidity, and rainfall data
data = pd.merge(temperature_df, humidity_df, on='month')
data = pd.merge(data, rainfall_df, on='month')

# Select the relevant features and target variable
X = data[['avg_high', 'avg_low', 'humidity_level', 'rainfall_inches']]
y = data['target_variable']  # Replace 'target_variable' with your actual target column

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
