#!/usr/bin/env python
# coding: utf-8

# In[86]:


import numpy as np
import matplotlib.pyplot as plot

np.set_printoptions(precision = 5, suppress = True)

def my_split(s):
    block_start = False
    start_index = 0
    ret_list=[]
    for i, c in enumerate(s):
        if block_start==False:
            if c==',':
                ret_list.append(s[start_index:i])
                start_index=i+1
            elif c=='"':
                block_start=True
                start_index = i
        else:
            if c=='"':
                block_start=False
    if s[-1]!=',':
        ret_list.append(s[start_index:])
    return ret_list

def split_len(data_list):
    len_list=[]
    for e in data_list:
        len_list.append(len(e))
    print(set(len_list))
    if len(set(len_list))>1:
        for i in set(len_list):
            print(i, len_list.count(i))
    return set(len_list)

def dist_np(p1, p2): #  [3,10]  [5,25]
    return math.sqrt(sum((p2-p1)**2))


def check_split(list_data):
    t = set()
    for e in list_data:
        t.add(len(e))
    return len(t)


# In[87]:


def np_data_from_data_go_kr_csv(filename):
    t = []
    with open(filename, encoding = 'cp949') as f:
        for line in f:
            t.append(my_split(line[:-1]))
    if check_split(t) != 1:
        return None
    else:
        return np.array(t)
    
def print_index_title(data):
    for e in enumerate(data[0]):
        print(e)


# In[88]:


def target1(data):
    sub_data = np_data[1:, [13, 17]]
    
    sub_data[sub_data == '0'] = ''
#     sub_data = np.where(sub_data == '0', '', sub_data)
    
    filter1 = sub_data[:, 1] != ''
    sub_data_f = sub_data[filter1].astype(np.float64)
#     print(np.unique(sub_data_f[:, 0]))
#     print(np.unique(sub_data_f[:, 1]))
#     print(sub_data_f[:10])

    filter2 = sub_data_f[:, 0] < 100
    sub_data_f2 = sub_data_f[filter2]

#     _, axe = plot.subplots()
#     axe.scatter(sub_data_f2[:, 0], sub_data_f2[:, 1])
    
    return np.corrcoef(sub_data_f2[:, 0], sub_data_f2[:, 1])[0][1]
    
# target1(np_data)


# In[89]:


def target2(data):
    sub_data = np_data[1:, 7]
    val, cnt = np.unique(sub_data, return_counts = True)
#     print(val, cnt)
    return cnt[2] * 100 / np.sum(cnt[1:])
    
# target2(np_data)


# In[90]:


def target3(data):
    sub_data = np_data[1:, [11, 7]]
#     print(np.unique(sub_data[:, 0]))
#     print(np.unique(sub_data[:, 1]))
    t = []
    for e in np.unique(sub_data[:, 0]):
#         print(e)
        filter1 = sub_data[:, 0] == e
        sub_data_f = sub_data[filter1]
#         print(sub_data_f)
        sub_data_f_y = sub_data_f[sub_data_f[:, 1] == 'Y']
        sub_data_f_n = sub_data_f[sub_data_f[:, 1] == 'N']
#         print(e, len(sub_data_f_y), len(sub_data_f_n))
#         print(np.unique(sub_data_f[:, 1], return_counts = True))
#         print(len(sub_data_f_y) / len(sub_data_f_n))
        yes_count = len(sub_data_f_y)
        no_count = len(sub_data_f_n)
        yes_no_count = yes_count + no_count
        if yes_no_count == 0:
            yes_no_count = 1
        t.append((e, yes_count, no_count, yes_count * 100 / yes_no_count))
    t = np.array(t).astype(np.float64)
    t = np.array(sorted(t, key = lambda x: x[0]))
    return t
    
# target3(np_data)


# In[91]:


def target4(data):
    sub_data = np_data[1:, [11, 14]]
#     print(np.unique(sub_data[:, 0]))
#     print(np.unique(sub_data[:, 1]))
    sub_data[sub_data == 'y'] = 'Y'
    sub_data[sub_data == 'n'] = 'N'
#     print(np.unique(sub_data[:, 1]))

    t = []
    for e in np.unique(sub_data[:, 0]):
#         print(e)
        filter1 = sub_data[:, 0] == e
        sub_data_f = sub_data[filter1]
#         print(sub_data_f)
        sub_data_f_y = sub_data_f[sub_data_f[:, 1] == 'Y']
        sub_data_f_n = sub_data_f[sub_data_f[:, 1] == 'N']
#         print(e, len(sub_data_f_y), len(sub_data_f_n))
#         print(np.unique(sub_data_f[:, 1], return_counts = True))
#         print(len(sub_data_f_y) / len(sub_data_f_n))
        yes_count = len(sub_data_f_y)
        no_count = len(sub_data_f_n)
        yes_no_count = yes_count + no_count
        if yes_no_count == 0:
            yes_no_count = 1
        t.append((e, yes_count, no_count, yes_count * 100 / yes_no_count))
    t = np.array(t).astype(np.float64)
    t = np.array(sorted(t, key = lambda x: x[0]))
    return t
    
    
# target4(np_data)


# In[92]:


def target5 (data):
    sub_data = np_data[1:, [11, 16]]
    
    sub_data[sub_data == 'n'] = 'N'
    filter1 = sub_data[:, 1] != ' '
    sub_data = sub_data[filter1]

    t = []
    for e in np.unique(sub_data[:, 0]):
#         print(e)
        filter1 = sub_data[:, 0] == e
        sub_data_f = sub_data[filter1]
#         print(sub_data_f)
        sub_data_f_y = sub_data_f[sub_data_f[:, 1] == 'Y']
        sub_data_f_n = sub_data_f[sub_data_f[:, 1] == 'N']
#         print(e, len(sub_data_f_y), len(sub_data_f_n))
#         print(np.unique(sub_data_f[:, 1], return_counts = True))
#         print(len(sub_data_f_y) / len(sub_data_f_n))
        yes_count = len(sub_data_f_y)
        no_count = len(sub_data_f_n)
        yes_no_count = yes_count + no_count
        if yes_no_count == 0:
            yes_no_count = 1
        t.append((e, yes_count, no_count, yes_count * 100 / yes_no_count))
    t = np.array(t).astype(np.float64)
    t = np.array(sorted(t, key = lambda x: x[0]))
    return t
    
    
# target5(np_data)


# In[93]:


if __name__ == '__main__':
    np_data = np_data_from_data_go_kr_csv('xing.csv')
    print(target1(np_data))
    print(target2(np_data))
    print(target3(np_data))
    print(target4(np_data))
    print(target5(np_data))
#     print_index_title(np_data)
#     print(np_data[:3])

