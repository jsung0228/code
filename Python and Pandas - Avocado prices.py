#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd

df = pd.read_csv("DataSets/avocado.csv")


# In[6]:


df.head(3)


# In[7]:


df.tail(3)


# In[27]:


df["Date"].head()


# In[37]:


albany_df = df[df['region'] == "Albany"]
albany_df.head()


# In[38]:


albany_df.index


# In[39]:


albany_df.set_index("Date")


# In[33]:


albany_df.plot()


# In[47]:


albany_df.index = pd.to_datetime(albany_df.index)


# In[48]:


albany_df["AveragePrice"].plot()


# In[49]:


albany_df['AveragePrice'].rolling(25).mean().plot()


# In[50]:


albany_df.head(25)


# In[51]:


albany_df.sort_index(inplace = True)


# In[53]:


albany_df['AveragePrice'].rolling(25).mean().plot()


# In[56]:


albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()


# In[58]:


albany_df.dropna()


# In[63]:


list(set(df['region'].values.tolist()))


# In[64]:


df['region'].unique()


# In[87]:


import pandas as pd

df = pd.read_csv("DataSets/avocado.csv")
df=df.copy()[df['type']=='organic']
df['Date'] = pd.to_datetime(df['Date'])
#df.set_index("Date")
df.sort_values(by="Date", ascending = True, inplace = True)

graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets! (so df rather than series)
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])


# In[88]:


graph_df.plot()


# In[90]:


graph_df.plot(figsize=(8,10), legend=False)

