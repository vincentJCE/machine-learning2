
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(100)
Y = 3* X*X + 4*X + 1 + np.random.randn(100)*0.5
plt.figure()
plt.scatter(X,Y)
plt.show()
df = pd.DataFrame({'a':X,'b':Y})
df.to_csv('quatratic data.csv')


# In[12]:




