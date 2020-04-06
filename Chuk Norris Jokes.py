#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib import request
from bs4 import BeautifulSoup
import json


# In[4]:


url = "https://api.icndb.com/jokes"


# In[5]:


html = request.urlopen(url).read()


# In[16]:


print(html)


# In[17]:


json_data = json.loads(html)


# In[18]:


print(json_data)


# In[24]:


ids = [d.get('id') for d in json_data['value'] if d.get('id')]


# In[27]:


jokes = [d.get('joke') for d in json_data['value'] if d.get('joke')]


# In[29]:


final_jokes = jokes[:498]`b


# In[31]:


final_jokes


# In[39]:


filename = 'ChukNorrisJokes.csv'
with open(filename, 'w') as f:
    header_string ="ID,Joke\n"
    f.write(header_string)
    
    j=0
    for i in range(1, 499):
        row_string = "%d,"%(i)
        row_string += final_jokes[j]
        j += 1
        row_string += '\n'
        f.write(row_string)


# In[ ]:




