#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

current_font_list = matplotlib.rcParams['font.family']

font_path = "C:\Windows\Fonts\malgunbd.ttf"
kfont = matplotlib.font_manager.FontProperties(fname = font_path).get_name()
matplotlib.rcParams['font.family'] = [kfont] + current_font_list

pd_data = pd.read_csv('이륜차신고현황_시도별_20230309164825.csv', encoding = 'cp949')
pd_data.drop(0, axis = 0, inplace = True)
pd_data.columns = ['시도명', '시점', '시군구', '경형합계', '소형합계', '중형합계', '대형합계', '관용경형', '관용소형', '관용중형', '관용대형', '자가용경형', '자가용소형', '자가용중형', '자가용대형']
pd_data


# In[142]:


fil_list = ['관용경형', '관용소형', '관용중형', '관용대형', '자가용경형', '자가용소형','자가용중형', '자가용대형']
pd_data[fil_list] = pd_data[fil_list].astype(np.int64)
car_kind = pd.concat([pd_data['시군구'], pd_data[fil_list]], axis = 1)
car_kind = car_kind.set_index('시군구')
fig, axes = plt.subplots(5, 3, figsize = (6.4 * 3, 4.8 * 2), sharey = True, sharex = True)
for i, n in enumerate(car_kind.index):
    index_number = car_kind.index[(car_kind.index == n)]
    gu_list = car_kind.loc[index_number].values.tolist()[0]
    car_list = car_kind.columns.tolist()
    ax = axes[i // 3, i % 3]
    ax.set_title(n + ' 이륜차 신고 현황')
    ax.pie(gu_list)
    labels = [f'{car_list[i]} ({gu_list[i]/sum(gu_list)*100:.2f}%)' for i in range(len(car_list))]
    ax.legend(labels, loc=(1.3, 0), fontsize = 8)

