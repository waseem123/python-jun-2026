
grand_total = 0
ch = 1
while ch==1:
    print('1. Biryani - INR. 150')
    print('2. Shawarma - INR. 120')
    print('3. Tea - INR. 15')
    print('4. Cold Drink - INR.20')
    choice = int(input('ENTER YOUR CHOICE - '))

    match choice:
        case 1:
            qty = int(input('ENTER QUANTITY OF BIRYANI-'))
            bill = qty * 150
            grand_total +=  bill
            print(f'YOUR BILL FOR {qty} BIRYANI(s) IS INR.{bill}')
        case 2:
            qty = int(input('ENTER QUANTITY OF SHAWARMA-'))
            bill = qty * 120
            grand_total +=  bill
            print(f'YOUR BILL FOR {qty} SHAWARMA(s) IS INR.{bill}')
        case 3:
            qty = int(input('ENTER QUANTITY OF TEA-'))
            bill = qty * 15
            grand_total +=  bill
            print(f'YOUR BILL FOR {qty} TEA(s) IS INR.{bill}')
        case 4:
            qty = int(input('ENTER QUANTITY OF COLD DRINK -'))
            bill = qty * 20
            grand_total +=  bill
            print(f'YOUR BILL FOR {qty} COLD DRINK(s) IS INR.{bill}')
        case _:
            print('WRONG INPUT! PLEASE SELECT OPTION BETWEEN 1 TO 4')
            
    ch = int(input('PRESS 1 TO ORDER MORE - '))
    
print(f'YOUR TOTAL BILL IS - {grand_total}')
print("THANKS! VISIT AGAIN.")