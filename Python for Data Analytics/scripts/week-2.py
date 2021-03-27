# Data processing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

path_orgin = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'
cars = pd.read_csv(path_orgin, header=None, names=headers)

not_int = [
    'make',
    'fuel-type',
    'aspiration',
    'num-of-doors',
    'body-style',
    'drive-wheels',
    'fuel-system',
    'num-of-cylinders',
    'engine-type',
    'engine-location',
]

# data formating
cars = cars.replace('?', 00)

for column in cars.columns:
    if column not in not_int:
        cars[column] = cars[column].astype(float)

# convert "mpg" to "L/100km"
"""
cars['city-mpg'] = 235 / cars['city-mpg']
cars['highway-mpg'] = 235 / cars['highway-mpg']
cars.rename(
    columns={'city-mpg': 'city-L/100km', 'highway-mpg': 'highway-L/100km'}, inplace=True
)
"""

# Missing values
cars = cars.replace(00, np.nan)

# dropar se for pouco
cars.dropna(subset=['price'], axis=0, inplace=True)
cars.reset_index(drop=True, inplace=True)

# substituir pela média
avg_norm_loss = cars['normalized-losses'].mean()
cars['normalized-losses'] = cars['normalized-losses'].replace(np.nan, avg_norm_loss)
avg_bore = cars['bore'].mean()
cars['bore'].replace(np.nan, avg_bore, inplace=True)
avg_stroke = cars['stroke'].mean()
cars['stroke'].replace(np.nan, avg_stroke, inplace=True)
avg_horsepower = cars['horsepower'].mean()
cars['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peak_rpm = cars['peak-rpm'].mean()
cars['peak-rpm'].replace(np.nan, avg_peak_rpm, inplace=True)

# substituir pela frequencia
max_freq_num_doors = cars['num-of-doors'].value_counts().idxmax()
cars['num-of-doors'].replace(np.nan, max_freq_num_doors, inplace=True)

# data normalization
# existem três modos:
# dividir cada valor pelo maximo da lista (entre 0 e 1)
cars['length'] / cars['length'].max()

# método do min max (entre 0 e 1)
(cars['length'] - cars['length'].min() / (cars['length'].max() - cars['length'].min()))

# z-score (entre -3 e 3)
cars['length'] = (cars['length'] - cars['length'].mean()) / cars['length'].std()
cars['width'] = (cars['width'] - cars['width'].mean()) / cars['width'].std()
cars['height'] = (cars['height'] - cars['height'].mean()) / cars['height'].std()

# Binning: agrupar valores em bins, caixas
# para isso usamos a função linspace do numpy
bins = np.linspace(cars['price'].min(), cars['price'].max(), 4)
group_names = ['Low', 'Medium', 'High']
cars['price-binned'] = pd.cut(
    cars['price'], bins, labels=group_names, include_lowest=True
)
print(cars[['price', 'price-binned']].tail())

_ = plt.hist(cars['price-binned'], bins=3)
plt.show()

# turning categorical variables into quantitative variables
# usa-se pd.get_dummies()
dummy_variable_1 = pd.get_dummies(cars['fuel-type'])
dummy_variable_1.rename(
    columns={'gas': 'fuel-type-gas', 'diesel': 'fuel-type-diesel'}, inplace=True
)
cars = pd.concat([cars, dummy_variable_1], axis=1)

dummy_variable_2 = pd.get_dummies(cars['aspiration'])
dummy_variable_2.rename(
    columns={'std': 'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True
)
cars = pd.concat([cars, dummy_variable_2], axis=1)

cars.drop(['fuel-type', 'aspiration'], axis=1, inplace=True)
print(cars.head())

cars.to_csv('data/cars_clean.csv')
