import workshop

N = 10000 # Number of tweets to use

lengths = {}

for tweet in workshop.tweets_text(N):
    length = len(tweet)
    if lengths.has_key(length):
        lengths[length] += 1
    else:
        lengths[length] = 1
    # Or, use the setdefault method

length_freq = lengths.items()
length_freq.sort()

for length, count in length_freq:
    print length, count
