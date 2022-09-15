'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

price = 0
num_ticket = 1 

tickets = int(input("Введите количество билетов, которое хотите купить: "))

years = int(input("Введите возраст посетителя: "))

while num_ticket != tickets:
    num_ticket += 1
    
    if int(years) < 18:
        cost = 0
    elif 18 < int(years) < 25:
        cost = 990
    elif int(years) > 25:
        cost = 1390
    years = input("Введите возраст посетителя: ")

price = cost*tickets

if tickets > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом 10% скидки')
else:
    print(f'Сумма к оплате {price} руб.')



    
