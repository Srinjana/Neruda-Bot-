# Bot reads a textfile line by line and tweets them individually.


import tweepy
import time
from credentials import *
from random import randint
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#  TWEETING PART

#  generating a random number 
absurd_number = randint(1, 196)
print(absurd_number)
# reading the data from a file for the bot to tweet

filename = open('texts/pablo.txt', 'r')
text_to_be_tweeted = filename.readlines()
filename.close()

# looping through the file to extract text
def bot_tweet():
    for my_line in text_to_be_tweeted[0:absurd_number]:
        try:
            print(my_line)
            if my_line != '\n':
                api.update_status(status=my_line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        time.sleep(15)

bot_tweet()
print("Mission Accomplished!")
# to terminate the process press CTRL+C and wait for some time.

