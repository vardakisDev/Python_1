


x = 'confecad'
n = ''.join(str(ord(i)) for i in x)
print(n)
isPrime = 0
prime =[1,3,7,9]
#  time needed to 0(srqt(n))
# if n == 1:
#     isPrime=1
# i = 2

# while i*i <= n:
#     if n % i == 0:
#         isPrime=1
#     i += 1


#since all the vaues of ascii code are greater than 1, 2,5 we dont have to check for those numbers
last=n[-1]
if last not in prime:
    print('Not a prime')
else:
    print('A prime')

