import workshop
import operator

from functions import extract_values, compute_frequencies

N = 20000 # Number of tweets to use
TWEETS_FILE = "top_tweets.json"  # Use the "top tweets" dataset instead

for field in ["favorite_count", "retweet_count"]:
    print "%s Frequencies" % field
    l = extract_values(N, TWEETS_FILE, field)
    freqs = compute_frequencies(l)
    freqs = freqs.items()
    freqs.sort(key = operator.itemgetter(1), reverse = True)
    for value, count in freqs[:10]:
        print value, count    
    print

