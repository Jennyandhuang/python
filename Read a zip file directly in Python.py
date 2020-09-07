#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages
import pandas as pd
import numpy as np
import os
import zipfile


# In[2]:


#change directory
os.chdir('/Users/ChiHuang/Documents/python/python files')
os.listdir()


# In[ ]:


#read zip file
zf=zipfile.ZipFile('411512_835452_compressed_2019-Nov.csv.zip','r')


# In[3]:


#get the zip file name contained
zipfile.ZipFile.namelist(zf)


# In[ ]:


#choose the csv file to read under zip file
df = pd.read_csv(zf.open('2019-Nov.csv'))

