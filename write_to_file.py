
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import codecs
import re


# In[24]:

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


# In[25]:

df = pd.DataFrame()
df["tweets"] = np.array(tweets)


# In[11]:

def get_label(string):
    return int(string[-1])


# In[41]:

file = 'fastText/file_output/tweet.test.predict'

def parse_file(file):
    pos_tweets = []
    pos_rank = []
    neg_tweets = []
    neg_rank = []
    with codecs.open(file, "r",encoding='utf-8', errors='ignore') as fdata:
            content = fdata.readlines()
            index = 0
            for line in content:
                label, rank = line.split()
                label = get_label(label)
                if label == 1:
                    pos_tweets.append(tweets[index])
                    pos_rank.append(rank)
                elif label == 0:
                    neg_tweets.append(tweets[index])
                    neg_rank.append(rank)
                index += 1
    pos_tweets = np.array(pos_tweets)
    pos_rank = np.array(pos_rank)
    neg_tweets = np.array(neg_tweets)
    neg_rank = np.array(neg_rank)
    neg = pd.DataFrame()
    neg['tweet'] = neg_tweets
    neg['rank'] = neg_rank
    pos = pd.DataFrame()
    pos['tweet'] = pos_tweets
    pos['rank'] = pos_rank
    return pos, neg


# In[45]:

p, n = parse_file(file)


# In[46]:

positive = p.sort('rank', ascending=False).reset_index()[['tweet', 'rank']]


# In[47]:

negative = n.sort('rank', ascending=False).reset_index()[['tweet', 'rank']]


# In[49]:

with codecs.open('positive.txt', "w",encoding='utf-8', errors='ignore') as fdata:
    fdata.write(positive.to_string(index=False))
print("Successfully created positive.txt file")

# In[50]:

with codecs.open('negative.txt', "w",encoding='utf-8', errors='ignore') as fdata:
    fdata.write(negative.to_string(index=False))
print("Successfully created negative.txt file")


# In[ ]:



