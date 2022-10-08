#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


athletes=pd.read_csv('C:\\Users\\ADMIN\\Desktop\\athlete_events.csv')


# In[4]:


region=pd.read_csv('C:\\Users\\ADMIN\\Desktop\\noc_regions.csv')


# In[5]:


athletes.head()


# In[6]:


region.head()


# In[7]:


athletes_df=athletes.merge(region ,how='left',on='NOC') 


# In[8]:


athletes_df.shape


# In[9]:


athletes_df.head()


# In[10]:


athletes_df.rename(columns={'region':'Region','notes':'Notes'},inplace=True);     #Rename column name
athletes_df


# In[11]:


nan_values=athletes_df.isnull().sum()  
nan_values


# In[12]:


athletes_df.columns [athletes_df.isnull ().any ()]


# In[13]:


athletes_df.query('Team=="India"').head(5)


# In[14]:


#Top countries participating
top_countries=athletes_df.Team.value_counts().head(10)


# In[15]:


top_countries


# In[16]:


#plot for these top 10 countries
plt.figure(figsize=(12,6))
plt.title('overall participation by country')
sns.barplot(x=top_countries.index, y=top_countries);


# In[17]:


gender_counts=athletes_df.Sex.value_counts()


# In[18]:


gender_counts


# In[19]:


#total number of female in each olympics.
femaleplayers=athletes_df[(athletes_df.Sex=='F') & (athletes_df.Season=='Summer')]


# In[20]:


femaleplayers


# In[21]:


#gold medal athletes
goldmedals=athletes_df[(athletes_df.Medal=='Gold')]


# In[22]:


goldmedals


# In[23]:


#gold beyond 60.
age60gold=athletes_df[(athletes_df.Medal=='Gold') &(athletes_df.Age>60)]


# In[24]:


age60gold


# In[ ]:




