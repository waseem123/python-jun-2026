n1 = 90
n2 = 90
n3 = 90

if n1>n2 and n1>n3:
    print(f'{n1} IS GREATER THAN {n2} AND {n3}')
elif n2>n1 and n2>n3:
    print(f'{n2} IS GREATER THAN {n1} AND {n3}')
elif n3>n2 and n3>n1:
    print(f'{n3} IS GREATER THAN {n1} AND {n2}')
else:
    print('ALL NUMBERS ARE EQUAL')