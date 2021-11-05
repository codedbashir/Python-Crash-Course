# code to calculate mean age of boys
age_of_boys = (7, 10, 9, 8, 9, 10)
total_age = 0
for age in age_of_boys:
    total_age += age
average_age = total_age / 6
print(f'The average  age of boys is {average_age}')
