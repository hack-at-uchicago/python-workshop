#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""
Compute the average length of the tweets
"""

import workshop
import math
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

length_sum = 0.0

for tweet in workshop.tweets_text(tfile, n):
    length_sum += len(tweet)

avg = length_sum / n

print "The average length is %.2f" % avg


