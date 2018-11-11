import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class TwitterAPIConfig(object):
	TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN') or 'you-will-never-guess'
	TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET') or 'you-will-never-guess'
	TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY') or 'you-will-never-guess'
	TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET') or 'you-will-never-guess'