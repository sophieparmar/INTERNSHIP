#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[7]:


url = "https://www.imdb.com/india/top-rated-indian-movies/"


# In[8]:


page = requests.get(url)
page          


# In[9]:


## display the page source code
page.content


# In[10]:


soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[11]:


# scrap movie names
scraped_movies = soup.find_all('td', class_="titleColumn")
scraped_movies


# In[12]:


# parse movie names
movies = []
for movie in scraped_movies:
    movie = movie.get_text().replace('\n', "")
    movie = movie.strip(" ")
    movies.append(movie)
movies


# In[13]:


# scrap rating for movies
scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')
scraped_ratings


# In[14]:


# parse ratings
ratings = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n', '')
    ratings.append(rating)
ratings


# In[15]:


# scrap movie release year
scraped_release = soup.find_all('span', class_='secondaryInfo')
scraped_release


# ## # scrap movie release year

# In[16]:


data = pd.DataFrame()
data['Movie Names'] = movies
data['Ratings'] = ratings
data.head(100)


# In[ ]:


data.to_csv('IMDB Top Movies.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




