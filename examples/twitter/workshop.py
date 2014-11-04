#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013
#

"""Convenience functions for the workshop, mostly to access the tweet dataset."""

import json

def tweets(filename, max_tweets = 0):
    """Generator function to iterate through a tweet dataset.

    This function is used like this:

       for tweet in tweets("tweets.json"):
           print tweet["text"]

    This would print the text of the all the tweets in file
    tweets.json.

    The function also accepts an optional max_tweets parameter
    to limit the number of tweets that will be read. For example,
    this would only print the first 50 tweets:

       for tweet in tweets("tweets.json", max_tweets=50):
           print tweet["text"]

    If instead of iterating through the dataset you want to
    get a list of tweets, use the get_tweets() function instead.

    Parameters:
     filename - Dataset filename
     max_tweets - Maximum number of tweets to load from the dataset.
                  Note that fewer tweets may be returned if n is
                  larger than the number of tweets in the dataset.
                  If this parameters is 0, all the tweets in the file
                  are loaded.

    Returns:
    Each iteration yields a single tweet, represented as a 
    dictionary containing the fields returned by the Twitter API (see 
    https://dev.twitter.com/docs/platform-objects/tweets)
    """

    f = open(filename)
    read = 0

    for line in f:
        tweet = json.loads(line)
        read += 1
        yield tweet
        if max_tweets !=0 and read == max_tweets:
            break

    f.close()
        
    
def tweets_text(filename, max_tweets = 0):
    """Same as the tweets() function, but generating only the text of the tweets

    Parameters:
     filename - Dataset filename
     max_tweets - Maximum number of tweets to load from the dataset
                  Note that fewer tweets may be returned if n is
                  larger than the number of tweets in the dataset.
                  If this parameters is 0, all the tweets in the file
                  are loaded.


    Returns:
    Each iteration yields the text of a single tweet.
    """
    f = open(filename)
    read = 0

    for line in f:
        tweet = json.loads(line)
        read += 1
        yield tweet["text"]
        if max_tweets!= 0 and read == max_tweets:
            break

    f.close()


def get_tweets(filename, max_tweets = 0):
    """Returns a list of tweets from the tweet dataset.

    Parameters:
     filename - Dataset filename
     max_tweets - Maximum number of tweets to load from the dataset
                  Note that fewer tweets may be returned if n is
                  larger than the number of tweets in the dataset.

                  If this parameters is 0, all the tweets in the file
                  are loaded.

                  Take into account that this function will load all the
                  tweets into memory at once, and may perform poorly for
                  large values of max_tweets (or if this parameter is
                  set to 0). Consider using the tweets() generator
                  function instead.

    Returns:
    List of tweets. Each tweet is a dictionary containing the
    fields returned by the Twitter API (see 
    https://dev.twitter.com/docs/platform-objects/tweets)
    """
    return [t for t in tweets(filename, max_tweets)]


def get_tweets_text(filename, max_tweets = 0):
    """Returns a list of strings, with the text of tweets from the dataset.

     filename - Dataset filename
     max_tweets - Maximum number of tweets to load from the dataset
                  Note that fewer tweets may be returned if n is
                  larger than the number of tweets in the dataset.

                  If this parameters is 0, all the tweets in the file
                  are loaded.

                  Take into account that this function will load all the
                  tweets into memory at once, and may perform poorly for
                  large values of max_tweets (or if this parameter is
                  set to 0). Consider using the tweets() generator
                  function instead.

    Returns:
    List of strings (the text of the tweets)
    """
    return [t for t in tweets_text(filename, max_tweets)]


def get_hashtags(tweet):
    """Extracts hashtags from a tweet

    Parameters:
      tweet - Dictionary with tweet data, as returned by tweets(), tweets_text()
              get_tweets(), or get_tweets_text()

    Returns:
      List of strings with hashtags (if any) in the tweet.
    """
    return [h["text"] for h in tweet["entities"]["hashtags"]]
