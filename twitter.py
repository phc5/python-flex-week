import tweepy
import sys
import pymongo
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

"""
    The Twitter streaming API is used to download twitter messages in real time.
    This is different from the REST API because REST is used to pull data from 
    twitter while the streaming API pushes messages to a persistent session, which 
    allows the streaming API to download more data in real time.

    An instance of tweepy.Stream establishes a streaming session and routes messages
    to StreamListener instance. And the override methods in this class will do work
    on the data.
"""
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        super(tweepy.StreamListener, self).__init__()
        self.api = api
        # Create new database
        self.db = pymongo.MongoClient().ChristmasEveEve

    """
        on_status() is invoked once a successful response is received from the
        server. Allows the listener to perform work on the data.

        We get the data from on_data() of tweepy's StreamListener and insert
        the data we get back into the database.
    """
    def on_status(self, status):
        print(status.text , "\n")
        data = {}
        data['text'] = status.text
        data['created_at'] = status.created_at
        data['coordinates'] = status.coordinates # use coordinates
        data['source'] = status.source
        self.db.Tweets.insert(data)

    # on_error() is called when a non-200 status code is returned.
    def on_error(self, status_code):
        print('Encountered error...', file=sys.stderr)
        return True

"""
    An instance of tweepy.Stream which establishes a streaming session and
    routes messages to MyStreamListener instance.
"""
sapi = tweepy.streaming.Stream(auth, MyStreamListener(api))

"""
    filter() is used to stream all tweets containing the word in 
    the track parameter (an array of search terms to stream)

    look into filter for hashtag
"""
sapi.filter(track=['ChristmasEveEve'])