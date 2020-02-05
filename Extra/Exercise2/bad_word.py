
with open("badwords.txt","r") as f:
    data = f.read().split()
f.close()

good = list("bdghjlmnpqstvexzBDGHJLMNPQSTVEXZ")
bad = list("fckrFCKR")

for word in data:
    number_of_good = sum(word.count(g) for g in good)
    number_of_bad = sum(word.count(b) for b in bad)
    if (number_of_bad > number_of_good):
        print('This is a bad word:' , word)
    