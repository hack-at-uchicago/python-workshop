#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013

"""
Find the top ten hashtags in the dataset
"""

import workshop
import operator
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

hashtags = {}

for tweet in workshop.tweets(n, tfile):
    tweet_hashtags = workshop.get_hashtags(tweet)
    for hashtag in tweet_hashtags:
        if hashtags.has_key(hashtag):
            hashtags[hashtag] += 1
        else:
            hashtags[hashtag] = 1
        # Or, use the setdefault method

hashtags_freq = hashtags.items()
hashtags_freq.sort(key = operator.itemgetter(1), reverse = True)

for hashtag, count in hashtags_freq[:10]:
    print "#" + hashtag, count
