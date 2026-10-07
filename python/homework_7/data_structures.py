# Homework 7: Data Structures
# This program creates basic data structures (list, tuple, set, dict)
# and performs simple operations on them.

# Step 1: create a list of fruits
fruits = ['apple', 'banana', 'cherry', 'potato']

# Step 2: create a tuple of colors
colors = ('red', 'green', 'blue')

# Step 3: create a set of numbers from 1 to 3
numbers = {1, 2, 3}

# Step 4: create a dictionary of people (name as key, age as value)
person = {'Marharyta': 25}

# Step 5: add 'grape' to the fruits list
fruits.append('grape')

# Step 6: remove 'potato' from the fruits list
fruits.remove('potato')

# Step 7: check if 'apple' is in the fruits list and output the result
is_apple_in_fruits = 'apple' in fruits
print('Is apple in fruits?', is_apple_in_fruits)

# Step 8: calculate the length of the colors tuple and output it
colors_length = len(colors)
print('Number of colors:', colors_length)

# Step 9: add the number 4 to the numbers set
numbers.add(4)

# Step 10: add a new key-value pair (another person: name -> age)
person['Alex'] = 30

# Print the final data structures to see the results
print('Fruits:', fruits)
print('Numbers:', numbers)
print('Person:', person)
