#!/usr/bin/python
#
# hack@uchicago Introduction to Python Workshop
# Borja Sotomayor, 2013-2014

"""Harvest tweets from Twitter

Connects to the Twitter API to either harvest tweets
from the public stream, or saves tweets from a list
of accounts.
 
For this to work, you need to create an application on
Twitter under your account (https://dev.twitter.com/apps/new).
You will get a consumer key and a consumer secret.
This program expects these values to be stored in
a file containing the key and the secret in a single 
line, separated by a space. By default, the program
will look for a ".twitter-oauth" file in the same
directory as this program, but a different path
can be specified with the -c option.

When you first run this program, you will be redirected
to a twitter webpage where you will have to authorize
the program to access your account. Every subsequent
run won't require you to do this (until your credentials
expire).

The tweets are saved to a file, one tweet per line.
Each tweet is encoded in JSON. However, the file itself
is not a valid JSON file (it must be read line by line,
and each line should be decoded separately).

"""

import argparse
import twitter
import json
import os.path
import signal
import sys

def signal_handler(signal, frame):
        global outfile
        outfile.close()
        print('You pressed Ctrl+C!')
        sys.exit(0)

def parse_command_line_arguments():
    """Parses the arguments provided through the
    command line. Run the program with option "-h"
    to see a human-readable description of the
    arguments"""

    description, epilog = __doc__.split("\n\n", 1)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description,
        epilog=epilog)

    parser.add_argument('-n', '--n', dest='n', action='store', type=int, required=True,
                       help='Number of tweets to harvest. Set to 0 to keep harvesting until the program is stopped explicitly.')
    parser.add_argument('-u', '--userfile', dest='userfile', action='store',
                       help='If specified, only fetch tweets from accounts specified in this file (one per line). The number of tweets per account is specified with the -n parameter.')
    parser.add_argument('-o', '--outfile', dest='outfile', action='store', required=True,
                       help='File to store the tweets in')
    parser.add_argument('-f', '--filter', dest='filter', action='store', required=False,
                       help='Filter stream by keywords (comma-separated list)')
    parser.add_argument('-c', '--consumer-credentials', dest='consumer_credentials', action='store',
                        default="./.twitter-oauth",
                        help='File with Twitter OAuth credentials (consumer key and secret, separated by a single space)')
    parser.add_argument('-k', '--user-credentials', dest='user_credentials', action='store',
                        default="./.twitter-credentials",
                        help='File with user credentials (fetched with the "OAuth Dance")')

    args = parser.parse_args()
    
    return args

def save_tweet(tweet, f):
    # Replace HTML entities
    tweet["text"] = tweet["text"].replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")

    print >>f, json.dumps(tweet)

if __name__ == "__main__":

    args = parse_command_line_arguments()
    
    
    # OAuth magic
    consumer_key, consumer_secret = open(args.consumer_credentials).read().strip().split()
    
    if not os.path.exists(args.user_credentials):
        twitter.oauth_dance("hack@uchicago Python Workshop", consumer_key, consumer_secret, args.user_credentials)
    
    oauth_token, oauth_secret = twitter.read_token_file(args.user_credentials)
    
    auth=twitter.OAuth(oauth_token, oauth_secret, consumer_key, consumer_secret)
    
    outfile = open(args.outfile, "w")
    
    if args.userfile:
        t = twitter.Twitter(auth=auth)
    
        users = open(args.userfile).read().strip().replace("@", "").split()
        for user in users:
            print "Fetching %i tweets from @%s" % (args.n, user)
            tweets = t.statuses.user_timeline(screen_name=user, count=args.n)   
            print "  (actually fetched %i)" % len(tweets)    
            for tweet in tweets:
                save_tweet(tweet, outfile)
    else:
        # Connect to the stream
        twitter_stream = twitter.TwitterStream(auth=auth)
    
        if args.filter is None:
            stream = twitter_stream.statuses.sample()
        else:
            stream = twitter_stream.statuses.filter(track=args.filter)
    
        # Fetch the tweets
        fetched = 0
    
        if args.n > 0:
            print "Fetching %i tweets... " % args.n
        else:
            signal.signal(signal.SIGINT, signal_handler)
            print "Fetching tweets. Press Ctrl+C to stop."
    
        for tweet in stream:
            # The public stream includes tweets, but also other messages, such
            # as deletion notices. We are only interested in the tweets.
            # See: https://dev.twitter.com/docs/streaming-apis/messages
            if tweet.has_key("text"):
                # We also only want English tweets
                if tweet["lang"] == "en":
                    save_tweet(tweet, outfile)
                    fetched += 1
                    if fetched % 100 == 0:
                        print "Fetched %i tweets." % fetched
                    if args.n > 0 and fetched >= args.n:
                        break
    
    outfile.close()

