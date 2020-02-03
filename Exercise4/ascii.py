


x = 'Stelios Vardakis'
n = ''.join(str(ord(i)) for i in x)
print(n)
isPrime = 0


#  time needed to 0(srqt(n))
n =int(n)
i = 2
while i*i <= n:
    if n % i == 0:
        isPrime=1
        break
    i += 1
# since all the vaues of ascii code are greater than 1, 2,5 we dont have to check for those numbers

if isPrime==0:
    print('Its prime')
else: print('Its not a prime')

