
def luhn(digits):
    digit = [int(x) for x in digits[::-2]] 
    u2 = [(2*int(y))//10+(2*int(y))%10 for y in digits[-2::-2]]
    return sum(digit+u2)%10 == 0

# given = input(' Give the 16 number of your card :' )
print(luhn("49927398716"))


