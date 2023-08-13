import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np

df = pd.read_csv('C:/Users/Rhythm Shah/Downloads/housinng.csv')
print(df.describe())

x = df.iloc[:,0:3]
y = df['median_income']
print(x)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=5)
model = RandomForestRegressor(n_estimators=20,random_state=41)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(metrics.mean_absolute_error(y_test,y_pred))
print(metrics.mean_squared_error(y_test,y_pred))
print(np.sqrt)