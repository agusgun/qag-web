# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

class TwitterAPI:

	def __init__(self, app):
		self.__ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
		self.__ACCESS_SECRET = app.config['TWITTER_ACCESS_SECRET']
		self.__CONSUMER_KEY = app.config['TWITTER_CONSUMER_KEY']
		self.__CONSUMER_SECRET = app.config['TWITTER_CONSUMER_SECRET']
		self.__oauth = OAuth(self.__ACCESS_TOKEN, self.__ACCESS_SECRET, self.__CONSUMER_KEY, self.__CONSUMER_SECRET)
		self.__twitters = Twitter(auth=self.__oauth)

	def fetchUserTimeline(self, user):
		results = self.__twitters.statuses.user_timeline(screen_name=user)
		return results