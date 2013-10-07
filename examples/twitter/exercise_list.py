import workshop
import math

N = 10000 # Number of tweets to use

tweets = workshop.load_tweets_text(N)

length_sum = 0
lengths = []

for tweet in tweets:
    length_sum += len(tweet)
    lengths.append(len(tweet))

avg = length_sum / N

stdev_sum = 0
for length in lengths:
    stdev_sum += (length - avg)**2

stdev = math.sqrt(stdev_sum/N)

print "The average length is %.2f" % avg
print "The standard deviation is %.2f" % stdev


