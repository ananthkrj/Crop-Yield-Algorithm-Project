from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import Ridge
import numpy as np

# Load the trained model and other necessary data
ridge_model = Ridge(alpha=1.0)  # Load your trained Ridge regression model here
# Load other necessary data such as temperature, humidity, etc.

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Crop Yield Prediction Algorithm!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Assume data contains the features required for prediction (temperature, humidity, etc.)
    # Preprocess the data if necessary
    # Make predictions using the trained model
    # Return the prediction as a JSON response
    prediction = ridge_model.predict(np.array(data).reshape(1, -1))
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
