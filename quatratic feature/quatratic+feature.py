
# coding: utf-8

# In[38]:


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
    
    FenMu = 0
    FenZi = 0
    for i in range(100):
        FenMu -= X[i]**4
        FenZi += b*X[i]**3 + (c-Y[i])* X[i]**2
    a = FenZi/FenMu
    
    FenMu = 0
    FenZi = 0
    for i in range(100):
        FenMu -= X[i]**2
        FenZi += a*X[i]**3 + (c-Y[i])*X[i]
    b = FenZi/FenMu
    
    FenMu = -100
    FenZi = 0
    for i in range(100):
        FenZi += a*X[i]**2 +b*X[i] - Y[i]
    c = FenZi/FenMu
    
    print(a,b,c)
    

plt.figure()
Y_pred = a*X*X +b*X +c
plt.plot(X,Y_pred)
plt.show()
    


# In[9]:


Y_pred


# In[11]:


X


# In[7]:





# In[3]:


np.random.randint(100)

