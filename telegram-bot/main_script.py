import config

from twython import Twython

# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.API_KEY)
