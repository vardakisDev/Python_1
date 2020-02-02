import tweepy
import re

def SumTweets(tweets):
    total =0
    # we  remove the specail chars like @ ! and then with the fiter(None) we remove the "" strings from the list so our count doesnt count them
    for tweet in tweets:
        counting = re.split(r'[^\w]' , tweet.full_text)
        counting = list(filter(None,counting))
        total = total + len(counting)
    return total 

#use the dev twitter tools
auth = tweepy.OAuthHandler("CQR7rH6B6CQvyPsDLeOFDx1vt", "T6Saw4oayNRYhsS6u6JEB2XKoPHoBfyLxokXTulSn24mOQJZAs")
auth.set_access_token('887397697-XFxTUUEuLnqoLDtNiopGPlek5v0iMEN01Hmz5lss', "sCGFVZeBQJraJpTaqifk4E1JY13053ExFwfUrJLo1ubpd")
#call the api
api = tweepy.API(auth)

#ask for user input for the profiles he wants to compare he has to use @ in order for api.user_timeline function to work save the user input and use the api to get the object which contains the full text of tweet 
user1_tweets = api.user_timeline(input('Give user1 , dont forget to use @   :') , count=50 , tweet_mode="extended")
user2_tweets = api.user_timeline(input('Give user2 , dont forget to use @   :'), count=50 , tweet_mode="extended")

sum1 = SumTweets(user1_tweets)
sum2 = SumTweets(user2_tweets)

if sum1>sum2 : 
    print("The user1 has in his latest 50 tweets a summary of :" ,sum1,"words")
else:
    print("The user2 has in his latest 50 tweets a summary of :" ,sum2,"words")
