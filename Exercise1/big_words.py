import re

with open("lol.txt","r") as f:
    data = f.read().split()
f.close()
#we lower all the cases because later when we sort there will be duplicare words 
data =[word.lower() for word in data]
#we remove specail symbols we might encounter
data = [word.strip('.,') for word in data]
#remove all duplicates and sort
data = list(set(data))
data.sort(reverse=True,key=len)
#keep the first big words
data = data[0:5]
vowels=['aeiou']
#remove vowels
result = [re.sub(r'[aeiou]','',word) for word in data]
print(result)
for word in result:
    #what deos [-1::-1] mean ? well -1 at the start means that we start from the end the second is empty which indicates we to go to the end of the string and -1 is the step 
    word=word[-1::-1]
    print(word)


