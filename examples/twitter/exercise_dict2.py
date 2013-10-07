import workshop
import operator

N = 50000 # Number of tweets to use

tweets = workshop.load_tweets(N)

hashtags = {}

for tweet in tweets:
    tweet_hashtags = workshop.get_hashtags(tweet)
    for hashtag in tweet_hashtags:
        if hashtags.has_key(hashtag):
            hashtags[hashtag] += 1
        else:
            hashtags[hashtag] = 1
        # Or, use the setdefault method

hashtags_freq = hashtags.items()
hashtags_freq.sort(key = operator.itemgetter(1), reverse = True)

for hashtag, count in hashtags_freq[:10]:
    print "#" + hashtag, count
