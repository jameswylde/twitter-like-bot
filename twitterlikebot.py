# @ferus-wylde

# Import libraries

import tweepy
import time
from termcolor import cprint
from pyfiglet import figlet_format

# ASCII title

cprint(figlet_format("TwitterLiker", font="standard"), "blue", attrs=["bold", "dark"])

# APIs and Secret Keys

auth = tweepy.OAuthHandler("", "")

auth.set_access_token("", "")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# Input: What and how many

search = str(input(("What to like?\n")))

while True:
    try:
        noTweets = int(input(("How many to like?\n")))
        break
    except:
        print("Numerical input only.\n")

for tweet in tweepy.Cursor(api.search, search).items(noTweets):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
