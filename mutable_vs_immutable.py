"""
All the data in a Python code is represented by objects or by relations between objects. 
Every object has an identity, a type, and a value.

Identity:- An object's identity never changes once it's been created. you may think of it as the object's address in memory. 
The "is" operator compares the identity of two objects; the id() function returns an integer representing its identity.

Type:- An object's type defines the possible values and operations (e.g. "does it have a length?") that type supports.

Value:- The value of some objects can change. Objects whose value can change are said to be mutable; 
objects whose value is unchangeable once they are created are called immutable.

mutable :- list, dictionary, set and user-defined classes
immutable :- int, float, decimal, bool, string, tuple, and range
"""

list_values = [1, 2, 3]  # list
set_values = (10, 20, 30)  # tuple
print(list_values[0])
print(set_values[0])

list_values[0] = 100
print(list_values)
# set_values[0] = 100 # error


# Tuple vs List Expanding
print()
print("Tuple vs list expanding")
print()
list_values = [1, 2, 3]
set_values = (1, 2, 3)
print(list_values)
print(set_values)
print(id(list_values))  # 4423663040
print(id(set_values))  # 4423412992
print()

list_values += [4, 5, 6]
set_values += (4, 5, 6)
print(list_values)
print(set_values)
print(id(list_values))  # 4423663040
print(id(set_values))  # 4423604544

"""
We can see that the list identity is not changed, while the tuple identity is changed. 
This means that we have expanded our list, but created a completely new tuple. Lists are more memory efficient than tuples.
"""


# Other Immutable Data Type Examples

print()
number = 42
print(id(number))

number += 1
print(id(number))

print()

text = "Data Science"
print(id(text))

text += " with Python"
print(id(text))


"""
We see that both for the number and text variables, their identity is changed. 
This means that new variables are created in both cases.

"""

# Copying Mutable Objects by Reference
print()
values = [4, 5, 6]
values2 = values
print(id(values))
print(id(values2))

values.append(7)
print(values is values2)
print(values)
print(values2)

# Copying Immutable Objects
print()
text = "Python"
text2 = text
print(id(text))
print(id(text2))
print(text is text2)
print()

text += " is awesome"
print(id(text))
print(id(text2))
print(text is text2)
print()

print(text)
print(text2)

"""
Every time when we try to update the value of an immutable object, a new object is created instead.
"""


# The == operator

"""
Sometimes we don’t want to compare the identity of two objects, but to compare the values of these objects
"""
print()
numbers = [1, 2, 3]
numbers2 = [1, 2, 3]
print(numbers == numbers2)
print(numbers is numbers2)

# Immutable Object Changing Its Value
"""
Value of an immutable container that contains a reference to a mutable object can be changed if that mutable object is changed.
"""
print()
skills = ["Programming", "Machine Learning", "Statistics"]
person = (129392130, skills)
print(type(person))
print(person)

skills[2] = "Maths"
print(person)

"""
However, if your immutable object contains only immutable objects, we cannot change their value.
"""
print()
unique_identifier = 42
age = 24
skills = ("Python", "pandas", "scikit-learn")
info = (unique_identifier, age, skills)
print(id(unique_identifier))
print(id(age))
print(info)

unique_identifier = 50
age += 1
skills += ("machine learning", "deep learning")
print(id(unique_identifier))
print(id(age))
print(info)
