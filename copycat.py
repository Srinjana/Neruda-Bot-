# tweets everytime a tweet is made by @3_rashi
import tweepy
import time
from credentials import *
from random import randint as r
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# reading the data from a file for the bot to tweet

filename = open('texts/pablo.txt', 'r')
text_to_be_tweeted = filename.readlines()
filename.close()

#  REPLYING PART

last_tweet = None  # assuming that last tweet had a null value

# picking a random line to reply with


def reply_line():
    return r(0, len(text_to_be_tweeted) - 1)

# most replywork code done in this fn


def compare_the_tweets():
    global last_tweet

    #obtains last tweet by @3_rashi and prints its id
    latest_tweet_made = api.user_timeline('3_rashi')[0]
    print(latest_tweet_made.id)

    # when there is a new tweet, it compares the tweets and prints a line from the textfile
    if latest_tweet_made != last_tweet:
        the_line = text_to_be_tweeted[reply_line()]
        api.update_status(status=the_line)
        print(the_line)

    last_tweet = latest_tweet_made


# runs this every 100secs
while True:
    compare_the_tweets()
    print("Sleeping!!! ZZZZ ")
    time.sleep(100)


# to terminate the process press CTRL+C and wait for some time.
