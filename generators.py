# example 1
print("----------------- sqaure nums using list ----------------------")


def square_nums(nums):
    result = []
    for num in nums:
        result.append(num * num)

    return result


nums = [1, 2, 3, 4, 5]
sq_nums = square_nums(nums)
print(sq_nums)

sq_nums = [x * x for x in nums]

print(sq_nums)

print("--------------------- using yield on list --------------------")


def square_yield_nums(nums):
    for num in nums:
        yield num * num  # generator


my_nums = square_yield_nums([1, 2, 3, 4, 5])
my_nums = (
    num * num for num in [1, 2, 3, 4, 5]
)  # this also works as generator, without using yield statement

print(my_nums)  # gives a generator
# print(list(my_nums)) # converting that generator to the list
print(next(my_nums))  # accessing elements using next
print("iterating over generator")
for num in my_nums:
    print(num)

print(list(my_nums))  # try running this

"""
    A list is stored in memory, which consumes huge space, if the list is big.
    But a generator does not compute the whole list, rather computes the next element on demand, rather than complete list
"""
