# model evaluation
# separate in train & test data - tecnica holdout
from sklearn.model_selection import train_test_split

# X_train, x_test, Y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=123)
# generalization error: quanto mais treino, o desempenho de generalização será menor mas o modelo será mais preciso

# cross validation - tecnica
from sklearn.model_selection import cross_val_score

# dividi nossos dados em pedaços, faz um train_test_split com eles e retorna um r-score, dps fazemos a média
# scores  =  cross_val_score(lr, x_data, y_data, cv=3)
# scores.mean()
# variable = cross_val_score(type of model, data, data target, folds)

# usa-se para fazer a previsão de fato
from sklearn.model_selection import cross_val_predict

# cross_val_score(lr, x_data, y_data, cv=3, scoring='accuracy')

# Como escolher a melhor polynomial order pra regression
# o error MSE de training diminui com o aumento da order, mas o test a partir de certo ponto aumenta
"""
Rsqu_test = []
order = [1, 2, 3, 4]

for n in order:
    pr = PolynomialFeatures(degree=n)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])

    lr.fit(x_train_pr, x_test_pr)

    Rsqu_test.append(lr.score(x_test_pr, x_test))

"""

# Rigde Regression: controla os coef giga de ordens polinomiais ordens giga introduzindo o param alpha
from sklearn.linear_model import Ridge

RidgeModel = Ridge(alpha=0.01)
# como escolher o alpha?

# Grid Search: pega o modelo e calcula diferentes valores nos hyperparameters, depois tira o R-score or MSE
from sklearn.model_selection import GridSearchCV

parameters1 = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000, 100000]}]
RR = Ridge()
Grid1 = GridSearchCV(RR, parameters1, cv=4)
Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)

Grid1.best_estimator_

scores = Grid1.cv_results_
scores['mean_test_score']

for param, mean_val, mean_test in zip(
    scores['params'], scores['mean_test_score'], scores['mean_train_score']
):
    print(param, 'R^2 on test data:', mean_val, 'R^2 on train data:', mean_test)
