#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


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

# In[4]:


url_drivers="https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners"
html2 =urlopen(url_drivers)


# In[6]:


soup2 = BeautifulSoup(html2, 'lxml')
print(soup2.title)


# In[7]:


#find the table we are working with
drivers_table = soup2.find("table",{"class":"sortable plainrowheaders wikitable"})


# In[35]:


Driver=[]
Driver_Country=[]
#First_Win=[]
for row in drivers_table.findAll('tr'):
        cells=row.findAll('a')
        if len(cells)>1:
            Driver.append(cells[1].find(text=True))
            Driver_Country.append(cells[0].find(text=True))

            


# In[26]:


#rank and wins are a different tag type
Rank_driver=[]
Wins_driver=[]

for row in drivers_table.findAll('tr'):
        cells=row.findAll('td')
        if len(cells)>1:
            Rank_driver.append(cells[0].find(text=True))
            Wins_driver.append(cells[2].find(text=True))

import re
Wins_driver = re.findall("\d+",str(Wins_driver))
Rank_driver = re.findall("\d+",str(Rank_driver))


# In[29]:


F1_drivers_table = pd.DataFrame()
F1_drivers_table["Rank"] = Rank_driver
F1_drivers_table["Driver"] = Driver
F1_drivers_table["Driver Country"] = Driver_Country
F1_drivers_table["Wins"] = Wins_driver

print(F1_drivers_table)


# In[36]:


F1_drivers_table.to_csv("F1_driver_table.csv",index=False)

