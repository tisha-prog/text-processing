#!/usr/bin/env python
# coding: utf-8

# In[79]:


import nltk
import os
import nltk.corpus
print(os.listdir(nltk.data.find("corpora")))


# # data processing

# ### 1.Tokenization Process 

# In[46]:


txt="""This clustering approach assumes data is composed of distributions, such as Gaussian distributions. In Figure 3, the distribution-based algorithm clusters data into three Gaussian distributions. As distance from the distribution's center increases, the probability that a point belongs to the distribution decreases. The bands show that decrease in probability. When you do not know the type of distribution in your data, you should use a different algorithm."""

from nltk.tokenize import word_tokenize
txt_token = word_tokenize(txt)
txt_token


# In[4]:


type(txt) #data type of text 


# In[8]:


len(txt_token) #length of tokenized text


# ## 2.Stemming 

# In[48]:


#import porterStemmer 
from nltk.stem import PorterStemmer
#Initialise the porterStemmer 
ps= PorterStemmer()
l=[]
for t in txt_token:
    l.append(ps.stem(t))
txt_token=l
txt_token


# # 3.Lemmatization

# ### Punctuations

# In[49]:


import nltk
#import wordnetlemmatizer database
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer

# Init the Wordnet Lemmatizer
wl=WordNetLemmatizer()
nltk.download('stopwords')

#removing the punctuations
punctuations="?:;',!."
for i in txt_token:
    if i in punctuations:
        txt_token.remove(i)
txt_token 


# In[50]:


#the length of text data reduces as we clean it more 
#68 from 77 after removing punctuations
len(txt_token)  


# In[ ]:


#A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore,
#when indexing entries for searching and when retrieving them as the result of a search query.


# ### Stopwords

# In[41]:


import nltk
from nltk.corpus import stopwords
#The list of stopwords can be modified the list by adding words in the english .txt. file in the stopwords directory.
#179 pre-defined stopwords
print(stopwords.words('english'))


# In[53]:


#
import nltk
from nltk.corpus import stopwords
#removing stopwords
s=stopwords.words('english')
for x in txt_token:
    if x in s:
        txt_token.remove(x)
txt_token


# In[54]:


#41 from 68 after removing stopwords
len(txt_token)

