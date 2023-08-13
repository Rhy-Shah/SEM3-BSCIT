import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

df = pd.read_csv('C:/Users/Rhythm Shah/Downloads/ML/Prac_4/doc.csv',names=['Message','Label'])
d = {'pos':1,'neg':0}
df['labelnum'] = df['Label'].map(d)

x = df['Message']
y = df['labelnum']

x_train,x_test,y_train,y_test = train_test_split(x,y)

std = CountVectorizer()
std_x_train = std.fit_transform(x_train)
std_x_test = std.transform(x_test)

model = MultinomialNB()
model.fit(std_x_train,y_train)
y_pred = model.predict(std_x_test)

print(metrics.accuracy_score(y_test,y_pred))
print(metrics.recall_score(y_test,y_pred))
print(metrics.precision_score(y_test,y_pred))