#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# ### Constructor Wins Collection
# 

# In[20]:


#get constructor data
url = "https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners_(constructors)"
html = urlopen(url)


# In[21]:


soup = BeautifulSoup(html, 'lxml')


# In[111]:


print(soup.title)


# In[201]:


#find the table we are working with
constructor_table = soup.find("table",{"class":"sortable wikitable plainrowheaders"})


# In[146]:


Constructor=[]
Country=[]
#First_Win=[]
#Last_Win=[]

for row in constructor_table.findAll('tr'):
        cells=row.findAll('a')
        if len(cells)>1:
            Constructor.append(cells[0].find(text=True))
            Country.append(cells[1].find(text=True))
            #First_Win.append(cells[3].find(text=True))
            #Last_Win.append(cells[4].find(text=True))
    


# In[203]:


print(Constructor)


# In[204]:


#rank and wins are a different tag type
Rank=[]
Wins=[]

for row in constructor_table.findAll('tr'):
        cells=row.findAll('td')
        if len(cells)>1:
            Rank.append(cells[0].find(text=True))
            Wins.append(cells[2].find(text=True))
           


# In[191]:


#extract numbers from scrapped data
import re 
Wins=re.findall('\d+', str(Wins))
Rank=re.findall('\d+', str(Rank))


# In[194]:


F1_Constructor_Table = pd.DataFrame()
F1_Constructor_Table["Rank"] = Rank
F1_Constructor_Table["Constructor"] = Constructor
F1_Constructor_Table["Country"] = Country
F1_Constructor_Table["Wins"] = Wins


# In[195]:


F1_Constructor_Table


# In[200]:


F1_Constructor_Table.to_csv("F1_constructor_table.csv",index=False)


# ### Driver Data Collection
# Collect data on the best drivers of the last 70 years
# 

# In[ ]:




