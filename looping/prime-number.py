n = int(input('ENTER A NUMBER - '))
isprime = True
part = n//2
for i in range(2,part):
    if n % i==0:
        isprime = False
        break

if isprime==True:print(n,'IS PRIME NUMBER')
else:print(n,'IS NOT PRIME NUMBER')