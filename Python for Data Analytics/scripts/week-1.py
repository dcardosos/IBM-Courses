import pandas as pd
import numpy as np

path_ex = 'https://gist.githubusercontent.com/noamross/e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv'
path_orgin = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

file = pd.read_csv(path_orgin, header=None)
print(file.head())

# tipos de dados que temos
print(file.dtypes)

# informações gerais
print(file.info)

# mudando nomes das colunas
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

file.columns = headers

# trocando o sinal de interrog por not a number
file1 = file.replace('?', np.nan)

# jogando os not a number em price fora
file = file1.dropna(subset=['price'], axis=0)

# estatistica basica
# apenas numeros
print(file.describe)
# numeros e palavras
print(file.describe(include='all'))

print(file[['length', 'compression-ratio']].describe())
