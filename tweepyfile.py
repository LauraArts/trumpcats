import tweepy

auth = tweepy.OAuthHandler("izowwmSEmwlF9Fwr8qYi2EOF4", "NWrzJSvEHPK5OokQ9T67QncQc686e5zoVcUFfNzY7XGrB4u9Ud")
auth.set_access_token("889586308678549509-0PKe6Df8Ulwi6ZrKLiNhN9ULnmy0TWa", "v5d214qwOdq2NKggq8XeC9whPGh3De4314uoD1JoGyO4S")

api = tweepy.API(auth)

public_tweets = api.user_timeline("realDonalTrump")
for tweet in public_tweets:
    print (tweet.text)