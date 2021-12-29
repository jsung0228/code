#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv('DataSets/Minimum Wage Data.csv', encoding="latin")
df.to_csv('DataSets/minwage.csv', encoding='utf-8')


# In[4]:


df=pd.read_csv('DataSets/minwage.csv')


# In[5]:


df.head()


# In[6]:


gb=df.groupby('State')
gb.get_group('Alabama').set_index('Year').head()


# In[ ]:


act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    
    

