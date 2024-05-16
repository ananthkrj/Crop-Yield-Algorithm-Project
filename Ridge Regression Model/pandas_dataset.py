import pandas as pd

# Temperature data
temperature_data = {
    'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'avg_high': [57, 61, 66, 72, 80, 89, 98, 97, 91, 80, 65, 57],
    'avg_low': [39, 42, 45, 49, 55, 62, 64, 63, 60, 53, 44, 39]
}
temperature_df = pd.DataFrame(temperature_data)

# Humidity data
humidity_data = {
    'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'humidity_level': [60, 65, 70, 75, 80, 85, 90, 90, 85, 80, 75, 70]
}
humidity_df = pd.DataFrame(humidity_data)

# Rainfall data
rainfall_data = {
    'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'rainfall_inches': [1.2, 2.3, 1.8, 0.9, 0.3, 0.1, 0.0, 0.0, 0.1, 0.4, 1.0, 1.5]
}
rainfall_df = pd.DataFrame(rainfall_data)

# Past crop yield data
past_crop_yield_data = {
    'Crop': ['Almond Meats', 'Almond Hulls', 'Almond Shells', 'Pistachios', 'Walnuts', 'Almond Meats', 'Almond Hulls', 'Almond Shells', 'Pistachios', 'Walnuts'],
    'Year': [2021, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2022],
    'Bearing Acreage': [109200.0, None, None, 911.0, 75700.0, 115500.0, None, None, 1126.0, 74500.0],
    'Per Acre': [1.15, None, None, 2.04, 2.45, 1.05, None, None, 2.8, 2.45],
    'Total': [125600, 242000, 120900, 1860, 186000, 120900, 242000, 120900, 3160, 192000],
    'Unit': ['ton', 'ton', 'ton', 'ton', 'ton', 'ton', 'ton', 'ton', 'ton', 'ton'],
    'Per unit in dollars': [3610.0, 130.0, 37.0, 4267.0, 1980.0, 3280.0, 213.0, 37.0, 4267.0, 1980.0],
    'Total in dollars': [453764000, 32666000, 534000, 8364000, 367825000, 397177000, 51521000, 4478000, 13463000, 145997000]
}
past_crop_yield_df = pd.DataFrame(past_crop_yield_data)

# CropAnd_WaterProjections data
CropAnd_WaterProjections_data = {
    'Crop': ['Alfalfa', 'Almonds', 'Other Crops', 'Pasture', 'Walnuts', 'Water', 'Idle'],
    '2018': [876, 35104, 1013, 3207, 1945, 10, 1903],
    '2020': [852, 35104, 999, 3119, 1934, 12, 1885],
    '2025': [792, 35104, 964, 2899, 1904, 15, 1839],
    '2030': [732, 35104, 929, 2678, 1874, 19, 1793],
    '2035': [671, 35104, 893, 2457, 1844, 23, 1747],
    '2040': [611, 35104, 858, 2237, 1814, 26, 1701]
}
CropAnd_WaterProjections_df = pd.DataFrame(CropAnd_WaterProjections_data)

# Soil characteristics data
soil_characteristics_data = {
    'Soil Horizons': ['Ap', 'Bt1', 'Bt2', '2Bt3', '2Bt4', '2Bqm1', '2Bqm2', '2Bq'],
    'soil_type': ['Loam', 'Loam', 'Loam', 'Clay', 'Clay', 'Indurated Duripan', 'Duripan', 'Duripan'],
    'pH': [7.3, 5.7, 5.9, 7.0, 7.3, 8.0, 8.0, 8.0],
    'nutrient_content': ['High', 'Good', 'High', 'High', 'High', 'High', 'High', 'High'],
    'depth': ['0-6 inches', '6-10 inches', '10-16 inches', '16-21 inches', '21-26 inches', '26-29 inches', '29-48 inches', '48-60 inches'],
    'organic_matter': ['Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium']
}
soil_characteristics_df = pd.DataFrame(soil_characteristics_data)
