import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix

df = datasets.load_iris()
x = df.data
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=33)

std = StandardScaler()
std_x_train = std.fit_transform(x_train)
std_x_test = std.transform(x_test)

model = LogisticRegression(random_state=0)
model.fit(std_x_train,y_train)
y_pred = model.predict(std_x_test)

print("Classification report is " , classification_report(y_test,y_pred))
print("Accuracy score is ",accuracy_score(y_test,y_pred))
print("Confusion matrix is " , confusion_matrix(y_test,y_pred))
