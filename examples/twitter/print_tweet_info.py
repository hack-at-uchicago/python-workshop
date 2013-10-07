import workshop
import sys

tfile = sys.argv[1]
n = int(sys.argv[2])

for tweet in workshop.tweets(n, tfile):
    print "User:", tweet["user"]["screen_name"]
    print "Text:", tweet["text"]
    print "Date:", tweet["created_at"]
    print "Retweets:", tweet["retweet_count"]
    print "Hashtags:", tweet["entities"]["hashtags"]
    print


