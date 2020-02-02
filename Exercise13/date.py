# Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία 
# σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ και εμφανίζει πόσες μέρες/ώρες/
# δευτερόλεπτα απέχει αυτή από σήμερα καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας
import datetime

months = {"01": 31, "02": 28, 
                      "03": 31, "04": 30,
                      "05": 31, "06": 30, 
                      "07": 31, "08": 31,
                      "09": 30, "10": 31,
                      "11": 30, "December": 31}

def yearisleap(x):
    return (x%4 == 0) and (x%100 != 0) or (x%400 == 0)

# You should complete the definition of this function:

def rangeofmonths(month, year):
    if yearisleap(int(year)) and month == '02':
        print('The month from the selected date has : 29 days ')
    else: print('The month from the selected date has : ' ,months[month],'days')


search = input('Enter End date in the format dd/mm/yy: ')

now = datetime.datetime.now()
time = now.strftime('%X')

newdate = search + time
data = datetime.datetime.strptime(newdate , '%d/%m/%Y%H:%M:%S')

diff =  data - now
print('The difference from the current date and the date you gave is : ' ,diff)

m = data.strftime('%m')
print(m)
y = data.strftime('%y')
rangeofmonths(m,y)


