import tweepy

key = 'vPluelKSMjckqdcyEr3cst0QH'
key_secret = 'ZkeGf68XyJxOGQkvXft8THHDTdbUMMzy5hde3AzvH4qISyGTg8'

def getusertweets(access_token, access_token_secret):
    auth = tweepy.OAuthHandler(key, key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    username = api.me().screen_name

    tweets = []

    for tweet in tweepy.Cursor(api.user_timeline, count=100).items():
        tweets.append(tweet)

    # API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
    # API.search_users(q[, per_page][, page])

    return username, tweets

getusertweets('2585352386-0A1shtpRmPL68IwlrdC7SE10vnXqRXxUz4BgYHT','3DyLhHWlKwBdZhvxag0k3ncBJnaSsyFhUZRxkFOTxNISe')