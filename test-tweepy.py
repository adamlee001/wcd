# imports
import csv
import json
import time
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#for pretty print _json
import pprint

# set twitter keys/tokens
consumer_key = 'NIGXsjjRwdWL7Mjoroemu4ItI'
consumer_secret = 'YF3G19UMqWALPgT8rCPp034N2eS0DPo532U8x3X7kne2C6FBnu'
access_token = '1244254596584869888-R4N7AZCgRpzJUqzIJLy0aNnDzD8ASf'
access_token_secret = 'eXPJYW5mPeC5L3yngPqOLNxV8g185O6YfNbuxV8puPlTl'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Let's start by taking a look at our own user account.
my_twitter = api.me()
print(my_twitter.name)

#For a full list of information we can get from this object, we can look at the json it returns
print(my_twitter._json)

#To get a nested piece of data, we just have to chain the methods.
print(my_twitter.status.retweet_count)

#To get a particular user, we can specify a user id or screen name to the 'get_user' method. Here we look at Canadian Tire's twitter.
user = api.get_user('CanadianTire')
print(user.name)
print(user.description)
pprint.pprint(user._json)

#We can get all the tweets from our home timeline by looping over the 'home_timeline' method.

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

#By default this will return 20 tweets. If we want to increase this amount we can set the 'count' parameter.
len(api.home_timeline())
len(api.home_timeline(count=30))


#Since 'home_timeline' returns multiple data objects, if we want to take a look at the json response we need to select only one of them.
print('look at jason response of first tweet')
pprint.pprint(public_tweets[0]._json)


#We can use 'followers_ids' to get the user ids of Trump's followers and use 'get_user' like before to get the screen names.
trump_followers = api.followers_ids('realDonaldTrump')

# let's just slice to get the first 10
print('first 10 Trump\'s followers')

for user_id in trump_followers[:10]:
    print(api.get_user(user_id).screen_name)


#We can also get the relationship between two users.

# between our own account and Trump's
print('relationship between me and trump???')
pprint.pprint(api.show_friendship(source_screen_name=api.me().screen_name, target_screen_name='realDonaldTrump'))

print('relationship: me & cibc')
pprint.pprint(api.show_friendship(source_screen_name=api.me().screen_name, target_screen_name='cibc'))

#Trend
#For example, if we look at the list above, we can see that the 'woeid' for Toronto is 4118. We can use this to get all the trending tweets in Toronto.

trends = api.trends_place(4118)
print(trends)

for trend in trends[0]['trends']:
    print(trend['name'])
