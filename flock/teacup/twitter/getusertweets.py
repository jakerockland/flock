import tweepy
import flock.config

twitter_auth = flock.config.oauth.get('twitter', {})
key = twitter_auth["consumer_key"]
key_secret = twitter_auth["consumer_secret"]

def getusertweets():
    return
