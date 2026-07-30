n = 1223
rev = 0

while n!=0:
    rem = n % 10
    rev = rev + (rem * 10)
    n = n // 10
    
print(rev)