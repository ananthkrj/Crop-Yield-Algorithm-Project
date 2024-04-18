from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# load csv files
ag_census_data = pd.read_csv('AgCensus_FarmSizes_data.csv')
basin_wide_data = pd.read_csv('BasinWide_FarmSizes_data.csv')
past_yield_21_data = pd.read_csv('past_crop_yield21_data.csv')
past_yield_22_data = pd.read_csv('past_crop_yield22_data.csv')
soil_data = pd.read_csv('soil_characteristics_data.csv')
valley_wide_data = pd.read_csv('ValleyWide_FarmSizes_data.csv')
@app.route('/')
def index():
    return render_template('index/.html')

def extract_keyword(user_input):
    user_input = user_input.lower()

    # Defines list of keywords
    keywords = [
        'pistachios',
        'walnuts',
        'year',
        'water use',
        'profit',
        'almond hulls',
        'almond meats',
        'almond shells',
        'financial values',
        'crop comparison',
        'weather impact',
    ]

    for keyword in keywords:
        if keyword in user_input:
            return keyword

    return None

# Dictionary mapping keywords to prediction functions
prediction_functions = {
    'pistachios': predict_pistachios,
    'walnuts': predict_walnuts,
    'year': predict_year,
    'water use': predict_wateruse,
    'profit': predict_profit,
    'almond hulls': predict_hulls,
    'almond meats': predict_meats,
    'almond shells': predict_shells,
    'financial values': financial_values,
    'crop comparison': crop_comparison,
    'weather impact': weather_impact,
}

def predict_pistachios(user_input):# Extract relevant information from user_input
    # Filter the crop data for pistachios
    pistachio_data = crop_data[crop_data['Crop'] == 'Pistachios']

    # Extract relevant information from user_input
    Bearing_Acreage = user_input.get('Bearing Acreage')
    Per_Acre = user_input.get('Growth per Acre')
    total = user_input.get('Total in quantity')
    unit = user_input.get('Weight')

    if 'Bearing Acreage' in user_input:
        # Make predictions related to price per unit
        prediction_type = 'Bearing Acreage'
        prediction = model.predict([[price_per_unit]])
        return formatted_response
    elif 'Growth Per Acre' in user_input:# Make predictions related to price per unit
        prediction_type = 'Growth per Acre'
        prediction = model.predict([[subtotal]])
    elif 'Total in quantity' in user_input:
        prediction_type = 'Total in quantity'
        prediction = model.predict([[total]])
    elif 'Weight' in user_input:
        prediction_type = 'Weight'
        prediction = model.predict([[total]])
    else:
        prediction_type = "Could not find Relevant info, try again later."

    formatted_response = f"The predicted {prediction_type} is: {prediction[0]}"
    return formatted_response

def predict_walnuts(user_input):
    # Filter the crop data for walnuts
    pistachio_data = crop_data[crop_data['Crop'] == 'Walnuts']

    # Extract relevant information from user_input
    Bearing_Acreage = user_input.get('Bearing Acreage')
    Per_Acre = user_input.get('Growth per Acre')
    total = user_input.get('Total in quantity')
    unit = user_input.get('Weight')

    if 'Bearing Acreage' in user_input:
        # Make predictions related to price per unit
        prediction_type = 'Bearing Acreage'
        prediction = model.predict([[price_per_unit]])
        return formatted_response
    elif 'Growth Per Acre' in user_input:  # Make predictions related to price per unit
        prediction_type = 'Growth per Acre'
        prediction = model.predict([[subtotal]])
    elif 'Total in quantity' in user_input:
        prediction_type = 'Total in quantity'
        prediction = model.predict([[total]])
    elif 'Weight' in user_input:
        prediction_type = 'Weight'
        prediction = model.predict([[total]])
    else:
        prediction_type = "Could not find Relevant info, try again later."

    formatted_response = f"The predicted {prediction_type} is: {prediction[0]}"
    return formatted_response

