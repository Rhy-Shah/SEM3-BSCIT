import pandas
import pydotplus
import graphviz
from sklearn import tree, datasets
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = datasets.load_iris()
print(df)


features=['sepal length','sepal width','petal length','petal width']
X = df[features]
y = df['Go']

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=33)

model = DecisionTreeClassifier()
model = model.fit(x_train, y_train)
# y_pred = model.predict(x_test)

# print("Classification report is " , metrics.classification_report(y_test,y_pred))
# print("Accuracy score is ",metrics.accuracy_score(y_test,y_pred))
# print("Confusion matrix is " , metrics.confusion_matrix(y_test,y_pred))
    
data = tree.export_graphviz(model, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('tree.png')

img=pltimg.imread('tree.png')
imgplot = plt.imshow(img)
plt.show()