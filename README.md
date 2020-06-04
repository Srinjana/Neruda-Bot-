#  Neruda Bot

## A twitter bot that posts Pablo Neruda quotes ##
  
  This is a Python Project that generates a twitter Bot which Shares quotes by Pablo Neruda. 
  Furthermore it listens to the Tweets by my Twitter account (@3_rashi) and Responds by posting a Random Neruda Quote in the Bot's  account.
  
  You can find Neruda Bot here : https://twitter.com/bot_neruda
  
  This code was written in Python 3.

**Required libraries:** tweepy 3.8, requests, time, os, random

---
## Creating a Twitter account for your bot

1. Go to http://twitter.com and sign up for a new account of your choosing
 - Include your mobile number (required for using the API) 
 - Email address must be unique to Twitter users

2. Go to http://apps.twitter.com and create a new app
 - Fill in project details during developer Application
 - Verify Email after completing Developer Application to create a New App
 - This info isn't public so be careful and keep multiple copies of the data 
 - Go to `Keys and Access Tokens`
 - `Create my access token`

3. Copy Consumer Key/Secret and Access Key/Secret to **credentials.template** and save as a new file named **credentials.py**

**WARNING :** Credentials are sensitive Data. Do not share it with others.

---
## Creating a .txt file with all the Quotes

- All the text file is stored in the texts folder inside the file `pablo.txt`
- Limit the number of characters per sentence to 140 charaters only because it would be too long for twitter otherwise.
- Make sure all the Data are compliant to a plain text file. (I seperated the data based on '.')
- If the original dataset is in ALL CAPS!, change text case to Sentence Case. (acronyms included)
- Replace multiple line breaks (\n+ in regex) with single ones (\n).
- Scan the text file to see if there are any unsupported characters which might throw you encoding errors.
---
## Basic bot: testing.py ##

  This isn't actually a bot, but it is a script that sends out one tweet using the Twitter API. This is to basically check if the code  is working!

- Clicking `Run` will run the code. A console (output area) will appear at the bottom of the screen, and the bot will have made the first tweet.
---
## Intermediate bot: mainbot.py

this tweet generates a random number `absurd_number` (1-196) {since there are 196 lines of quotes}

This script sends out `absurd_number` of tweets from the first line onwards of an external .txt file stored in the texts folder

1. Click on `mainbot.py`

2. Also look at `pablo.txt` to see the text for the quotes

3. Select `Run`

4. It tweets certain random of tweets iterating from the first line of the text file everytime, and if the tweet is aleady made, it just replies with an Error message on the console. 

5. It waits *15 seconds* between two subsequent tweets.

---
## Advanced bot: copycat.py

- This script listens to all tweets by @3_rashi and tweets a random line from a `.txt` file whenever @3_rashi ( ME :3 ) tweets.
- The bot Takes Sleeping intervals by 100 secs
- Change who the bot listens to from @3_rashi to some other user.
- An ID is attached with the last tweet made by the Selected user and when the ID changes, a new tweet is made.
---

The code can be stopped from runnig at anytime by a keyboard interrupt. `CTRL+C` on your console.
