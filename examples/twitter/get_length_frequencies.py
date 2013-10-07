import workshop
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

lengths = {}

for tweet in workshop.tweets_text(n, tfile):
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
