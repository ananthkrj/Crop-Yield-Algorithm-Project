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

# Save the dataframes to a file for later use
temperature_df.to_csv('temperature_data.csv', index=False)
humidity_df.to_csv('humidity_data.csv', index=False)
rainfall_df.to_csv('rainfall_data.csv', index=False)
growing_season_df.to_csv('growing_season_data.csv', index=False)
