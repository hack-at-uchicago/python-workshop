#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014


"""
Prints out the frequency of lengths for the
tweet dataset.
"""

import workshop
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

lengths = {}

for tweet in workshop.tweets_text(tfile, n):
    length = len(tweet)
    if lengths.has_key(length):
        lengths[length] += 1
    else:
        lengths[length] = 1
    # Or, use the setdefault method

length_freq = lengths.items()
length_freq.sort()

for length, count in length_freq:
    print length, count
