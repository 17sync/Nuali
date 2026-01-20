# Nuali

A Twitter/X bot that tweets a joke every 2 hours or so. Nuali also performs basic actions such as liking, retweeting and replying to posts. <br>

![Profile](images/profile.png)

> Link to profile: https://x.com/NualiPy <br>
> Inspiration: https://github.com/Lucas-Kohorst/Twitter-Bot <br>

<br>

## Code Overview

- **post_tweet()**: Automates tweeting, picks a random joke and posts it.
```python
def post_tweet():
    tweet = random.choice(jokes)
    client.create_tweet(text=tweet)
    logging.info(f"Tweet posted: {tweet}")
``` 
<br>

- **interact_with_tweets()**: Makes use of the API to retweet, reply to and search for tweets.
```python
def interact_with_tweets():
    query = " OR ".join(keywords) + " -is:retweet lang:en"
    response = client.search_recent_tweets(query=query, max_results=5)
    if response.data is None:
        return
    for tweet in response.data:
        try:
            client.like(tweet.id)
            try:
                client.retweet(tweet.id)
            except:
                pass
            reply = random.choice(replies)
            client.create_tweet(text=reply, in_reply_to_tweet_id=tweet.id)
            logging.info(f"Interacted with tweet {tweet.id}")
            time.sleep(20)
        except Exception as e:
            logging.error(str(e))
```
<br>

- **run()**: Main loop calling posting and interactions repeatedly.
```python
def run():
    while True:
        try:
            post_tweet()
            interact_with_tweets()
        except Exception as e:
            logging.error(str(e))
        time.sleep(tweetInterval)
```
<br>

>full source code: https://github.com/17sync/Nuali/blob/main/Nuali.py

<br>

## SDLC Phases Overview

### Planning <br>

The purpose of this project is to develop a Twitter/X bot that performs actions such as posting tweets, retweeting, replying etc based on predefined rules. <br>

**Objectives:** <br>
- Automate basic interactions such as tweet posting, following etc.
- Learn and implement Twitter/X API usage.
- Apply SDLC concepts on a real project. <br>

**StakeHolders:** <br>
- Developers: @17sync, @Thor-Lowkey
- Supervisor: @ayyzenn
- End Users: Twitter/X users interacting with Nuali
- Platform Provider: Twitter/X <br>

**Timeline:** <br>
![SDLC Timeline](images/sdlcTimeline.png) <br>

<br>

### Requirements<br>

What the bot must do and it's constraints.

**Functional Requirements:** <br>
- Post tweets automatically at scheduled intervals.
- Favourite tweets containing specific keywords.
- Retweet tweets containing relevant keywords. 
- Reply to tweets containing specific keywords.
- Nuali's replys should be human-like and well thought out. 
- Nuali's behaviour must not cause any harm or spread toxicity. <br>

**Non-Functional Requirements:** <br>
- Nuali must run 24/7 with minimal downtime.
- Interval between tweets should be an hour.
- Nuali must be secure (API keys stored and not exposed) <br>

<br>

### Design

This phase focuses on defining the system architecture, components, and workflows. The goal is to ensure the system is modular, secure, and compliant with Twitter/X API policies.

**System Architecture:**
Nuali follows a modular, script-based architecture where each core functionality is handled independently. This improves maintainability and scalability.

**Main Components:**
- Authentication Module
- Tweet Scheduler
- Keyword Scanner
- Interaction Handler
- Reply Generator
- Error & Rate Limit Handler
- Logging Module

**Design Constraints:**
- Must comply with Twitter/X automation rules.
- Limited by Non-Elevated API access.

<br>

### Development

This phase involves implementing the system based on the design specifications using Python and Tweepy.

**Development Environment:**
- Language: Python
- Library: Tweepy
- IDE: VS Code
- Platform: Local Machine
- Version Control: Git & GitHub

**Development Approach:**
The bot is developed incrementally, starting with authentication and followed by core functionalities.

**Development Constraints:**
- Limited API access.
- No machine learning or advanced NLP features.
- Must comply with Twitter/X policies.

<br>

### Testing

The testing phase ensures that Nuali operates correctly, reliably, and within defined constraints.

**Testing Objectives:**
- Verify correct functionality of all bot features.
- Ensure compliance with Twitter/X API policies.
- Detect and fix errors before deployment.

<br>

>complete documentation: https://github.com/17sync/Nuali/tree/main/docs
