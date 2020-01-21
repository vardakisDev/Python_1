import tweepy
import re
#use the dev twitter tools
auth = tweepy.OAuthHandler("CQR7rH6B6CQvyPsDLeOFDx1vt", "T6Saw4oayNRYhsS6u6JEB2XKoPHoBfyLxokXTulSn24mOQJZAs")
auth.set_access_token('887397697-XFxTUUEuLnqoLDtNiopGPlek5v0iMEN01Hmz5lss', "sCGFVZeBQJraJpTaqifk4E1JY13053ExFwfUrJLo1ubpd")
#call the api
api = tweepy.API(auth)



#ask for user input for the profiles he wants to compare 
#he has to use @ in order for api.user_timeline function to work

user_tosearch1 = input('Give user1 , dont forget to use @   :')
user_tosearch2 = input('Give user2 , dont forget to use @   :')
# save the user input and use the api to get the object which contains the full text of tweet 
user1_tweets = api.user_timeline(user_tosearch1 , count=50 , tweet_mode="extended")
user2_tweets = api.user_timeline(user_tosearch2 , count=50 , tweet_mode="extended")

sum1 = 0
sum2 = 0

# we  remove the specail chars like @ ! and then with the fiter(None) we remove the "" strings from the list so our count doesnt count them
for tweet in user1_tweets:
    counting = re.split(r'[^\w]' , tweet.full_text)
    counting = list(filter(None,counting))
    sum1 = sum1 + len(counting)
for tweet in user2_tweets:
    counting = re.split(r'[^\w]' , tweet.full_text)
    counting = list(filter(None,counting))
    sum2 = sum2 + len(counting)

#
if sum1>sum2 : 
    print("The user1 has in his latest 50 tweets a summary of :" ,sum1,"words")
else:
    print("The user2 has in his latest 50 tweets a summary of :" ,sum2,"words")
