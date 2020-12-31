#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy


# In[3]:


class wikispider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M']
    def parse(self, response):
        filename = 'wiki.html'
        with open(filename, 'wb') as f:
            f.write(response.body)


# In[5]:





# In[ ]:




