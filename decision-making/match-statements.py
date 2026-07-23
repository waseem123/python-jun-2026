print('1. Biryani - INR. 150')
print('2. Shawarma - INR. 120')
print('3. Tea - INR. 15')
print('4. Cold Drink - INR.20')
choice = int(input('ENTER YOUR CHOICE - '))

match choice:
    case 1:
        qty = int(input('ENTER QUANTITY OF BIRYANI-'))
        bill = qty * 150
        print(f'YOUR BILL FOR {qty} BIRYANI(s) IS INR.{bill}')
    case 2:
        qty = int(input('ENTER QUANTITY OF SHAWARMA-'))
        bill = qty * 120
        print(f'YOUR BILL FOR {qty} SHAWARMA(s) IS INR.{bill}')
    case 3:
        qty = int(input('ENTER QUANTITY OF TEA-'))
        bill = qty * 15
        print(f'YOUR BILL FOR {qty} TEA(s) IS INR.{bill}')
    case 4:
        qty = int(input('ENTER QUANTITY OF COLD DRINK -'))
        bill = qty * 20
        print(f'YOUR BILL FOR {qty} COLD DRINK(s) IS INR.{bill}')
    case _:
        print('WRONG INPUT! PLEASE SELECT OPTION BETWEEN 1 TO 4')