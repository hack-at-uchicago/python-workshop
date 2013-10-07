import workshop
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

tweets = workshop.get_tweets_text(n, tfile)

for tweet in tweets:
    print len(tweet)

#
# Alternatively:
#
# for tweet in workshop.tweets_text(N):
#    print len(tweet)
#

