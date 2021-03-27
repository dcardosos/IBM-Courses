import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import GridSearchCV
from ipywidgets import interact, interactive, fixed, interact_manual

df = pd.read_csv('data/cars-clean.csv')

# only numeric features
df = df._get_numeric_data()
df.head()


def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    ax1 = sns.distplot(RedFunction, hist=False, color='r', label=RedName)
    sns.distplot(BlueFunction, hist=False, color='b', label=BlueName, ax=ax1)
    plt.title(Title)
    plt.show()
    plt.close()


y_data = df['price']
x_data = df.drop('price', axis=1)

# separate data
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.25, random_state=123
)

print('Shape Train:', x_train.shape[0], 'Shape Test:', x_test.shape[0])

# model
lr = LinearRegression()
lr.fit(x_train[['horsepower']], y_train)
print('with test:', lr.score(x_test[['horsepower']], y_test))
print('with train:', lr.score(x_train[['horsepower']], y_train))
yhat_lr = lr.predict(x_test[['horsepower']])

DistributionPlot(
    RedFunction=y_test,
    BlueFunction=yhat_lr,
    RedName='Actual Value',
    BlueName='Predict Value',
    Title='Distribution plot',
)

# cross validation
rcross = cross_val_score(
    lr, x_data[['horsepower']], y_data, cv=4
)  # how to choose num of folds
print(rcross.mean())
print(rcross)

# negative squared error
print(
    -1
    * cross_val_score(
        lr, x_data[['horsepower']], y_data, cv=4, scoring='neg_mean_squared_error'
    )
)

# accuracy
"""
print(
    cross_val_score(
        lr, x_data[['horsepower']].round(), y_data.round(), cv=4, scoring='accuracy'
    )
)
"""
# predict
yhat_cross = cross_val_predict(lr, x_data[['horsepower']], y_data, cv=4)
print(yhat_cross[:5])

DistributionPlot(
    y_test, yhat_cross, 'Actual Value', 'Predict Value', 'Distribution Plot'
)

# mais dados
lr_over = LinearRegression()
# lr_over.fit(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_train)

"""
DÁ ERRO AQUI, MAS FUNCIONA NO GOOGLE COLAB POR EXEMPLO, É BUG
print(
    lr_over.score(
        x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_test
    )
)
"""

# yhat_over = lr_over.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
