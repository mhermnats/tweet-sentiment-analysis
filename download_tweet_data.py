
# coding: utf-8

# In[17]:

import numpy as np
import pandas as pd
import urllib
import zipfile
import os


# In[12]:

url = 'http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip'
file_name = 'fastText/data/tweet.zip'

# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, file_name)
print("Successfully downloaded the zip file")


# In[13]:

directory = 'fastText/data/'
zip_ref = zipfile.ZipFile(file_name, 'r')
zip_ref.extractall(directory)
zip_ref.close()
print("Successfully unziped the zip file")


# In[18]:

os.remove(file_name)
print("Successfully deleted the zip file")


# In[14]:

df = pd.read_csv('fastText/data/Sentiment Analysis Dataset.csv', error_bad_lines=False)
data = df[['Sentiment', 'SentimentText']]
shuffled_data = data.sample(frac=1).reset_index(drop=True)


# In[15]:

n = len(shuffled_data)
train_size = int(n * 0.95)
test_size = n - train_size
train = shuffled_data.head(train_size).reset_index(drop=True)
test = shuffled_data.tail(test_size).reset_index(drop=True)


# In[16]:

train.to_csv('fastText/data/train.csv', header=False, index=False)
print("Successfully created the training set")
test.to_csv('fastText/data/test.csv', header=False, index=False)
print("Successfully created the testing set")

os.remove('fastText/data/Sentiment Analysis Dataset.csv')
print("Successfully deleted the original csv file")

# In[ ]:



