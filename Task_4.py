# This is learning how to use index and some in-built methods
#Q Hello there, how old are you? what index will return how old?
# Answer index [13:20]
# Solution
question = "Hello there, how old are you? what index will return how old?"
print(question[13:20])

#Q story = "Python is Awesome" What is story[2:4] + story[-1]
#Ans- the
story = "Python is Awesome"
print(story[2:4] + story[-1])

#Q my_string = "python rocks"- What is length of my_string
# Ans = 12
my_string = "python rocks"
print(f'The length of my string is {len(my_string)}')

#Q flower = "Rose". What is flower[0] = P; print(flower). Will it return "Pose"
#Ans- No. Because Rose is a string

#Q word = "Python is so cool"- What is word[-4:] * 3
#Ans coolcoolcool

#Q Write a code that returns macdonald as MacDonald
#sol
name = "mac donald"
print(name.title())

#Q Write a code that retuns "pepsi" as "PEPSI"
drink_brand = "pepsi"
print(drink_brand.upper())

# Q write a code that returns "MUSHRAH" as "mushrah"
player_name = "MUSHRAH"
print(player_name.lower())

#Q Using the built-in method, how will you return "Hello World" as a list
greetings = "Hello word"
print(greetings.split())

#Q How do I add a "-" in between every character in a string "Python is cool"
my_strings = "Python is cool"
my_stringss = "-".join(my_strings)
print(my_stringss)

#Q How do I remove Hello from "Hello World"
# Answer: By slicing
#solution
remove_hello = "Hello world"
print(remove_hello[6:])

#Q What is the index of first character in a string
#Ans = 0

#Q Print the number of "o" in the string: "Hello, python is sooo cool"
no_of_o = "Hello, python is sooo cool"
print(no_of_o.count("o"))

'''Q if i want to write this string: "hello world! welcome to Python" as a title case, what inbuilt method will be called'''
# Ans: .title()

#Q convert this string to a title case: "hello world! welcome to Python"
title_conversion = "hello world! welcome to Python"
print(title_conversion.title())