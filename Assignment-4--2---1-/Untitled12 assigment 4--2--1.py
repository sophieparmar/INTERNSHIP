#!/usr/bin/env python
# coding: utf-8

# In[28]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import requests
import re


# In[18]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[19]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[20]:


Top_Rank=[]
Vedio_Name=[]
Artist_Name=[]
Upload_date=[]
Views=[]


# In[21]:


rk=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[1]")
for i in rk:
    if i.text is None :
        Top_Rank.append("--") 
    else:
        Top_Rank.append(i.text)
print(len(Top_Rank),Top_Rank)


# In[ ]:


# scraping Top_Rank from the given page
Top_tags=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[1]")
for i in Top_tags[0:20]:
    Top=i.text
    Top_Rank.append(Top)
    
# scraping Vedio_Name from the given page
Vedio_tags=driver.find_elements(By.XPATH,"//td[@class='column-3']")
for i in Vedio_tags[0:20]:
    Vedio=i.text
    Vedio_Name.append(Vedio)
    
# scraping Artist_Name from the given page
Artist_tags=driver.find_elements(By.XPATH,"//td[@class='column-3']")
for i in Artist_tags[0:20]:
    Artist=i.text
    Artist_Name.append(Artist)
    
# scraping Upload_date from the given page
Upload_tags=driver.find_elements(By.XPATH,'//td[@align="right"]')
for i in Upload_tags[0:20]:
    Upload=i.text
    Upload_date.append(Upload)
    
# scraping Views from the given page
Views_tags=driver.find_elements(By.XPATH,'//td[@align="center"]')
for i in Views_tags[0:20]:
    Views=i.text
    Views.append(Views)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Question 2

# In[31]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[32]:


driver.get('https://www.bcci.tv/.')


# In[33]:


search_button = driver.find_element(By.XPATH,'//a[@href="https://www.bcci.tv/international/fixtures"]')
search_button.click()


# In[41]:


Match_title=[]
Series_name=[]
Place_name=[]
Date_s=[]
Time_chart=[]


# In[42]:


# scraping Match_title from the given page
Match_tags=driver.find_elements(By.XPATH,'//div[@class="fixture-card-mid d-flex align-items-center justify-content-between"]')
for i in Match_tags[0:3]:
    Match=i.text
    Match_title.append(Match)
    
# scraping Series from the given page
Series_tags=driver.find_elements(By.XPATH,'//span[@class="ng-binding"]')
for i in Series_tags[0:3]:
    Series=i.text
    Series_name.append(Series)
    
# scraping Place from the given page
Place_tags=driver.find_elements(By.XPATH,'//div[@class="fix-place ng-binding ng-scope"]')
for i in Place_tags[0:3]:
    Place=i.text
    Place_name.append(Place)
    
# scraping Date from the given page
Date_tags=driver.find_elements(By.XPATH,'//h5[@class="ng-binding"]')
for i in Date_tags[0:3]:
    Date=i.text
    Date_s.append(Date)
    
# scraping Top_Rank from the given page
Time_tags=driver.find_elements(By.XPATH,'//h5[@class="text-right ng-binding"]')
for i in Time_tags[0:3]:
    Time=i.text
    Time_chart.append(Time)


# In[43]:


print(len(Match_title),len(Series_name),len(Place_name),len(Date_s),len(Time_chart))


# In[44]:


import pandas as pd
df=pd.DataFrame({'match':Match_title,'series':Series_name,'place':Place_name,'date':Date_s,'time':Time_chart})
df


# In[ ]:





# ## Question 3

# In[64]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[65]:


url_4="http://statisticstimes.com/"


# In[66]:


driver.get(url_4)


# In[67]:


Rank=[]
State =[]
GDP=[]
GSDP_Current=[]
GSDP_Previous=[]
Share=[]


# In[68]:


search_button = driver.find_element(By.XPATH,'//button[@class="dropbtn"]')
search_button.click()


# In[69]:


Rank_GSDP=[]
State_name=[]
GSDP_18_19=[]
GSDP_19_20=[]
Share_18_19=[]


# In[70]:


# scraping Rank from the given page
Rank_tags=driver.find_elements(By.XPATH,'//td[@class="data1"]')
for i in Rank_tags[0:33]:
    Rank=i.text
    Rank_GSDP.append(Rank)
    
# scraping State_name from the given page
State_tags=driver.find_elements(By.XPATH,'//td[@class="name"]')
for i in State_tags[0:33]:
    State=i.text
    State_name.append(State)
    
# scraping GSDP_18_19 from the given page
GSDP_tags=driver.find_elements(By.XPATH,'//td[@class="data sorting_1"]')
for i in GSDP_tags[0:33]:
    GSDP=i.text
    GSDP_18_19.append(GSDP)
    
# scraping GSDP_19_20 from the given page
GSDP_tags=driver.find_elements(By.XPATH,'//*[@id="table_id"]/tbody/tr/td[6]')
for i in GSDP_tags[0:33]:
    GSDP=i.text
    GSDP_19_20.append(GSDP)
    
# scraping Share_18_19 from the given page
Share_tags=driver.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[5]")
for i in Share_tags[0:33]:
    Share=i.text
    Share_18_19.append(Share)


# In[71]:


print(len(Rank_GSDP),len(State_name),len(GSDP_18_19),len(GSDP_19_20),len(Share_18_19))


# In[72]:


import pandas as pd
df=pd.DataFrame({'Rank':Rank_GSDP,'State':State_name,'GSDP':GSDP_18_19,'GSDP':GSDP_19_20,'Share':Share_18_19})
df


# In[ ]:





# In[ ]:





# ## Question 4

# In[67]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[68]:


driver.get('https://github.com/')


# In[ ]:


search_button = driver.find_element(By.XPATH,'//button[@class="dropbtn"]')
search_button.click()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




