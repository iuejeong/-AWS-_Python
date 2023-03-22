#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
def my_sq_prod(numpy_ndarry):
    
    b = np.prod((numpy_ndarry*numpy_ndarry))
    
    return b
my_sq_prod(np.array([1,2,3]))

def score_check():
    score = 0
    if my_sq_prod(np.array([1, 2, 3])) == 36:
        score += 30
        print(score)

if __name__ == "__main__":
    score_check()

