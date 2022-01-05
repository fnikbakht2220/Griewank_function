#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
def griewank_func(x_local):
    gtotal=0
    D=x_local.size
    for i,x_i in enumerate (x_local):
        gtotal += (x_i**2 / 4000) + math.cos(x_i / math.sqrt(i+1) )
    gtotal += 1 + gtotal
    return gtotal

x_local=np.array([2,3,4,5])
b=griewank_func(x_local)
print (b) 
    
    


# In[ ]:




