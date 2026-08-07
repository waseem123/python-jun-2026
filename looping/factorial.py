# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 5! = 1 * 2 * 3 * 4 * 5 = 120

n = 5
fact = 1
for i in range(1,n+1):
    # print(fact)
    fact = fact * i  #fact=120, i=6 => 120
print(fact)