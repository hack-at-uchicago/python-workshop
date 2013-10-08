import workshop

def extract_lengths(n, tweets_file):
    l = []
    for tweet in workshop.tweets(n, tweets_file):
        l.append(len(tweet["text"]))

    return l


