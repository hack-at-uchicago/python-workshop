#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013
#
# Convenience functions for the workshop,
# mostly to access the tweet dataset.

import json

# Loads tweets from the dataset.
# By default, it will look for a file called tweets.json.
#
# Parameters:
#  n - Maximum number of tweets to load from the dataset
#      Note that fewer tweets may be returned if n is
#      larger than the number of tweets in the dataset.
#  filename - Dataset filename
#
# Returns:
# List of tweets. Each tweet is a dictionary containing the
# fields returned by the Twitter API (see 
# https://dev.twitter.com/docs/platform-objects/tweets)
def tweets(n, filename = "tweets.json"):
    f = open(filename)
    read = 0

    for line in f:
        tweet = json.loads(line)
        read += 1
        yield tweet
        if read == n:
            break
        
    
# Same as load_tweets, but returning a list of strings
# (with the texts of the tweets)
def tweets_text(n, filename = "tweets.json"):
    f = open(filename)
    read = 0

    for line in f:
        tweet = json.loads(line)
        read += 1
        yield tweet["text"]
        if read == n:
            break

# Extracts hashtags from a tweet
#
# Parameters:
#   tweet - Dictionary with tweet data (as returned by load_tweets)
#
# Returns:
#   List of strings with hashtags (if any) in the tweet.
def get_hashtags(tweet):
    return [h["text"] for h in tweet["entities"]["hashtags"]]
