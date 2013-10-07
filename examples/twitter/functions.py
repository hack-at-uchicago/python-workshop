import workshop

def extract_values(n, tweets_file, field):
    l = []
    for tweet in workshop.tweets(n, tweets_file):
        l.append(tweet[field])

    return l

def compute_frequencies(l):
    freqs = {}
    for v in l:
        freqs[v] = freqs.setdefault(v, 0) + 1

    return freqs


