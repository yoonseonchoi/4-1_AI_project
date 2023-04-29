#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
from PIL import Image


# In[2]:


df = pd.read_csv('list_attr_celeba.csv')
df = df[['image_id', 'Male']]
df.head()


# In[3]:


directory = './img_align_celeba'
imgs = os.listdir(directory)


# In[4]:


men_folder = './men'


# In[5]:


men_list = df[df['Male']==1]['image_id'].values


# In[6]:


for men in imgs:
    if men in men_list:
        with Image.open(os.path.join(directory, men)) as img:
            img.save(os.path.join(men_folder, men))


# In[ ]:




