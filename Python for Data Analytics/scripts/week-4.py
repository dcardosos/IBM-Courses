# model development
# linear regression: y = b0 + b1x
# b0 = the intercept; b1 = the slope
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

cars = pd.read_csv('data/cars-clean.csv')
lm = LinearRegression()
X = cars[['highway-mpg']]
Y = cars[['price']]
lm.fit(X, Y)
Yhat = lm.predict(X)
lm.intercept_
lm.coef_
# price = 38423.3 - 821.73x

# multiple linear regression
Z = cars[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, cars['price'])
yhat2 = lm.predict(Z)
lm.intercept_
lm.coef_
# Y = -15824 + 53.61x1 + 4.71x2 + 81.47x3 + 36.39x4

# Model evaluation
# regression plot
sns.regplot(x='highway-mpg', y='price', data=cars)
plt.show()

# residual plot: serve pra analisar se a função tem que ser linear or not-linear
# curvatura indica que assumir função linear é um erro
sns.residplot(x='highway-mpg', y='price', data=cars)
plt.show()

# distribution plot: predict value x actual value
# simple
ax1 = sns.distplot(cars['price'], hist=False, color='r', label='Actual Value')
sns.distplot(Yhat, hist=False, color='b', label='Predict Value', ax=ax1)
plt.show()

# multiple
ax2 = sns.distplot(cars['price'], hist=False, color='r', label='Actual Value')
sns.distplot(yhat2, hist=False, color='b', label='Predict Value', ax=ax2)
plt.show()

# polynomial regression and pipelines
# "ao elevar ao quadrado ou definir termos de ordem superior de variáveis preditoras"
# o modelo pode ser quadrático (segunda ordem): Y = b0 + b1x1 + b2(x1)^2
# cubico (teceira ordem): Y = b0 + b1x1 + b2(x2)^2 + b3(x1)^3
x = cars['price']
y = cars['highway-mpg']
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

# multi dimensional polynomial: PolynomialFeatures
pr = PolynomialFeatures(degree=2, include_bias=False)
x_polly = pr.fit_transform(cars[['horsepower', 'curb-weight']])
x_polly
# intuitivo
pr = PolynomialFeatures(degree=2, include_bias=False)
pr.fit_transform([[1, 2]])  # x1 e x2
# output: x1, x2, x1x2, x1^2, x2^2

# normalization
SCALE = StandardScaler()
SCALE.fit(cars[['horsepower', 'highway-mpg']])
x_scale = SCALE.transform(cars[['horsepower', 'highway-mpg']])
x_scale

# pipelines - simplificação
Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(degree=2)),
    ('mode', LinearRegression()),
]

pipe = Pipeline(Input)
a = cars[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
pipe.fit(
    cars[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], cars['price']
)
yhat = pipe.predict(a)

ax3 = sns.distplot(cars['price'], hist=False, color='r', label='Actual Value')
sns.distplot(yhat, hist=False, color='b', label='Predict Value', ax=ax3)

# measure for in-sample evaluation
# mean-squared error: sklearn mean_squared_error
mean_squared_error(cars['price'], Yhat)
mean_squared_error(cars['price'], yhat)

# r-squared: coef of determination: lm.score: quanto a variability das predict variable
# é explicada pelas independent variables
lm.score(X, Y)
