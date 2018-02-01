
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('quatratic data.csv')
X = np.array(df.a)
Y = np.array(df.b)
plt.figure()
plt.scatter(X,Y)
plt.show()
a = 1
b = 2
c = 3


rate = 0.6
#rate是迭代更新的权重，用这次的min（误差除以上次的误差，0.9^(epoch/10))作为比例。
for epoch in range(5000):
    
    FenMuA = 0
    FenZiA = 0
    FenMuC = -100
    FenZiC = 0
    FenMuB = 0
    FenZiB = 0
    for i in range(100):
        FenMuA -= X[i]**4
        FenZiA += b*X[i]**3 + (c-Y[i])* X[i]**2
        FenMuB -= X[i]**2
        FenZiB += a*X[i]**3 + (c-Y[i])*X[i]
        FenZiC += a*X[i]**2 +b*X[i] - Y[i]
        
    a = FenZiA/FenMuA
    b = FenZiB/FenMuB
    c = FenZiC/FenMuC
    
    print(a,b,c)
    

plt.figure()
Y_pred = a*X*X +b*X +c
plt.plot(X,Y_pred)
plt.show()
    

