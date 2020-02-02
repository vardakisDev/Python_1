
import random

file = open("testfile.txt","w+")
for i in range(0,100):
    line = str(random.randint(1,14))+','
    file.write(line)
file.close()