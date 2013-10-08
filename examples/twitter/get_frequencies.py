import workshop
import operator
import sys

# For this script to run, you need to implement the extract_values
# and compute_frequencies values in exercise_functions.py
from exercise_functions import extract_values, compute_frequencies

tfile = sys.argv[1]
n = int(sys.argv[2])

for field in ["favorite_count", "retweet_count"]:
    print "Top 10 frequencies of %s" % field
    l = extract_values(n, tfile, field)
    freqs = compute_frequencies(l)
    freqs = freqs.items()
    freqs.sort(key = operator.itemgetter(1), reverse = True)
    for value, count in freqs[:10]:
        print value, count    
    print
