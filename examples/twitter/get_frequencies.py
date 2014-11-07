#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""
Prints out the ten most-frequent values for the
"favorite_count" and "retweet_count" fields in a
tweet dataset
"""

import workshop
import operator
import sys

# For this script to run, you need to implement the extract_values
# and compute_frequencies values in exercise_functions.py
from functions import extract_values, compute_frequencies

tfile = sys.argv[1]
n = int(sys.argv[2])

for field in ["favorite_count", "retweet_count"]:
    print "Top 10 frequencies of %s" % field
    l = extract_values(tfile, n, field)
    freqs = compute_frequencies(l)
    freqs = freqs.items()
    freqs.sort(key = operator.itemgetter(1), reverse = True)
    for value, count in freqs[:10]:
        print value, count    
    print

