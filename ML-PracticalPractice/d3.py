import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset('iris')
p = sns.countplot('sepal_length',data=iris)
print(iris)
b = iris.corr()
a = sns.heatmap(b)
plt.imshow(a,cmap='hot')
plt.show()