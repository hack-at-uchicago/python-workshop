#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013

"""Function example"""

import workshop

def extract_lengths(n, tweets_file):
    """Extract the lengths of the tweets in a tweet dataset

    Parameters:
     n - Maximum number of tweets to load from the dataset
         Note that fewer tweets may be returned if n is
         larger than the number of tweets in the dataset.
     tweets_file - Dataset filename

    Returns:
    List of integers (lengths)
    """
    l = []
    for tweet in workshop.tweets(n, tweets_file):
        l.append(len(tweet["text"]))

    return l


