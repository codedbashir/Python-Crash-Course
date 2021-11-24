#Checking if a name is the same as reverse
'''user_name = input('Kindly insert your name here:' ).lower()

if user_name == user_name[::-1]:
    print(f'Hi {user_name}; your name is a palindrome')

else:
    print(f'Hi {user_name}, your name is not a palindrome')

animal_name1 = input('Give the animal name: ')
animal_name_2 = input('Give the second animal name: ')

if animal_name1[0] == animal_name_2[0]:
    print(f'The first letter in {animal_name1} is the same as first letter in {animal_name_2}')

else:
    print('The letter are not the same')'''


# Zakat Calculator
'''users_money = int(input('Please enter your savings for the last one year: '))
debt_status = input('Please do you have debt? True or False ').lower()
nisob = 1500000

if debt_status == 'true':
    debt = int(input('Please enter your debt: '))
    new_user_money = users_money - debt
    if new_user_money >= nisob:
        your_zakat = new_user_money * 0.025
        print(f'Your zakat this year is {your_zakat}')
    else:
        print(f'Your money{new_user_money} is not zakatable,\n because it is not upto {nisob}, which is the minimum nisob value')
elif debt_status == 'false':
    your_zakat = users_money * 0.025
    print(f'Your zakat this year is {your_zakat}')
else:
    print(f'Your money is not zakatable, because it is not upto {nisob}, which is the minimum nisob value')


if debt_status == 'true' and users_money >= nisob:
    debt = int(input('Please enter your debt: '))
    new_user_money = users_money - debt
    if new_user_money >= nisob:
        your_zakat = new_user_money * 0.025
        print(f'Your zakat this year is {your_zakat}')
    else:
        print(f'Your money{new_user_money} is not zakatable,\n because it is not upto {nisob}, which is the minimum nisob value')
elif debt_status == 'false' and users_money >= nisob:
    your_zakat = users_money * 0.025
    print(f'Your zakat this year is {your_zakat}')
else:
    print(f'Your money is not zakatable, because it is not upto {nisob}, which is the minimum nisob value')



'''
zakatable_item = input('Please insert the item you to used for zakat. choose either money, or cow ').upper()

if zakatable_item == 'MONEY':
    users_money = int(input('Please enter your savings for the last one year: '))
    debt_status = input('Please do you have debt? True or False ').lower()
    nisob = 1500000

    if debt_status == 'true' and users_money >= nisob:
        debt = int(input('Please enter your debt: '))
        new_user_money = users_money - debt

        if new_user_money >= nisob:
            your_zakat = new_user_money * 0.025
            print(f'Your zakat this year is {your_zakat}')
    
        else:
            print(f'Your money{new_user_money} is not zakatable,\n because it is not upto {nisob}, which is the minimum nisob value')
    
    elif debt_status == 'false' and users_money >= nisob:
        your_zakat = users_money * 0.025
        print(f'Your zakat this year is {your_zakat}')
    
    else:
        print(f'Your money is not zakatable, because it is not upto {nisob}, which is the minimum nisob value')

elif zakatable_item == 'COW':
    users_cow_quantity = int(input('Kindly insert your total number of cow '))
    nisob = 30
   
    if users_cow_quantity < nisob:
        print(f'No Zakat is due because your quantity of cows, {users_cow_quantity}, is less than {nisob}')
    
    elif users_cow_quantity >= nisob and users_cow_quantity >= 30 and users_cow_quantity < 40:
        your_zakat = 1
        print(f'Your zakat is {your_zakat} cow aged one year')

    elif users_cow_quantity >= nisob and users_cow_quantity  >= 40 and users_cow_quantity < 50:
        your_zakat = 1
        print(f'Your zakat is {your_zakat} cow aged two years')

    elif users_cow_quantity >= nisob and users_cow_quantity  >= 50 and users_cow_quantity < 60:
        your_zakat = 2
        print(f'Your zakat is {your_zakat} cows aged one year')

    elif users_cow_quantity >= nisob and users_cow_quantity  >= 60 and users_cow_quantity < 70:
        your_zakat = 2
        print(f'Your zakat is {your_zakat} cows aged one year and two year')

    elif users_cow_quantity >= nisob and users_cow_quantity  >= 70 and users_cow_quantity < 80:
        your_zakat = 2
        print(f'Your zakat is {your_zakat} cows both aged two years')

    elif users_cow_quantity >= nisob and users_cow_quantity  >= 90 and users_cow_quantity < 100:
        your_zakat = 3
        print(f'Your zakat is {your_zakat} cows aged two years')

else:
    print(f'your good, {zakatable_item}, is not a zakatable good')


