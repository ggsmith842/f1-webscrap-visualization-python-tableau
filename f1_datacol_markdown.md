```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
```

### Constructor Wins Collection



```python
#get constructor data
url = "https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners_(constructors)"
html = urlopen(url)
```


```python
soup = BeautifulSoup(html, 'lxml')
```


```python
print(soup.title)
```

    <title>List of Formula One Grand Prix winners (constructors) - Wikipedia</title>
    


```python
#find the table we are working with
constructor_table = soup.find("table",{"class":"sortable wikitable plainrowheaders"})
```


```python
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
    

```


```python
print(Constructor)
```

    ['Ferrari', 'McLaren', 'Williams', 'Mercedes', 'Team Lotus', 'Red Bull', 'Brabham', 'Renault', 'Benetton', 'Tyrrell', 'BRM', 'Cooper', 'Alfa Romeo', 'Maserati', 'Vanwall', 'Matra', 'Ligier', 'Brawn', 'Kurtis Kraft', 'Jordan', 'Watson', 'March', 'Wolf', 'Honda', 'Epperly', 'Lotus F1', 'Kuzma', 'Porsche', 'Eagle', 'Hesketh', 'Penske', 'Shadow', 'Stewart', 'BMW Sauber', 'Toro Rosso']
    


```python
#rank and wins are a different tag type
Rank=[]
Wins=[]

for row in constructor_table.findAll('tr'):
        cells=row.findAll('td')
        if len(cells)>1:
            Rank.append(cells[0].find(text=True))
            Wins.append(cells[2].find(text=True))
           
```


```python
#extract numbers from scrapped data
import re 
Wins=re.findall('\d+', str(Wins))
Rank=re.findall('\d+', str(Rank))
```


```python
F1_Constructor_Table = pd.DataFrame()
F1_Constructor_Table["Rank"] = Rank
F1_Constructor_Table["Constructor"] = Constructor
F1_Constructor_Table["Country"] = Country
F1_Constructor_Table["Wins"] = Wins

```


```python
F1_Constructor_Table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Constructor</th>
      <th>Country</th>
      <th>Wins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Ferrari</td>
      <td>Italy</td>
      <td>238</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>McLaren</td>
      <td>United Kingdom</td>
      <td>182</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Williams</td>
      <td>United Kingdom</td>
      <td>114</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Mercedes</td>
      <td>Germany</td>
      <td>103</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Team Lotus</td>
      <td>United Kingdom</td>
      <td>79</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Red Bull</td>
      <td>Austria</td>
      <td>62</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Brabham</td>
      <td>United Kingdom</td>
      <td>35</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Renault</td>
      <td>France</td>
      <td>35</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Benetton</td>
      <td>United Kingdom</td>
      <td>27</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Tyrrell</td>
      <td>United Kingdom</td>
      <td>23</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>BRM</td>
      <td>United Kingdom</td>
      <td>17</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Cooper</td>
      <td>United Kingdom</td>
      <td>16</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Alfa Romeo</td>
      <td>Italy</td>
      <td>10</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Maserati</td>
      <td>Italy</td>
      <td>9</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Vanwall</td>
      <td>United Kingdom</td>
      <td>9</td>
    </tr>
    <tr>
      <th>15</th>
      <td>14</td>
      <td>Matra</td>
      <td>FRA</td>
      <td>9</td>
    </tr>
    <tr>
      <th>16</th>
      <td>14</td>
      <td>Ligier</td>
      <td>FRA</td>
      <td>9</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>Brawn</td>
      <td>United Kingdom</td>
      <td>8</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>Kurtis Kraft</td>
      <td>United States</td>
      <td>5</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>Jordan</td>
      <td>Ireland</td>
      <td>4</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>Watson</td>
      <td>United States</td>
      <td>3</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>March</td>
      <td>United Kingdom</td>
      <td>3</td>
    </tr>
    <tr>
      <th>22</th>
      <td>21</td>
      <td>Wolf</td>
      <td>Canada</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>21</td>
      <td>Honda</td>
      <td>Japan</td>
      <td>3</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>Epperly</td>
      <td>United States</td>
      <td>2</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>Lotus F1</td>
      <td>United Kingdom</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>Kuzma</td>
      <td>United States</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>Porsche</td>
      <td>Germany</td>
      <td>1</td>
    </tr>
    <tr>
      <th>28</th>
      <td>27</td>
      <td>Eagle</td>
      <td>United States</td>
      <td>1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>27</td>
      <td>Hesketh</td>
      <td>United Kingdom</td>
      <td>1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>27</td>
      <td>Penske</td>
      <td>United States</td>
      <td>1</td>
    </tr>
    <tr>
      <th>31</th>
      <td>27</td>
      <td>Shadow</td>
      <td>United Kingdom</td>
      <td>1</td>
    </tr>
    <tr>
      <th>32</th>
      <td>27</td>
      <td>Stewart</td>
      <td>United Kingdom</td>
      <td>1</td>
    </tr>
    <tr>
      <th>33</th>
      <td>27</td>
      <td>BMW Sauber</td>
      <td>Germany</td>
      <td>1</td>
    </tr>
    <tr>
      <th>34</th>
      <td>27</td>
      <td>Toro Rosso</td>
      <td>Italy</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
F1_Constructor_Table.to_csv("F1_constructor_table.csv",index=False)
```

### Driver Data Collection
Collect data on the best drivers of the last 70 years



```python
url_drivers="https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners"
html2 =urlopen(url_drivers)
```


```python
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2.title)
```

    <title>List of Formula One Grand Prix winners - Wikipedia</title>
    


```python
#find the table we are working with
drivers_table = soup2.find("table",{"class":"sortable plainrowheaders wikitable"})
```


```python
Driver=[]
Driver_Country=[]
#First_Win=[]
for row in drivers_table.findAll('tr'):
        cells=row.findAll('a')
        if len(cells)>1:
            Driver.append(cells[1].find(text=True))
            Driver_Country.append(cells[0].find(text=True))

            
```


```python
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
```


```python
F1_drivers_table = pd.DataFrame()
F1_drivers_table["Rank"] = Rank_driver
F1_drivers_table["Driver"] = Driver
F1_drivers_table["Driver Country"] = Driver_Country
F1_drivers_table["Wins"] = Wins_driver

print(F1_drivers_table)
```

        Rank              Driver  Driver Country Wins
    0      1  Michael Schumacher         Germany   91
    1      2      Lewis Hamilton  United Kingdom   84
    2      3    Sebastian Vettel         Germany   53
    3      4         Alain Prost          France   51
    4      5        Ayrton Senna          Brazil   41
    ..   ...                 ...             ...  ...
    103   77       Olivier Panis          France    1
    104   77        Jarno Trulli           Italy    1
    105   77       Robert Kubica          Poland    1
    106   77   Heikki Kovalainen         Finland    1
    107   77    Pastor Maldonado       Venezuela    1
    
    [108 rows x 4 columns]
    


```python
F1_drivers_table.to_csv("F1_driver_table.csv",index=False)
```
