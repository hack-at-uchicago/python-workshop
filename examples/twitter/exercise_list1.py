import workshop
import math
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

length_sum = 0.0

for tweet in workshop.tweets_text(n, tfile):
    length_sum += len(tweet)

avg = length_sum / n

print "The average length is %.2f" % avg


