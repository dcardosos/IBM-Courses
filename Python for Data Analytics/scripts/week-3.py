# exploratory data analysis (EDA)
# analisar as features, caracteristicas principais, variaveis importantes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

sns.set()

cars = pd.read_csv('data/cars_clean.csv')
cars.drop(columns=['Unnamed: 0'], inplace=True)
cars
# Descriptive statistics
print(cars.describe())
print(cars.describe(include=['object']))
drive_wheels_count = cars['drive-wheels'].value_counts().to_frame()
print(drive_wheels_count)

# boxplot
sns.boxplot(x='drive-wheels', y='price', data=cars)
plt.show()

# sc´çatter plot
# predictor/independent variables on x-axis
# target/dependent variables on y-axis
sns.scatterplot(x='engine-size', y='price', data=cars)
plt.show()

# groupby
df_group = cars[['drive-wheels', 'body-style', 'price']]
df_group = df_group.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
print(df_group)

# tabela dinamica com pivot
df_pivot = df_group.pivot(index='drive-wheels', columns='body-style')
print(df_pivot)

# heatmap
sns.heatmap(df_pivot, cmap='RdBu')
plt.show()

# correlation
# positive correlation
sns.regplot(x='engine-size', y='price', data=cars)
plt.ylim(
    0,
)
plt.show()

# negative correlation

# weak correlation
sns.regplot(x='compression-ratio', y='price', data=cars)
plt.show()

# correlation statistics
# pearson: correlation coef and p-value
stats.pearsonr(cars['horsepower'], cars['price'])

cars.columns
# heatmap correlation
cat_features = [
    'make',
    'num-of-doors' 'fuel-type',
    'aspiration',
    'num-of-doors',
    'body-style',
    'drive-wheels',
    'fuel-system',
    'num-of-cylinders',
    'engine-type',
    'engine-location',
    'aspiration-turbo',
    'aspiration-std',
    'fuel-type-diesel',
    'fuel-type-gas',
    'price-binned',
]

cars_num_features = set(cars) - set(cat_features)
print(cars[cars_num_features].corr())
sns.heatmap(cars[cars_num_features].corr(), annot=True, cmap='coolwarm')
plt.show()

# Chi-Square - association between two categorical variables
cont_table = pd.crosstab(cars['drive-wheels'], cars['drive-wheels'])
# stats.chi2_contigency(cont_table, correction= True)
