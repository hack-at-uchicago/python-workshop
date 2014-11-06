#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""
Compute the average length and standard deviation of the tweets
"""

import workshop
import math
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

length_sum = 0.0
lengths = []

for tweet in workshop.tweets_text(tfile, n):
    length_sum += len(tweet)
    lengths.append(len(tweet))

avg = length_sum / n

stdev_sum = 0
for length in lengths:
    stdev_sum += (length - avg)**2

stdev = math.sqrt(stdev_sum/n)

print "The average length is %.2f" % avg
print "The standard deviation is %.2f" % stdev


