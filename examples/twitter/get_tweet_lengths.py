#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""
Prints out the lengths of the tweets in the dataset.
"""

import workshop
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

tweets = workshop.get_tweets_text(tfile, n)

for tweet in tweets:
    print len(tweet)

#
# Alternatively:
#
# for tweet in workshop.tweets_text(N):
#    print len(tweet)
#

