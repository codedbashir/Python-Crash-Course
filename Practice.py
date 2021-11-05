# No of Siblings
no_of_siblings = 10
print(f'I have {no_of_siblings} siblings')

#Task 3: Favourite Food
favourite_food = "Pounded Yam"
print(f'My favorite food is {favourite_food}')

num1 = 12
num2 = 20
add_num = num1 + num2
sub_num = num1 - num2
mult_num = num1 * num2
div_num = num1 / num2
flo_div_num = num1 // num2
modu_num = num1 % num2
expo_num = num1 ** 2
print(f'Addition of no is {add_num}, Subtraction is {sub_num}, multiplication is {mult_num}, division is {div_num}, float division is {flo_div_num}, modulus is {modu_num} and exponential is {expo_num}')

print("Bashir Salako")
#print('o----')
#print('||||')
#price= 20
#print(price)
#name = input('what is your name? ')
#favourite_color = input('what is your color')
#print( name  +  ' likes'  +  favourite_color)

#weight_pound = input('what is your weight')
#weight_kilogram = 2.2 + int(weight_pound)
#print(weight_kilogram)

# FORMATTED STRING
#first = 'John'
#last = 'smith'
#message = first + '[' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(message)
#print(msg)

#len is used to put limitation.
#course = 'Python for beginners'
#print(len(course))

#Arithmethic operations % --remainda, **- exponential, //--integer

# Math Function  (Print(round(2.9); Print(abs(-2.9)) will return +ve


# If Statement
#is_hot = False
#is_cold = True

#if is_hot:
 #   print("It's a hot day")
 #   print("Drink plenty of water")
#elif is_cold:
 #   print("It's a cold day")
  #  print("Wear warm clothes")
#else:
  #  print("It's a lovely day")
#print("Enjoy your day")

#price = 1000000
#has_good_credit= True

#if has_good_credit:
 #   down_payment = 0.1 * price
#else:
   # down_payment = 0.2 * price
#print(f"Down payment: {down_payment}")

#has_high_income = True
#good_credit = True

#if has_high_income and good_credit:
#    print("Eligible for loan")
#else:
#    print("apply next time")

#LOGICAL OPERATORS ; and; or; and not.

#COMPARISON OPERATORS

#name = 'Bashir'
#if len(name) < 3:
 #   print('name must be at least 3 three characters')
#elif len(name) > 50:
#    print ('name can be a maximum of 50 characters')
#else:
#    print('name looks good!')

#Weight converter

#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)g: ')
#if unit.upper() == "L":
 #   converted = weight * 0.45
 #   print(f"You are {converted} kilos")
#else:
  #  converted = weight / 0.45
  #  print(f"You are {converted} pounds")

#WHILE LOOP
#i = 1
#while i <= 5:
#    print(i)
#    i = i +1
#print("Done")

#i = 1
#while i <= 5:
#    print('*' * i)
#    i = i +1
#print("Done")

#Guessing Game
#secret_number = 9
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
 #   guess = int(input('Guess: '))
 #   guess_count += 1
 #   if guess == secret_number:
 #       print('You won!')
  #      break
#else:
  #  print('Sorry you failed!')

  #CAR GAME
#command = ""
#started = False
#while True:
#    command = input("> ").lower()
#    if command == "start":
#        if started:
#            print("car is already started")
#        else:
#            started = True
#            print("Car started")
#    elif command == "stop":
#        if not started:
#           print("car is already stopped!")
#       else:
#            started = False
#        print("car stopped")
#    elif command == "help":
#        print("""
#   start- to start the car
#   stop- to stop the car
#   quit- to quit
#        """)
#    elif command == "quit":
#        break
#else:
#    print("I don't understand")

#FOR LOOPS
#for item in "python": OR  for item in ['Mosh', 'John', 'Sarah']:
#    print(item)
#for item in [1, 2, 3, 4]: OR for item in range(10): OR for item in range(5, 10):
#    print(item)

