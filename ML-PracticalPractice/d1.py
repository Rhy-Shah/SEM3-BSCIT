from io import StringIO
import numpy as np

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
l3 = [1,2,3,4,5] 
arr = np.array([l1,l2,l3])
arr1 = arr.reshape(5,3)
print(arr1)

print(arr1[2:3,1:2])

arr2 = np.arange(0,10,step=2)
print(arr2)


import pandas as pd
df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['Column1','Column2','Column3','Column4'])
print(df)

data = ('a,b,c/n'
        '4,apple,bat,/n'
        '8,orange,cow,')

hp = pd.read_csv(StringIO(data),index_col=False)

print(hp)