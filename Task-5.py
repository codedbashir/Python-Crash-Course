# Create a list that contains  at least one string, one integer and one float
list_1 = [1, 'punch', 3.2, 15, 'guardian',]
print(f'This is a list that contains number, string and float {list_1}')

# Grab 2 from this list
grab = [1, 1, [1, 2]]
grab_2 = grab[2][1]
print(f"running this above code will grab {grab_2} from the list of item in {grab}")

# Using pop method
lst = [0, 1, 2]
use_pop = lst.pop()
print(f' This code will remove item {use_pop} and would make the oringinal list becomes {lst}')

#Q4: Yes

#Q5: if lst = ["a", "b", "c"] what is the result of lst[1:]
Ans = ["b", "c"]

#Q6 List is for collection of data with duplicate where as dictionary is used for key-value pair (no duplicate)

#Q7 
his_details = {
    "First Name": "Segun",
    "Last Name": "Oieza",
    "Age": 10
}

#Q8
player_scores = {
    'Player 1': 10,
    'Player 2': 12,
    'Player 3': 8
}

#Q9 No

#Q10 d= {"k1": [1, 2, 3]}. What is the output of d["k1"][1]t
d= {"k1": [1, 2, 3]}
print (d["k1"][1])

#Q11 Yes

#Q12
d = {'simple_key': 'hello'}
grab_hello = d['simple_key']
print(f" running this code will grab ({grab_hello}) from {d}")


# Q13
my_dicti = {'k1':{'k2': 'Hello'}}
print(my_dicti['k1']['k2'])

#Q14
my_dict = {"k1":[{'nest key':['this is deep',['hello']]}]}
print(my_dict['k1'][0]['nest key'][1][0])



#Q15
my_diction = {'k1':[1,2,{'k2':['this is tricky', {'tough':[1,2,['hello']]}]}]}
print(my_diction['k1'][2]['k2'][1]['tough'][2][0])