def predict_meats(user_input):
    # Filter the crop data for Almond Meats
    pistachio_data = crop_data[crop_data['Crop'] == 'Almond Meats']

    # Extract relevant information from user_input
    Bearing_Acreage = user_input.get('Bearing Acreage')
    Per_Acre = user_input.get('Growth per Acre')
    total = user_input.get('Total in quantity')
    unit = user_input.get('Weight')

    if 'Bearing Acreage' in user_input:
        # Make predictions related to price per unit
        prediction_type = 'Bearing Acreage'
        prediction = model.predict([[price_per_unit]])
        return formatted_response
    elif 'Growth Per Acre' in user_input:  # Make predictions related to price per unit
        prediction_type = 'Growth per Acre'
        prediction = model.predict([[subtotal]])
    elif 'Total in quantity' in user_input:
        prediction_type = 'Total in quantity'
        prediction = model.predict([[total]])
    elif 'Weight' in user_input:
        prediction_type = 'Weight'
        prediction = model.predict([[total]])
    else:
        prediction_type = "Could not find Relevant info, try again later."

    formatted_response = f"The predicted {prediction_type} is: {prediction[0]}"
    return formatted_response

def predict_hulls(user_input):
    # Filter the crop data for pistachios
    pistachio_data = crop_data[crop_data['Crop'] == 'Almond Hulls']

    # Extract relevant information from user_input
    Bearing_Acreage = user_input.get('Bearing Acreage')
    Per_Acre = user_input.get('Growth per Acre')
    total = user_input.get('Total in quantity')
    unit = user_input.get('Weight')

    if 'Bearing Acreage' in user_input:
        # Make predictions related to price per unit
        prediction_type = 'Bearing Acreage'
        prediction = model.predict([[price_per_unit]])
        return formatted_response
    elif 'Growth Per Acre' in user_input:  # Make predictions related to price per unit
        prediction_type = 'Growth per Acre'
        prediction = model.predict([[subtotal]])
    elif 'Total in quantity' in user_input:
        prediction_type = 'Total in quantity'
        prediction = model.predict([[total]])
    elif 'Weight' in user_input:
        prediction_type = 'Weight'
        prediction = model.predict([[total]])
    else:
        prediction_type = "Could not find Relevant info, try again later."

    formatted_response = f"The predicted {prediction_type} is: {prediction[0]}"
    return formatted_response

def predict_shells(user_input):
    # Filter the crop data for almond shells
    pistachio_data = crop_data[crop_data['Crop'] == 'Almond Sbells']

    # Extract relevant information from user_input
    Bearing_Acreage = user_input.get('Bearing Acreage')
    Per_Acre = user_input.get('Growth per Acre')
    total = user_input.get('Total in quantity')
    unit = user_input.get('Weight')

    if 'Bearing Acreage' in user_input:
        # Make predictions related to price per unit
        prediction_type = 'Bearing Acreage'
        prediction = model.predict([[price_per_unit]])
        return formatted_response
    elif 'Growth Per Acre' in user_input:  # Make predictions related to price per unit
        prediction_type = 'Growth per Acre'
        prediction = model.predict([[subtotal]])
    elif 'Total in quantity' in user_input:
        prediction_type = 'Total in quantity'
        prediction = model.predict([[total]])
    elif 'Weight' in user_input:
        prediction_type = 'Weight'
        prediction = model.predict([[total]])
    else:
        prediction_type = "Could not find Relevant info, try again later."

    formatted_response = f"The predicted {prediction_type} is: {prediction[0]}"
    return formatted_response

def predict_financial_values(user_input):
    # Extract relevant information from user_input
    price_per_unit = user_input.get('price per unit in dollars')
    subtotal = user_input.get('subtotal')
    total = user_input.get('Total in dollars')

    if 'price per unit in dollars' in user_input:
        # Make predictions related to price per unit
        prediction_type = 'price per unit in dollars'
        prediction = model.predict([[price_per_unit]])
        return formatted_response
    elif 'subtotal' in user_input:# Make predictions related to price per unit
        prediction_type = 'subtotal'
        prediction = model.predict([[subtotal]])
    elif 'Total in dollars' in user_input:
        prediction_type = 'Total in dollars'
        prediction = model.predict([[total]])
    else:
        prediction_type = "Could not find Relevant info, try again later."

    formatted_response = f"The predicted {prediction_type} is: {prediction[0]}"
    return formatted_response


def predict_weather_impact(user_input):
    # Extract weather data
    temperature = user_input.get('temperature', 0)
    humidity = user_input.get('humidity', 0)
    rainfall = user_input.get('rainfall', 0)

    features = np.array([[temperature, humidity, rainfall]])
    prediction = ridge_model.predict(features)

    return prediction[0]

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    user_input = request.json.get('user_input')

    # Convert data to DataFrame
    keyword = extract_keyword(user_input)

    # Make prediction based on keyword
    if keyword in prediction_functions:
        prediction = prediction_functions[keyword](user_input)
    else:
        prediction = "Keyword not recognized"

    # Return prediction as JSON response
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True)