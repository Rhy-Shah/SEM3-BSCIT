from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = datasets.load_iris()
x = df.data
y = df.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=16)

std = StandardScaler()
std_x_train = std.fit_transform(x_train)
std_x_test = std.transform(x_test)

model = KNeighborsClassifier(n_neighbors=5,n_jobs=1)
model.fit(std_x_train,y_train)
y_pred = model.predict(x_test)

print("Classification report is " , metrics.classification_report(y_test,y_pred))
print("Accuracy score is ",metrics.accuracy_score(y_test,y_pred))
print("Confusion matrix is " , metrics.confusion_matrix(y_test,y_pred))