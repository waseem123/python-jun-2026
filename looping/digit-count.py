# n = 3259554522125
# n = str(n)
# print(len(n))

n =  int(input('ENTER A NUMBER - '))
count = 0

if n == 0:
    print(1)
else:
    while n != 0:
        count += 1
        n = n // 10
    print(count)