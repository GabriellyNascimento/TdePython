#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


dataset = pd.read_csv(r'C:\Users\corlos eduardo\Documents\Arquivos Faculdade GABY\Phyton\analisedados\master.csv')


# In[6]:


type(dataset)


# In[7]:


dataset.head()


# In[11]:


dataset.columns


# In[19]:


dataset.loc[(dataset['suicides_no'] < 16) & (dataset['suicides/100k pop'] > 4 )]


# In[17]:


dataset[dataset['sex']=='female'].count()


# In[30]:


dataset['size'] = (dataset['suicides_no'])


# In[32]:


dataset['size']


# In[43]:


def suicides_no(s):
    if s >= 30:
        return 'Small'
    elif s >= 15:
        return 'Medium'
    elif s >= 1:
        return 'Big'


# In[44]:


dataset['suic_size'] = dataset['size'].apply(suicides_no)


# In[45]:


pd.value_counts(dataset['suic_size'])


# In[46]:


dataset.drop(['suic_size'], axis=1, inplace=True)


# In[47]:


dataset.isnull().sum()


# In[48]:


get_ipython().run_line_magic('matplotlib', 'notebook')
dataset.suicides_no.plot()


# In[84]:


dataset.plot(x='population', y='suicides_no', kind='scatter', title='N° de Suicídios x População', color='r')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




