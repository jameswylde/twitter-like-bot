# @ferus-wylde

# Import libraries

import os
import tweepy
import time
from termcolor import cprint
from pyfiglet import figlet_format



# Clears the terminal

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()




# ASCII title

cprint(figlet_format('Tweet', font='banner3-D'), 'blue', attrs=['bold', 'dark'])
cprint(figlet_format('Liker', font='banner3-D'), 'blue', attrs=['bold', 'dark'])
cprint(figlet_format('jimcw44', font='banner3-D'), 'blue', attrs=['bold', 'dark'])




# APIs and Secret Keys

# Enter consumer key and consumer secret generated from Twitter Dev under 'Consumer Keys' for your created Project/App under 'Keys and Tokens'

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')

# Enter access token and access token secret from Twitter Dev under 'Authentication Tokens' for your created Project/App under 'Keys and Tokens'

auth.set_access_token('access_token', 'access_token_secret')



# Twitter restricts how many requests can be made to the server via this API, we can set it to run on the allowed amount with the below

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


# Prompt to define what to look for, can be a user, hashtag, or any word. Anything that is contained within a tweet.
# Prompt to define how many to like. As above, there's a limit on requests via API, 900 requests/15 minutes.

search = str(input(('What to like?\n')))

while True:
    try:
        noTweets = int(input(('How many Tweets to like?\n')))
        print('\n')
        break
    except:
        print('Numerical input only.\n')
        print('\n')

for tweet in tweepy.Cursor(api.search, search).items(noTweets):
    try:
        print('#######################################')
        print('@'+tweet.user.screen_name)
        print(tweet.text)
        print('#######################################')
        print('\n')
        tweet.favorite()
        time.sleep(3)
    except tweepy.TweepError as e:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print(e.reason)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('\n')
    except StopIteration:
        break
    except tweepy.RateLimitError:
        time.sleep(15 * 60)