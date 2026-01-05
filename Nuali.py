import tweepy

apiKey="api_key"
apiSecret="secret_key"
bearerToken=r"bearer_token"         # r=raw string, for special characters
accessToken="access_token"
accessTokenSecret="secret_access_token"

client=tweepy.Client(bearerToken, apiKey, apiSecret, accessToken, accessTokenSecret)

auth=tweepy.OAuth1UserHandler(apiKey, apiSecret, accessToken, accessTokenSecret)        # not essential but helps incase we want to use tweepy functions that need OAuth 1.0a
api=tweepy.API(auth)

client.create_tweet(text="Hello world! I am Nuali.")