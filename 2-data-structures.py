# Yeah, I know. What I'm doing is super basic. I haven't coded in years, since I've been working
# as an IT Technician / IT Support / System Administrator. I'm doing this for practice.

# List is represented by opening and closing bracket
my_list = [1,2,3,4]
print(my_list)

# you can have integers, strings, floats, booleans, or another list inside a list
# you can have nested lists
my_list_02 = ["banana", False, 24]
print(len(my_list_02))
# len() count how many values are inside the list


my_list_03 = [[1,2,3],[False,True],["basketball","football"]]

# the order of the elements inside a list is important if it is compared to another list

###################################################################################################

# Set is almost identical to list, except that all of the elements in it have to be unique
# curly bracket is used
my_set = {1, 2, 3, 4, 5}
print(my_set)

###################################################################################################

# Tuples is similar to list, but they are enclosed by parenthesis
# order also matters in tuple when comparing to another tuple
# you cannot modify tuples
# once a tuple is declared, you can't add to it or change any of the values in it
# Tuples are used because they are memory efficient
# It uses only exactly the amount of memory it needs, good for storing little things like coordinates
my_tuple = (1,2,3)

###################################################################################################

# Dictionaries in python is similar to dictionaries in real world
# the keys in dictionaries need to be unique
# uses curly brackets
my_dictionary = {
    "apple": "A red fruit",
    "banana": "Contains lots of potassium"
}

print(my_dictionary["apple"])






