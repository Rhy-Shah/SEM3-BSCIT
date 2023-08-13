import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv('C:/Users/Rhythm Shah/Downloads/kc_house_data.csv')
print(df.head())

x = df[['bedrooms','bathrooms']]
y = df['price']

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.2,random_state=35)

model = linear_model.LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
x1 = df['bedrooms']
x2 = df['bathrooms']

print(metrics.mean_absolute_error)

fig=plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,projection='3d')
ax.scatter(x1,x2,y,c='black',marker='o')
plt.show()