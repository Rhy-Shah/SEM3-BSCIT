import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# data = sns.load_dataset('iris')
# #data.info()
# print(data.head())
# # print(data.describe())

# # print(data['species'].value_counts())

# # g = sns.pairplot(data, hue='species', markers='+')
# # plt.show()

arr = [2,4,6,8,10]
for i in arr:
    for j in range(len(arr)):
        print(j)