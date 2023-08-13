import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np

df = datasets.load_iris()
x = df.data
y = df.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=33)

model = RandomForestClassifier(random_state=41)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(metrics.classification_report(y_test,y_pred))
print(metrics.accuracy_score(y_test,y_pred))
print(metrics.confusion_matrix(y_test,y_pred))