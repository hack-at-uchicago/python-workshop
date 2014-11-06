#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""Function example"""

import workshop

def extract_lengths(tweets_file, n):
    """Extract the lengths of the tweets in a tweet dataset

    Parameters:
     tweets_file - Dataset filename
     n - Maximum number of tweets to load from the dataset
         Note that fewer tweets may be returned if n is
         larger than the number of tweets in the dataset.

    Returns:
    List of integers (lengths)
    """
    l = []
    for tweet in workshop.tweets(tweets_file, n):
        l.append(len(tweet["text"]))

    return l

def extract_values(n, tweets_file, field):
    # YOUR CODE HERE

    # Remember to update the return value
    return []

def compute_frequencies(l):
    # YOUR CODE HERE

    # Remember to update the return value
    return []

