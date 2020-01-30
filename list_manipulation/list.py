
import random

file = open("testfile.txt","w+")
for i in range(0,100):
    line = str(random.randint(1000,9999))+','
    file.write(line)
file.close()