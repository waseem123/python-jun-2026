n = int(input('ENTER A NUMBER - '))
rev = 0

while n!=0:
    rem = n % 10  # 1
    rev = rem + (rev * 10) # 1 + (432 * 10) => 4321
    n = n // 10
    
print(rev)