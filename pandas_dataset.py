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
    'humidity_level': ['muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy', 'muggy']
}
humidity_df = pd.DataFrame(humidity_data)

# Rainfall data
rainfall_data = {
    'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'rainfall_inches': [1.2, 2.3, 1.8, 0.9, 0.3, 0.1, 0.0, 0.0, 0.1, 0.4, 1.0, 1.5]
}
rainfall_df = pd.DataFrame(rainfall_data)

# Growing season data
growing_season_data = {
    'start_date': ['January 27'],
    'end_date': ['December 4'],
    'duration_days': [313]
}
growing_season_df = pd.DataFrame(growing_season_data)

# past crop yield data for 2021
past_crop_yield21_data = [
        {'Crop': 'Almond Meats', 'Year': 2021, 'Bearing Acreage': 109200, 'Per Acre': 1.15, 'Total': 125600, 'Unit': 'ton'},
        {'Crop': 'Almond Hulls', 'Year': 2021, 'Bearing Acreage': None, 'Per Acre': None, 'Total': 242000, 'Unit': 'ton'},
        {'Crop': 'Almond Shells', 'Year': 2021, 'Bearing Acreage': None, 'Per Acre': None, 'Total': 120900, 'Unit': 'ton'},
        {'Crop': 'Pistachios', 'Year': 2021, 'Bearing Acreage': 911, 'Per Acre': 2.04, 'Total': 1860, 'Unit': 'ton'},
        {'Crop': 'Walnuts', 'Year': 2021, 'Bearing Acreage': 75700, 'Per Acre': 2.45, 'Total': 186000, 'Unit': 'ton'}
]

past_crop_yield_df = pd.DataFrame(past_crop_yield21_data)

# past gross value data for 2021
gross_value21_data = [
        {'Crop': 'Almond Meats', 'Year': 2021, 'Per unit in dollars': 3610.00, 'Subtotal': None, 'Total in dollars': 453764000},
        {'Crop': 'Almond Hulls', 'Year': 2021, 'Per unit in dollars': 130.00, 'Subtotal': None, 'Total in dollars': 32666000},
        {'Crop': 'Almond Shells', 'Year': 2021, 'Per unit in dollars': 37.00, 'Subtotal': None, 'Total in dollars': 534000},
        {'Crop': 'Pistachios', 'Year': 2021, 'Per unit in dollars': 4267.00, 'Subtotal': None, 'Total in dollars': 8364000},
        {'Crop': 'Walnuts', 'Year': 2021, 'Per unit in dollars': 1980.00, 'Subtotal': None, 'Total in dollars': 367825000}
]
gross_value_data_df = pd.DataFrame(gross_value21_data)

# past crop yield data for 2022
past_crop_yield22_data = [
        {'Crop': 'Almond Meats', 'Year': 2022, 'Bearing Acreage': 115500, 'Per Acre': 1.05, 'Total': 120900, 'Unit': 'ton'},
        {'Crop': 'Almond Hulls', 'Year': 2022, 'Bearing Acreage': None, 'Per Acre': None, 'Total': 242000, 'Unit': 'ton'},
        {'Crop': 'Almond Shells', 'Year': 2022, 'Bearing Acreage': None, 'Per Acre': None, 'Total': 120900, 'Unit': 'ton'},
        {'Crop': 'Pistachios', 'Year': 2022, 'Bearing Acreage': 1126, 'Per Acre': 2.8, 'Total': 3160, 'Unit': 'ton'},
        {'Crop': 'Walnuts', 'Year': 2022, 'Bearing Acreage': 74500, 'Per Acre': 2.45, 'Total': 192000, 'Unit': 'ton'}
]
past_crop_yield_df = pd.DataFrame(past_crop_yield22_data)

# past gross value data for 2022
gross_value22_data = [
        {'Crop': 'Almond Meats', 'Year': 2022, 'Per unit in dollars': 3280.00, 'Subtotal': None, 'Total in dollars': 397177000},
        {'Crop': 'Almond Hulls', 'Year': 2022, 'Per unit in dollars': 213.00, 'Subtotal': None, 'Total in dollars': 51521000},
        {'Crop': 'Almond Shells', 'Year': 2022, 'Per unit in dollars': 37.00, 'Subtotal': None, 'Total in dollars': 4478000},
        {'Crop': 'Pistachios', 'Year': 2022, 'Per unit in dollars': 4267.00, 'Subtotal': None, 'Total in dollars': 13463000},
        {'Crop': 'Walnuts', 'Year': 2022, 'Per unit in dollars': 1980.00, 'Subtotal': None, 'Total in dollars': 145997000}
]
gross_value_data_df = pd.DataFrame(gross_value22_data)

