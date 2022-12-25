"""
    defaultdict:
        The defaultdict is a subclass of Python’s dict that accepts a default_factory as its primary argument.
        The default_factory is usually a Python type, such as int or list, but you can also use a function or a lambda too.
"""

# Normal dict formation

from collections import defaultdict


sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(" ")

reg_dict = {}

for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)


# using default dict

reg_dict = defaultdict(int)
for word in words:
    reg_dict[word] += 1

print(reg_dict)


my_list = [
    (1234, 100.23),
    (345, 10.45),
    (1234, 75.00),
    (345, 222.66),
    (678, 300.25),
    (1234, 35.67),
]

reg_dict = {}

for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]

print(reg_dict)


reg_dict = defaultdict(list)
for acct_num, value in my_list:
    reg_dict[acct_num].append(value)

print(reg_dict)


animal = defaultdict(lambda: "Monkey")
animal["Sam"] = "Tiger"
print(animal["Nick"])
# Monkey

print(animal)

x = defaultdict(None)
x["Mike"]
