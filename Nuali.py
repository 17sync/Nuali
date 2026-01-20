import tweepy
import time
import random
import logging

apiKey="api_key"
apiSecret="secret_key"
bearerToken=r"bearer_token"         # r=raw string, for special characters
accessToken="access_token"
accessTokenSecret="secret_access_token"

client=tweepy.Client(
    bearerToken,
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    wait_on_rate_limit=True
)

auth=tweepy.OAuth1UserHandler(      # not essential but helps incase we want to use tweepy functions that need OAuth 1.0a
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret
)                               
api = tweepy.API(auth)

logging.basicConfig(
    filename="nuali.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

tweetInterval=60*60

keywords=["python", "coding", "programming", "opensource"]

jokes=[
    "Why do programmers prefer dark mode? Because light attracts bugs.",         
    "There are 10 types of people in the world: those who understand binary and those who do not.",
    "I told my computer I needed a break, and it froze.",
    "Why do Java developers wear glasses? Because they do not C#.",
    "A SQL query walks into a bar, walks up to two tables and asks: Can I join you?",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "I changed my password to incorrect. Now whenever I forget it, the computer reminds me.",
    "There is no place like 127.0.0.1.",
    "Why did the programmer quit his job? Because he did not get arrays.",
    "Programmers do not sleep, they just wait.",
    "Hardware is the part of a computer you can kick.",
    "A programmer is told: Go to the store and buy a loaf of bread. If they have eggs, buy a dozen. He comes back with twelve loaves of bread.",
    "Real programmers count from zero.",
    "Why did the function return early? Because it had nothing else to do.",
    "I would tell you a UDP joke, but you might not get it.",
    "The best thing about a Boolean is that even if you are wrong, you are only off by a bit.",
    "I tried to catch an exception, but it caught me instead.",
    "Why did the developer go broke? Because he used up all his cache.",
    "A user interface is like a joke — if you have to explain it, it is not that good.",
    "My code works, I have no idea why."
]

replies=[
    "HMMMMMMMMM, interesting.",
    "Nah, I'd win.",
    "Really?!.",
    "LOOOOOOOOOOOOOOOOOOOOOOOOL",
    "WOWOWOWOWWWW!"
]

def post_tweet():
    tweet=random.choice(jokes)
    client.create_tweet(text=tweet)
    logging.info(f"Tweet posted: {tweet}")

def interact_with_tweets():
    query=" OR ".join(keywords) + " -is:retweet lang:en"
    response=client.search_recent_tweets(
        query=query,
        max_results=5
    )

    if response.data is None:
        return

    for tweet in response.data:
        try:
            client.like(tweet.id)
            try:
                client.retweet(tweet.id)
            except:
                pass
            reply=random.choice(replies)
            client.create_tweet(
                text=reply,
                in_reply_to_tweet_id=tweet.id
            )
            logging.info(f"Interacted with tweet {tweet.id}")
            time.sleep(20)
        except Exception as e:
            logging.error(str(e))

def run():
    while True:
        try:
            post_tweet()
            interact_with_tweets()
        except Exception as e:
            logging.error(str(e))
        time.sleep(tweetInterval)

run()
