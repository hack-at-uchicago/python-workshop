#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""
Prints some information for each tweet in the dataset
"""

import workshop
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

for tweet in workshop.tweets(tfile, n):
    print "User:", tweet["user"]["screen_name"]
    print "Text:", tweet["text"]
    print "Date:", tweet["created_at"]
    print "Retweets:", tweet["retweet_count"]
    print "Hashtags:", tweet["entities"]["hashtags"]
    print


