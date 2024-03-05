from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

X = dataset[['feature1', 'feature2', ...]]  # Select the relevant features
y = dataset['target_variable']              # Select the target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Ridge(alpha=1.0)  # Create a Ridge regression model
model.fit(X_train, y_train)  # Train the model

predictions = model.predict(X_test) # make predictions

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

