#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013
#
# Convenience functions for the workshop,
# mostly to access the tweet dataset.

import json

# Generator function to iterate through the tweets 
# in the dataset.
#
# This function is used like this:
#
#    for tweet in tweets(50, "tweets.json"):
#        print tweet["text"]
#
# This would print the text of the first 50 tweets in file
# tweets.json.
#
# If instead of iterating through the dataset you want to
# get a list of tweets, use the get_tweets() function instead.
#
# Parameters:
#  n - Maximum number of tweets to load from the dataset
#      Note that fewer tweets may be returned if n is
#      larger than the number of tweets in the dataset.
#  filename - Dataset filename
#
# Returns:
# Each iteration yields a single tweet, represented as a 
# dictionary containing the fields returned by the Twitter API (see 
# https://dev.twitter.com/docs/platform-objects/tweets)
def tweets(n, filename):
    f = open(filename)
    read = 0

    for line in f:
        tweet = json.loads(line)
        read += 1
        yield tweet
        if read == n:
            break
        
    
# Same as the tweets() function, but generating only 
# the text of the tweets
#
# Parameters:
#  n - Maximum number of tweets to load from the dataset
#      Note that fewer tweets may be returned if n is
#      larger than the number of tweets in the dataset.
#  filename - Dataset filename
#
# Returns:
# Each iteration yields the text of a single tweet.
def tweets_text(n, filename):
    f = open(filename)
    read = 0

    for line in f:
        tweet = json.loads(line)
        read += 1
        yield tweet["text"]
        if read == n:
            break


# Returns a list of tweets from the tweet dataset.
#
# Parameters:
#  n - Maximum number of tweets to load from the dataset
#      Note that fewer tweets may be returned if n is
#      larger than the number of tweets in the dataset.
#      Take into account that this function will load all the
#      tweets into memory at once, and may perform poorly for
#      large values of n. Consider using the tweets() generator
#      function instead.
#  filename - Dataset filename
#
# Returns:
# List of tweets. Each tweet is a dictionary containing the
# fields returned by the Twitter API (see 
# https://dev.twitter.com/docs/platform-objects/tweets)
def get_tweets(n, filename):
    return [t for t in tweets(n,filename)]


# Returns a list of strings, with the text of tweets from the dataset.
#
# Parameters:
#  n - Maximum number of tweets to load from the dataset
#      Note that fewer tweets may be returned if n is
#      larger than the number of tweets in the dataset.
#      Take into account that this function will load all the
#      tweets into memory at once, and may perform poorly for
#      large values of n. Consider using the tweets() generator
#      function instead.
#  filename - Dataset filename
#
# Returns:
# List of strings (the text of the tweets)
def get_tweets_text(n, filename):
    return [t for t in tweets_text(n,filename)]


# Extracts hashtags from a tweet
#
# Parameters:
#   tweet - Dictionary with tweet data (as returned by load_tweets)
#
# Returns:
#   List of strings with hashtags (if any) in the tweet.
def get_hashtags(tweet):
    return [h["text"] for h in tweet["entities"]["hashtags"]]
