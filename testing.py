import tweepy
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot tweets
tweet = "Someday, somewhere — anywhere, unfailingly, you'll find yourself, and that, and only that, can be the happiest or bitterest hour of your life."

#sending and testing it printed on console.
api.update_status(status=tweet)
print(tweet)

print("Successful")