#prices = [10, 20, 30]
#total = 0
#for price in prices:
#    total += price
#print(f"Total: {total}")

#Nested Loop
#for x in range(4):
#    for y in range(3):
#        print(f"({x}, {y})")

#numbers = [5, 2, 5, 2, 2]
#for number in numbers:
#    output = ''
#    for item in range(number):
#        output += 'x'
#    print(output)

#LIST
#numbers = [1, 5, 8, 10, 7, 34]
#max = numbers[0]
#for number in numbers:
#    if number > max:
#        max = number
#print(max)

#2D LIST
#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#matrix[0][2] = 20
#print(matrix[0[2]])

#for row in matrix:
#    for item in row:
 #       print(item)

#LIST METHODS
#numbers = [5, 2, 1, 5, 7, 4]
#numbers.append(); add new no at the end; numbers.insert(0, 5) will add 5 to the first position
#numbers.remove(5) will 5; numbers.clear() will clear everything
#numbers.count(5) will give number of occurence of item 5
#numbers.copy() will copy it. number.sort() will sort in ascending and can be in descending by numbwers.reverse()

# TO REMOVE DUPLICATE
#numbers = [5, 4, 7, 10, 5, 7, 12, 5, 4]
#uniques = []
#for number in numbers:
#    if number not in uniques:
#        uniques.append(number)
#print(f' Uniques: {uniques}')

#TUPLES. IS LIKE A LIST BUT CANNOT BE CHANGED/IMMUTABLE.
#numbers = (1, 2, 3)  this is a tuple. ()

#UNPACKING
#coordinates = (1, 2, 3)
#x, y, z = coordinates
#print( x, y, z)

#DICTIONARIES
'''
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
'''
'''
phone = input("Phone:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)
'''

'''coordinate_axis = [2, 4, 6, 8, 10]
maximum = coordinate_axis[0]
for coordinate in coordinate_axis:
    if maximum < coordinate:
        maximum = coordinate
print(f'Maximum cordinate: {maximum}')'''
'''
# Task 1
print("Hello")
print("how are you?")

x = ("apple", "banana", "cherry")
print(x)

#Task 2
my_name = "Bashir"
my_siblings = 10
print(my_name, my_siblings)

#Task 3
favorite_food = "Pounded yam"
number_name = 6
age_division = 2.5
a = 2 < 9
b = 14 > 100
print(type(favorite_food))
print(type(number_name))
print(type(age_division))
print(type(a))

#Task 4
#This is a single line comment
print("Hello World!")
print("Hello World!")# This is a comment after a code
#print("Hello World!") We can comment out a code

'''

'''
num1 = 12
num2 = 20
add_num = num1 + num2
sub_num = num1 - num2
mult_num = num1 * num2
div_num = num1 / num2
flo_div_num = num1 // num2
modu_num = num1 % num2
expo_num = num1 ** 2
print(add_num, sub_num, mult_num, div_num, flo_div_num, modu_num, expo_num)
'''
'''
message = input(">")
words = message.split(' ')
print(words)
'''
#FUNCTION
'''
def greet_user():
    print("Hi there")
    print("welcome aboard")

print("start")
greet_user()
print("finish")

#Parameters
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


print("start")
greet_user("Bashir", "Salako")
print("finish")'''
#Exception
'''
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid Value')'''
#CLASS - NOT understood
'''
#Task 1
length = 7
width = 4
area_of_rectangle = length * width
print(area_of_rectangle)

# Task 2
pi = 3.142
radius = 7
area_of_circle = pi * radius **2
print(area_of_circle)

#Task 3
pi = 3.142
length = 20
radius = 2.5
vol_of_cylinder = pi * radius ** 2 * length
print(vol_of_cylinder)

# Dont know the formula for cube. the one I saw is side**3
Task 4
base = 8
height = 12
area_of_triangle = 0.5 * 8 * 12
print(area_of_triangle)

Task 5
length = 20
thickness = 0.225
width = 5
vol_of_concrete = length * thickness * width
print(vol_of_concrete)
'''

