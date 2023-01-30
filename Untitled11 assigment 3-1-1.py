#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# ## Question 4

# In[15]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[16]:


driver.get("https://www.flipkart.com/")


# In[17]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'_3704LK')
designation.send_keys('smartphone')


# In[18]:


Brand_Name=[]
Colour=[]
Storage_RAM_ROM=[]
Display_size_Resolution=[]
P_F_Camera=[]
Processor_And_Cores=[]
Battery_size=[]
Price_p=[]
Product_URL=[]


# In[19]:


# scraping brand from the given page
Brand_tags=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
for i in Brand_tags[0:24]:
    Brand=i.text
    Brand_Name.append(Brand)


# In[20]:


# scraping Storage RAM ROM from the given page
Storage_tags=driver.find_elements(By.XPATH,"//ul[@class='_1xgFaf']//li[1]")
for i in Storage_tags[0:24]:
    Storage=i.text
    Storage_RAM_ROM.append(Storage)


# In[21]:


# scraping Display_size_Resolution from the given page
Display_tags=driver.find_elements(By.XPATH,"//ul[@class='_1xgFaf']//li[2]")
for i in Display_tags[0:24]:
    Display=i.text
    Display_size_Resolution.append(Display)


# In[22]:


# scraping P_F_Camera from the given page
P_tags=driver.find_elements(By.XPATH,"//ul[@class='_1xgFaf']//li[3]")
for i in P_tags[0:24]:
    P=i.text
    P_F_Camera.append(P)


# In[23]:


# scraping Processor_And_Cores from the given page
Processor_tags=driver.find_elements(By.XPATH,"//ul[@class='_1xgFaf']//li[5]")
for i in Processor_tags[0:24]:
    Processor=i.text
    Processor_And_Cores.append(Processor)


# In[24]:


# scraping Battery from the given page
Battery_tags=driver.find_elements(By.XPATH,"//ul[@class='_1xgFaf']//li[4]")
for i in Battery_tags[0:24]:
    Battery=i.text
    Battery_size.append(Battery)


# In[25]:


# scraping Price from the given page
Price_tags=driver.find_elements(By.XPATH,"//div[@class='_30jeq3 _1_WHN1']")
for i in Price_tags[0:24]:
    Price=i.text
    Price_p.append(Price)


# In[26]:


print(len(Brand_Name),len(Storage_RAM_ROM),len(Display_size_Resolution),len(P_F_Camera),len(Processor_And_Cores),len(Battery_size),len(Price_p))


# In[27]:


import pandas as pd
df=pd.DataFrame({'Brand':Brand_Name,'Storage':Storage_RAM_ROM,'Display':Display_size_Resolution,'P':P_F_Camera,'Processor':Processor_And_Cores,'Battery':Battery_size,'Price':Price_p})
df


# In[ ]:





# ## Question 1

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[25]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[26]:


driver.get('https://www.amazon.in/')


# In[27]:


search_bar=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search_bar.send_keys('guitars')
search_button = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search_button.click()


# In[28]:


product_Name=[]


# In[31]:


# scraping product from the given page
product_tags=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]')
for i in product_tags[0:20]:
    product=i.text
    product_Name.append(product)


# In[32]:


print(len(product_Name))


# In[35]:


import pandas as pd
df=pd.DataFrame({'product':product_Name})
df


# In[ ]:





# ## Question 2

# In[2]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[3]:


driver.get('https://www.amazon.in/')


# In[4]:


search_bar=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search_bar.send_keys('guitars')
search_button = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search_button.click()


# In[12]:


start_page = 0
end_page = 3
for page in range(start_page,end_page+1):
    try:
        page_urls = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-no-outline"]')
        for url in page_urls:
        url = url.get_attribute('href')   


# In[ ]:





# ## Question 6

# In[33]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[34]:


driver.get('https://trak.in/india-startup-funding-investment-2015/')


# In[35]:


Dates_d=[]
Company_Name=[]
Industry_type=[]
Investor_Name=[]
Investment_Type=[]
Amount_inv=[]


# In[36]:


# scraping Company from the given page
Company_tags=driver.find_elements(By.XPATH,"//td[@class='column-3']")
for i in Company_tags[0:20]:
    Company=i.text
    Company_Name.append(Company)
    
