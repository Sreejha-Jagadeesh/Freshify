import random
import pandas as pd

# Define the range of values for each variable
ethylene_min_mg = {
    'mature-green': 0.1,
    'ripening': 0.2,
    'over-ripening': 0.3,
    'spoiled': 0.5
}
ethylene_max_mg = {
    'mature-green': 2,
    'ripening': 8,
    'over-ripening': 15,
    'spoiled': 30
}

respiration_min_ml = {
    'mature-green': 10,
    'ripening': 12,
    'over-ripening': 20,
    'spoiled': 50
}
respiration_max_ml = {
    'mature-green': 30,
    'ripening': 40,
    'over-ripening': 70,
    'spoiled': 100
}

temperature_min_celsius = {
    'mature-green': 13,
    'ripening': 15,
    'over-ripening': 20,
    'spoiled': 25
}
temperature_max_celsius = {
    'mature-green': 14,
    'ripening': 20,
    'over-ripening': 25,
    'spoiled': 30
}

relative_humidity_min_percent = {
    'mature-green': 90,
    'ripening': 90,
    'over-ripening': 90,
    'spoiled': 90
}
relative_humidity_max_percent = {
    'mature-green': 95,
    'ripening': 95,
    'over-ripening': 95,
    'spoiled': 95
}

# Define the MAR model parameters
k_ethylene = 0.0002  # ethylene reaction rate constant
K_m = 0.1  # Michaelis-Menten constant for ethylene
Q_10 = 2  # temperature coefficient for respiration rate

# Generate random values within the specified ranges
ethylene_values = [random.uniform(ethylene_min_mg[stage], ethylene_max_mg[stage]) for _ in range(1000) for stage in ethylene_min_mg]
respiration_values = [random.uniform(respiration_min_ml[stage], respiration_max_ml[stage]) for _ in range(1000) for stage in respiration_min_ml]
temperature_values = [random.uniform(temperature_min_celsius[stage], temperature_max_celsius[stage]) for _ in range(1000) for stage in temperature_min_celsius]
relative_humidity_values = [random.uniform(relative_humidity_min_percent[stage], relative_humidity_max_percent[stage]) for _ in range(1000) for stage in relative_humidity_min_percent]

# Calculate the number of days left until bananas ripen based on the MAR model
days_to_ripen = [
    abs((-1 / (k_ethylene * ethylene))) *
    (
        (respiration / Q_10**((temperature - 20) / 10)) *
        (1 - (ethylene / (ethylene + K_m)))**2
    )
    for ethylene, respiration, temperature, relative_humidity in zip(ethylene_values, respiration_values, temperature_values, relative_humidity_values)
]

# Create a Pandas DataFrame to store the synthetic data
data = {
    'ethylene (ul C2H4/kg·hr)': ethylene_values,
    'respiration rate (ml CO2/kg·hr)': respiration_values,
    'temperature (°C)': temperature_values,
    'relative humidity (%)': relative_humidity_values,
    'days to ripen': days_to_ripen
}
df = pd.DataFrame(data)

# Save the synthetic dataset to a CSV file
df.to_csv('synthetic_fruit_data.csv', index=False)