x = 100
y = 50
z = 77

print(x>y and x>z) # (True and True) => True
print(x>y and z>x) # (True and False) => False
print(x<y and z>x) # (False and False) => False
print('_______________________')

print(x>y or x>z) # (True or True) => True
print(x>y or z>x) # (True or False) => True
print(x<y or x>z) # (False or True) => True
print('________________________')

print(not(x>y and x>z)) # not(True and True) => not(True)
print(not(x>y or x<z)) # (True or False) => False
print((x>y) and (not(x<z))) #(True and True) => True

print(not(not(x>y) and not(x<z))) 

#not(not(True) and not(False))
# not(False and True)
# not(False) 
# => True