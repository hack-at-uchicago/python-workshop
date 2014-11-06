#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

import workshop

def extract_lengths(n, tweets_file):
    l = []
    for tweet in workshop.tweets(tweets_file, n):
        l.append(len(tweet["text"]))

    return l

def extract_values(tweets_file, n, field):
    l = []
    for tweet in workshop.tweets(tweets_file, n):
        l.append(tweet[field])

    return l

def compute_frequencies(l):
    freqs = {}
    for v in l:
        freqs[v] = freqs.setdefault(v, 0) + 1

    return freqs


