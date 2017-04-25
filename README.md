# tweet-sentiment-analysis

Tweet Sentiment Analysis using Facbook's fastText.

## Requirements

**fastText** builds on modern Mac OS and Linux distributions.
Since it uses C++11 features, it requires a compiler with good C++11 support.
These include :

* (gcc-4.6.3 or newer) or (clang-3.3 or newer)

Compilation is carried out using a Makefile, so you will need to have a working **make**.
For the word-similarity evaluation script you will need:

* python 2.6 or newer
* numpy & scipy

## Building tweet-sentiment-analysis

To get the files do the following:

```
$ git clone https://github.com/mhermnats/tweet-sentiment-analysis.git
```

Then, navigate to the root directory of this repo. In other words `pwd` should end with `/tweet-sentiment-analysis`.

In order to download the training dataset, shuffle it and split it into the train and test sets, use the following:

```
$ python download_tweet_data.py
```

The ratio of training/test set sizes is 95 to 5 by default. You can change this by modifying train_size in the download_tweet_data.py file. You can find more information about the dataset I am using in the Reference. It contains nearly 1.5m tweets with 0 or 1 labels, where 0 corresponds to negative and 1 to positive sentiments.

In order to build `tweet-sentiment-analysis` and `fastText`, use the following:

```
$ cd fastText
$ make
```

Now, if you want to see the precision and recall for the test set, use these commands:

Make sure you are in the `/fastText` directory.

```
$ bash tweet-classify-results.sh
```

This will do the necessary parsing and shuffle for your data, then will train the model on the training set and do the corresponding predictions on the testing set. You can find the predictions in `fastText/output`. 

You can expect almost 82% precision and recall for this datasets. 

## Text classification

Now we can classify our own tweets using the above mentioned dataset to get tweet sentiments. For this you need to dump your tweets into tweets.txt file in the following way:

Each tweet needs to start with 'RT ' and preferable have a newline charater at the end of it. You can have a look at the tweets.txt file for your reference and/or modify parse_tweets.py file for your own case. 

So, to parse the tweets and make a test set, run the following command(this should be done in the root repo):

```
$ python parse_tweets.py
```

Now you can classify your tweets navigating to the `fastText` directory and do the following:

```
$ bash tweet-classify-file.sh
```

This will find and put the corresponding predictions and their probabilities in `fastText/file_output`. In order to get the positive and negative tweets in positive.txt and negative.txt files you need to run the following from the root directory:

```
$ python write_to_file.py
```

After this command, you can find the tweets and their probabilities in the above-mentioned files, the most probable predictions appearing first. 

## References

Please cite [1](#bag-of-tricks-for-efficient-text-classification) if using this text classification. Also, check out https://github.com/facebookresearch/fastText GitHub repo for more information about the training and classifying the data sets. 

### Bag of Tricks for Efficient Text Classification

[1] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, [*Bag of Tricks for Efficient Text Classification*](https://arxiv.org/abs/1607.01759)

```
@article{joulin2016bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.01759},
  year={2016}
}
```

(\* These authors contributed equally.)


###  Twitter Sentiment Analysis Dataset 

You can find more about the dataset in here:

http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/








