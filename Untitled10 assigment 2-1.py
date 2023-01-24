#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[31]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[32]:


driver.get("https://www.naukri.com/")


# In[33]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Analyst')


# In[34]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[37]:


# scraping job title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
# scraping job Location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
# scraping job Company from the given page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
# scraping job Experience from the given page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[38]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[39]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# In[ ]:





# ## Question 2

# In[40]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[41]:


driver.get("https://www.naukri.com/")


# In[42]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Scientist')


# In[43]:


job_title=[]
job_location=[]
company_name=[]


# In[44]:


# scraping job title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
# scraping job Location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
# scraping job Company from the given page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[45]:


print(len(job_title),len(job_location),len(company_name))


# In[46]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name})
df


# In[ ]:





# ## Question 3

# In[77]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[78]:


driver.get("https://www.naukri.com/")


# In[79]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Scientist')


# In[83]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]
salary_required=[]


# In[84]:


# scraping job title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
# scraping job Location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
# scraping job Company from the given page
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
# scraping job Experience from the given page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)
    
# scraping job salary from the given page
salary_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft "]')
for i in salary_tags[0:10]:
    salary=i.text
    salary_required.append(salary)


# In[85]:


print(len(job_title),len(job_location),len(company_name),len(experience_required),len(salary_required))


# In[87]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required,'Salary':salary_required})
df


# In[ ]:





# ## Question 4

# In[172]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[173]:


driver.get("https://www.flipkart.com/")


# In[174]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'_3704LK')
designation.send_keys('sunglasses')


# In[175]:


brand_name=[]
Product_Description=[]
Price_required=[]


# In[176]:


# scraping job brand from the given page
brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:10]:
    brand=i.text
    brand_name.append(brand)

# scraping job product from the given page
product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_tags[0:10]:
    product=i.text
    Product_Description.append(product)
    
# scraping job price from the given page
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags[0:10]:
    price=i.text
    Price_required.append(price)


# In[177]:


print(len(brand_name),len(Product_Description),len(Price_required))


# In[178]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_name,'Product':Product_Description,'Price':Price_required})
df


# In[ ]:





# ## Question 5

# In[214]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[223]:


driver.get("https://www.flipkart.com/")


# In[224]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'_3704LK')
designation.send_keys('apple iphone 11 black 64')


# In[225]:


Rating_name=[]
Review_summary=[]
Full_review=[]


# In[226]:


# scraping job Rating from the given page
Rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in Rating_tags[0:1]:
    Rating=i.text
    Rating_name.append(Rating)
    
# scraping job Review summary from the given page
Review_tags=driver.find_elements(By.XPATH,'//div[@class="_2QKOHZ"]')
for i in Review_tags[0:10]:
    Review=i.text
    Review_summary.append(Review)
    
# scraping job full review summary from the given page
Full_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in Full_tags[0:10]:
    Full=i.text
    Full_review.append(Full)


# In[227]:


print(len(Rating_name),len(Review_summary),len(Full_review))


# In[228]:


import pandas as pd
df=pd.DataFrame({'Rating':Rating_name,'Review':Review_summary,'Full':Full_review})
df


# In[ ]:





# ## Question 6

# In[150]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[151]:


driver.get("https://www.flipkart.com/")


# In[152]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'_3704LK')
designation.send_keys('sneaker')


# In[153]:


brand_name=[]
Product_Description=[]
Price_required=[]


# In[154]:


# scraping job brand from the given page
brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:10]:
    brand=i.text
    brand_name.append(brand)

# scraping job product from the given page
product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_tags[0:10]:
    product=i.text
    Product_Description.append(product)
    
# scraping job price from the given page
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags[0:10]:
    price=i.text
    Price_required.append(price)


# In[155]:


print(len(brand_name),len(Product_Description),len(Price_required))


# In[156]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_name,'Product':Product_Description,'Price':Price_required})
df


# In[ ]:





# ## Question 7

# In[229]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[230]:


driver.get("https://www.amazon.in/")


# In[240]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'utf-8')
designation.send_keys('Intel Core i7')


# In[ ]:





# ## Question 8

# In[248]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[249]:


driver.get("https://www.azquotes.com/")


# In[250]:


Quote_information=[]
Author_name=[]


# In[251]:


# scraping job quote from the given page
Quote_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in Quote_tags[0:100]:
    Quote=i.text
    Quote_information.append(Quote)
    
# scraping job Author from the given page
Author_tags=driver.find_elements(By.XPATH,'//a[@class="name"]')
for i in Author_tags[0:100]:
    Author=i.text
    Author_name.append(Author)


# In[252]:


print(len(Quote_information),len(Author_name))


# In[253]:


import pandas as pd
df=pd.DataFrame({'Quote':Quote_information,'Author':Author_name})
df


# In[ ]:




