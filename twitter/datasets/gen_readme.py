#!/bin/python

import sys

sys.path.append('../../examples/twitter/')

import workshop
from datetime import datetime

def find_date_range(filename):

    min_date = datetime.now()
    max_date = datetime(1, 1, 1, 0, 0, 0)

    n = 0

    for tweet in workshop.tweets(filename):
        d = datetime.strptime(tweet["created_at"],"%a %b %d %H:%M:%S +0000 %Y")

        if d > max_date:
            max_date = d
        
        if d < min_date:
            min_date = d

        n += 1

    return n, min_date, max_date

README = """This file contains two Twitter datasets.

Each dataset is a text file, with one tweet
per line (encoded in JSON). Each tweet
contains the information returned by the
Twitter API (see https://dev.twitter.com/docs/platform-objects/tweets).
Note that the file itself is not a valid JSON 
file (it must be read line by line, and each 
line should be decoded separately).

100K TWEETS
-----------
"tweets.json" contains 100,000 tweets in 
English collected from the public stream.

These tweets span the following times:

First tweet: {0} (UTC)
Last tweet:  {1} (UTC)


TOP TWEETERS
------------
"top_tweets.json" contains {2:,} tweets
from the 100 most-followed Twitter users.
For each user, the dataset includes at
most 200 of their most recent tweets. Take
into account that some of these users
have less than 200 tweets.

These tweets span the following times:

First tweet: {3} (UTC)
Last tweet:  {4} (UTC)"""

n_all, min_date_all, max_date_all = find_date_range("tweets.json")
n_top, min_date_top, max_date_top = find_date_range("top_tweets.json")

print README.format(min_date_all, max_date_all, n_top, min_date_top, max_date_top)


