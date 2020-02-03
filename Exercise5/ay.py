# Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει ένα κείμενο από ένα αρχείο και το σπάει σε λεξεις.
#  Αν οι λέξεις έχουν μήκος πάνω από 3 γράμματα,
#  αφαιρέστε το πρώτο γράμμα και προσθέστε το γράμμα στο τέλος μαζί με το ay.

def ChangeWord(word):
    char1 = 'ay'
    if len(word)>3:
        char2 = word[0]
        char3 = word[1:len(word)]
        return char3+char2+char1
    else: return word

with open("lol.txt","r") as f:
    data = f.read().split()
f.close()
data = [ChangeWord(word) for word in data ]
print(data)
