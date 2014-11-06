#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""
Generates a histogram of the tweet lengths
"""

import matplotlib.pyplot as plt
from functions import extract_lengths
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

lengths = extract_lengths(tfile, n)

# Use Matplotlib to generate histogram
plt.hist(lengths, bins=50)

plt.xlabel('Lengths')
plt.ylabel('# Tweets')
plt.title('Distribution of tweet lengths')
plt.show()

