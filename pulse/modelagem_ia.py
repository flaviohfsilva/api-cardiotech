from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import xgboost as xgb
import plotly.express as px
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import joblib

dados = pd.read_csv('heart.csv')

x = dados.drop(['output'], axis=1)
y = dados['output']

x.shape, y.shape


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


print("Dados de treino tem {} amostras.".format(X_train.shape[0]))
print("Dados de teste tem  {} amostras.".format(X_test.shape[0]))

scaler = StandardScaler()

# Ajustando o StandardScaler nos dados de treino
scaler.fit(X_train)

# Padronizando todas as características nos dados de treino e teste
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Substituindo as características padronizadas nos dados originais
X_train = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test = pd.DataFrame(X_test_scaled, columns=X_test.columns)

X_train


model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

model.fit(X_train, y_train)

score = model.score(X_test, y_test)


joblib.dump(model, 'pulseIA_model_knn.pkl')










