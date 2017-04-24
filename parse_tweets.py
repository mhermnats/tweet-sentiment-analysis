
# coding: utf-8

# In[36]:

import numpy as np
import pandas as pd
import codecs
import re


# In[37]:

fname = 'tweets.txt'

def get_list_of_tweets(fname):
    with codecs.open(fname, "r",encoding='utf-8', errors='ignore') as fdata:
        tweets = []
        content = fdata.readlines()
        tweetline = ""
        for line in content:
            if line[:2] == 'RT':
                if tweetline:
                    tweets.append(tweetline[2:])
                tweetline = line
            else:
                tweetline = tweetline + line
        if tweetline:
            tweets.append(tweetline[2:])
    return tweets

tweets = get_list_of_tweets(fname)
tweets = [re.sub(r"http\S+", "", tweet).rstrip().replace('\n', ' ').replace('\r', '') for tweet in tweets]


# In[38]:

df = pd.DataFrame()
df['labels'] = np.array([0 for i in range(len(tweets))])
df["tweets"] = np.array(tweets)


# In[39]:

df.to_csv('fastText/data/test-tweets.csv', header=False, index = False)
print("Successfully created the csv file")

# In[ ]:



