#!/usr/bin/env python
# coding: utf-8

# #### 전복
# 
# data url: https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data
# 
# 1. [함수] requests 패키지를 이용해 데이터 가져와서 ndarray로 변환.
# 
# 2. [함수] 성별이 'M'인 데이터를 필터, Length와 Diameter 간 상관도를 반환
# 
# 3. __name__ 값이 __main__ 이면, 1, 2함수를 실행, 2번 함수의 반환 값을 프린트.

# In[37]:


import requests
import numpy as np

def nda():
    x= requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
    raw_data = []
    for line in x.text.split('\n'):
        raw_data.append(line.split(','))
    np_data = np.array(raw_data[:-1])
    return np_data


# In[38]:


def cor(np_data): 
    filter_m = np_data[:, 0] == 'M'
    np_data_f = np_data[filter_m]
    np_data_f = np_data_f[:, 1:].astype(np.float64)
#     data_len = np_data_f[:, 0]
#     data_dia = np_data_f[:, 1]
    return np.corrcoef(np_data_f[:, 0], np_data_f[:, 1])


# In[40]:


if __name__ == '__main__' :
	a = nda()
	b = cor(a)
	print(b)

