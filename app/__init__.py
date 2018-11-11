from flask import Flask
from config import Config, TwitterAPIConfig

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(TwitterAPIConfig)

from app import routes