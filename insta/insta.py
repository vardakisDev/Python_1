import instaloader
from collections import Counter 
from itertools import islice

L = instaloader.Instaloader()
user = input('Please give us the username of the profile you want to find out: ')
profile = instaloader.Profile.from_username(L.context, user)



data = []


for post in islice(profile.get_posts(),20) :
    post_comments = post.get_comments()

    for comment in post_comments:
        data.append(comment.owner.username)
print(data)
Counter = Counter(data) 
most_occur = Counter.most_common(1)
print('The three most active profiles in your comment section is:')
for i in range(len(most_occur)):
    print('1.',most_occur[i][0])