# soil characteristics for San Joaquin
soil_characteristics_data = [
    {'Soil Horizons': 'Ap',
     'soil_type': 'Loam',
     'pH': 7.3,
     'nutrient_content': 'High',
     'depth': '0-6 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': 'Bt1',
     'soil_type': 'Loam',
     'pH': 5.7,
     'nutrient_content': 'Good',
     'depth': '6-10 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': 'Bt2',
     'soil_type': 'Loam',
     'pH': 5.9,
     'nutrient_content': 'High',
     'depth': '10-16 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': '2Bt3',
     'soil_type': 'Clay',
     'pH': 7.0,
     'nutrient_content': 'High',
     'depth': '16-21 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': '2Bt4',
     'soil_type': 'Clay',
     'pH': 7.3,
     'nutrient_content': 'High',
     'depth': '21-26 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': '2Bqm1',
     'soil_type': 'Indurated Duripan',
     'pH': 8.0,
     'nutrient_content': 'High',
     'depth': '26-29 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': '2Bqm2',
     'soil_type': 'Duripan',
     'pH': 8.0,
     'nutrient_content': 'High',
     'depth': '29-48 inches',
     'organic_matter': 'Medium',
    },
    {'Soil Horizons': '2Bq',
     'soil_type': 'Duripan',
     'pH': 8.0,
     'nutrient_content': 'High',
     'depth': '48-60 inches',
     'organic_matter': 'Medium',
    },
]
soil_characteristics_data_df = pd.DataFrame(soil_characteristics_data_data)

# contains valley-wide summaries of the farm counts, acreage,
# and crop diversity index by farm size bins
ValleyWide_FarmSizes_data = [
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
    },
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
     },
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
     },
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
     },
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
     },
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
     },
    {'Farm Size': 'Ap',
     'Farm Count': 'Loam',
     'Irrigable Acreage': 7.3,
     'Cropped Acreage': 'High',
     'Idle Land': '0-6 inches',
     'Trees/Vines': 'Medium',
     'Vegetables': 'Medium',
     'Field/Grain': 'Medium',
     'PastureAlfafa': 'Medium',
     'Average Crop Index Binned': 'Medium',
     },
]
ValleyWide_FarmSizes_data_df = pd.DataFrame(ValleyWide_FarmSizes_data)


BasinWide_FarmSizes_data = [
        {'Basin': 'Almond Meats', 'Farm Size': 2022, 'Farm Count': 115500, 'Per Acre': 1.05, 'Total': 120900, 'Unit': 'ton'},
        {'Crop': 'Almond Hulls', 'Year': 2022, 'Bearing Acreage': None, 'Per Acre': None, 'Total': 242000, 'Unit': 'ton'},
        {'Crop': 'Almond Shells', 'Year': 2022, 'Bearing Acreage': None, 'Per Acre': None, 'Total': 120900, 'Unit': 'ton'},
        {'Crop': 'Pistachios', 'Year': 2022, 'Bearing Acreage': 1126, 'Per Acre': 2.8, 'Total': 3160, 'Unit': 'ton'},
        {'Crop': 'Walnuts', 'Year': 2022, 'Bearing Acreage': 74500, 'Per Acre': 2.45, 'Total': 192000, 'Unit': 'ton'}
]
BasinWide_FarmSizes_data_df = pd.DataFrame(BasinWide_FarmSizes_data)


ValleyWide_FarmSizes_data
# Save the dataframes to a file for later use
# temperature_df.to_csv('temperature_data.csv', index=False),
# humidity_df.to_csv('humidity_data.csv', index=False),
# rainfall_df.to_csv('rainfall_data.csv', index=False),
# growing_season_df.to_csv('growing_season_data.csv', index=False)

# Access separate CSV files
past_crop_yield21 = pd.read_csv('past_crop_yield21_data.csv')
past_crop_yield22 = pd.read_csv('past_crop_yield22_data.csv')
farm_sizes = pd.read_csv('farm_sizes_data.csv')
soil_data = pd.read_csv('soil_characteristics_data.csv')