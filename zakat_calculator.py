# This is a zakat calculator
'''zakatable_item = input('Please insert the item you to used for zakat. choose either money, or cow ').upper()

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
    
    elif users_cow_quantity >= nisob:

        if users_cow_quantity in range(30,40):
            your_zakat = 1
            print(f'Your zakat is {your_zakat} cow aged one year')

        elif users_cow_quantity in range(40,60):
            your_zakat = 1
            print(f'Your zakat is {your_zakat} cow aged two years')

        elif users_cow_quantity  in range(60,70):
            your_zakat = 2
            print(f'Your zakat is {your_zakat} cows aged one year')

        elif users_cow_quantity  in range(70,80):
            your_zakat = 2
            print(f'Your zakat is {your_zakat} cows aged one yecowar and two year')

        elif users_cow_quantity  in range(80,90):
            your_zakat = 2
            print(f'Your zakat is {your_zakat} cows both aged two years')

        elif users_cow_quantity  in range(90,100):
            your_zakat = 3
            print(f'Your zakat is {your_zakat} cows aged two years')

        elif users_cow_quantity  in range(100,200):
            your_zakat = 4
            print(f'Your zakat is {your_zakat} cows aged two years')

else:
    print(f'your good, {zakatable_item}, is not a zakatable good')
'''

#checking addition of two numbers
'''number1 = int(input('Kindly insert your number: '))
number2 = int(input('Kindly insert your number: '))
#number3 = number1 + number2
if number1 + number2 == 20 or number2 == 20 or number1 == 20:
    print('True')

else:
    print('False')'''

'''
# script that returns the words of a sentence reversed
conversation = 'How are you'
conservation1 = conversation.split()
conversation3 = conservation1[::-1]
conversation_reversed = ' ' .join(conversation3)
print(f'{conversation}, \n\t {conservation1} \n\t {conversation3}\n\t {conversation_reversed}')'''

#FIZZ BUZZ
'''write a generic code that accepts a range of number from 1 to 100, and check if a number in that range is divisible by 3, it should print 'FIZZ', and if it is divisible by 5, it shpuld print 'BUZZ' and if it is divisible by both 3 and 5, it should print ,FIZZBUZZ,'''

ages = range(1,100)
for age in ages:
    if age % 3 == 0 and age % 5 == 0:
        print('FIZZBUZZ')

    elif age % 5 == 0:
        print('BUZZ')
    
    elif age % 3 == 0:
        print('FIZZ')

    else:
        print(f'{age}; you are neither divisible by 3 or 5')
