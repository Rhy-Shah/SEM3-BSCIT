import pandas
from sklearn import tree
import pydotplus
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
df = pandas.read_csv("d6.csv")
d = {'Yes': 1, 'No': 0}
df["Ethanol"] = df["Ethanol"].map(d)
features = ["Ethanol", "Density", "Sulphates", "Alcohol", "Price"]
X = df[features]
Y = df["Quality"]
print(X)
print(Y)
print()
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, Y)
training_set, test_set = train_test_split(df, test_size=0.2, random_state=1)
X_train = training_set.iloc[:, 0:5].values
Y_train = training_set.iloc[:, 5].values
X_test = test_set.iloc[:, 0:5].values
Y_test = test_set.iloc[:, 5].values

scaler = StandardScaler().fit(X_train)
X0 = scaler.transform(X_train)
X1 = scaler.transform(X_test)

le = LabelEncoder()
encode_target = le.fit_transform(Y_train)
encode_test_target = le.fit_transform(Y_test)
data_model = dtree.fit(X_train, encode_target.astype(int))
prediction = data_model.predict(X_test)
print("Prediction: ", prediction)
a = confusion_matrix(encode_test_target.astype(int), prediction)
print("Confusion Matrix: ", a)
b = accuracy_score(encode_test_target.astype(int), prediction)
print("Accuracy: ", b)


data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('2.png')
img = pltimg.imread('2.png')
imgplot = plt.imshow(img)
plt.show()
