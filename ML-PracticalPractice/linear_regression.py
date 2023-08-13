from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

df = pd.read_csv('C:/Users/Rhythm Shah/Downloads/lr.csv')
print(df.describe())

x = df['spend'].values.reshape(-1,1)
y = df['freq'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=16)

model = linear_model.LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(metrics.mean_absolute_error(y_test,y_pred))
print(metrics.mean_squared_error(y_test,y_pred))

plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred)
plt.show()
