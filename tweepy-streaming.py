######################################################
# Getting started with tweepy and twitter streaming
######################################################

# Import tweepy libraries
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# Define how you are going to parse the JSON response from twitter API in the on_data function below
class TweetStreamListener(StreamListener):
    # on success
    def on_data(self, data):
        # decode json
        dict_data = json.loads(data)

        if "text" in dict_data.keys():
            print(dict_data["created_at"],  dict_data["text"])

        return True

    # on failure
    def on_error(self, status):
        print(status)


# Provide your twitter credential below
consumer_key = 'NIGXsjjRwdWL7Mjoroemu4ItI'
consumer_secret = 'YF3G19UMqWALPgT8rCPp034N2eS0DPo532U8x3X7kne2C6FBnu'
access_token = '1244254596584869888-R4N7AZCgRpzJUqzIJLy0aNnDzD8ASf'
access_token_secret = 'eXPJYW5mPeC5L3yngPqOLNxV8g185O6YfNbuxV8puPlTl'


# Provide the filtering criteria below and start the stream listener
if __name__ == '__main__':
    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()
    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # create instance of the tweepy stream
    stream = Stream(auth, listener)
    # search twitter for "tweet" keyword
    stream.filter(track=['#trump'])