# scraping Industry from the given page
Industry_tags=driver.find_elements(By.XPATH,"//td[@class='column-4']")
for i in Industry_tags[0:20]:
    Industry=i.text
    Industry_type.append(Industry)
    
# scraping Dates from the given page
Dates_tags=driver.find_elements(By.XPATH,"//td[@class='column-2']")
for i in Dates_tags[0:20]:
    Dates=i.text
    Dates_d.append(Dates)
    
# scraping Investor Name from the given page
Investor_tags=driver.find_elements(By.XPATH,"//td[@class='column-7']")
for i in Investor_tags[0:20]:
    Investor=i.text
    Investor_Name.append(Investor)
    
# scraping Investment Type the given page
Investment_tags=driver.find_elements(By.XPATH,"//td[@class='column-8']")
for i in Investment_tags[0:20]:
    Investment=i.text
    Investment_Type.append(Investment)
    
# scraping Amount from the given page
Amount_tags=driver.find_elements(By.XPATH,"//td[@class='column-9']")
for i in Amount_tags[0:20]:
    Amount=i.text
    Amount_inv.append(Amount)


# In[37]:


print(len(Company_Name),len(Industry_type),len(Dates_d),len(Investor_Name),len(Investment_Type),len(Amount_inv))


# In[38]:


import pandas as pd
df=pd.DataFrame({'Company':Company_Name,'Industry':Industry_type,'Dates':Dates_d,'Investor':Investor_Name,'Investment':Investment_Type,'Amount':Amount_inv})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Question 5

# In[ ]:





# In[3]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[15]:


# opening google maps
driver.get("https://www.google.co.in/maps")
time.sleep(3)

search_button = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search_button.click()                                                            
time.sleep(2)
search.send_keys('[class="DgCNMb"]')
button = driver.find_element_by_id("searchbox-searchbutton")               
button.click()                                                             
time.sleep(3)


# In[5]:


try:
    url_string = driver.current_url
    print("URL Extracted: ", url_string)
    lat_lng = re.findall(r'@(.*)data',url_string)
    if len(lat_lng):
        lat_lng_list = lat_lng[0].split(",")
        if len(lat_lng_list)>=2:
            lat = lat_lng_list[0]
            lng = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(lat, lng))

except Exception as e:
        print("Error: ", str(e)


# In[ ]:





# ## Question 7

# In[35]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[36]:


url="https://www.digit.in/top-products/best-gaming-laptops-40.html"


# In[37]:


driver.get(url)


# In[38]:


Brand_name=[]
Product_Description=[]
Specification_laptop=[]
Price_laptop=[]


# In[39]:


# scraping brand from the given page
Brand_tags=driver.find_elements(By.XPATH,'//div[@class="left_side"]')
for i in Brand_tags[0:10]:
    Brand=i.text
    Brand_name.append(Brand)
    
# scraping Products Description from the given page
Product_tags=driver.find_elements(By.XPATH,'//div[@class="tptn-prod-desc"]')
for i in Product_tags[0:10]:
    Product=i.text
    Product_Description.append(Product)
    
# scraping Specification from the given page
Specification_tags=driver.find_elements(By.XPATH,"//div[@class='Section-center']")
for i in Specification_tags[0:10]:
    Specification=i.text
    Specification_laptop.append(Specification)
    
# scraping Price from the given page
Price_tags=driver.find_elements(By.XPATH,"//td[@class='smprice']")
for i in Price_tags[0:10]:
    Price=i.text
    Price_laptop.append(Price)


# In[40]:


print(len(Brand_name),len(Product_Description),len(Specification_laptop),len(Price_laptop))


# In[44]:


import pandas as pd
df=pd.DataFrame({'Brand':Brand_name,'product':Product_Description,'specification':Specification_laptop,'price':Price_laptop})
df


# In[ ]:





# ## Questions 3

# In[51]:


# let's first connect to the web driver
driver = webdriver.Chrome("Downloads\chromedriver.exe")


# In[52]:


driver.get('https://images.google.com/')


# In[53]:


# enterning the naukri page on automated chrome browser

designation=driver.find_element(By.CLASS_NAME,'gLFyf')
designation.send_keys('fruits images')


# In[39]:


search_button = driver.find_elements(By.XPATH,'//input[@title="Search"]')
search_button.click()


# In[ ]:





# In[ ]:




