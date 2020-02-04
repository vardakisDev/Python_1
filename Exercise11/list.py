
import random
from ast import literal_eval
# file = open("testfile.txt","w")
# for i in range(0,100):
#     line = str(random.sample(range(1,12),4))
#     file.write(line)
#     file.write('\n')
# file.close()

data = [numbers.rstrip('\n') for numbers in open("testfile.txt","r")]
print(data)
given = input('Give the the 6 exercises you want to look for , as 12,11,10,14:'  ).split(',')
search = [int(numbers) for numbers in given]
search = search[0:4]


for numbers in data:
    
    if literal_eval(numbers)==search:
        print('matched')
        break
