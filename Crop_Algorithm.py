from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.get_json()

    # Convert data to DataFrame
    input_data = pd.DataFrame(data, index=[0])

    # Make prediction
    prediction = model.predict(input_data)

    # Return prediction as JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':