"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space.

example1:
    Input: [1, 4, 4, 3, 2]
    Output: 4

example2:
    Input: [2, 1, 3, 3, 5, 4]
    Output: 3

example3:
    Input: [2, 4, 1, 4, 4]
    Output: 4
"""


def find_duplicate(nums):
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return nums[i]


print(find_duplicate([1, 4, 4, 3, 2]))
print(find_duplicate([2, 1, 3, 3, 5, 4]))
print(find_duplicate([2, 4, 1, 4, 4]))
print(find_duplicate([5, 5, 4, 3, 2, 1]))
print(find_duplicate([5, 4, 4, 3, 2, 1]))


"""
Challenge to do it without modifying input array and in O(1).

Slow and fast pointer approach
"""


def find_duplicate_without_modifying_nums(nums):
    slow = nums[0]
    fast = nums[nums[0]]

    # find meet point
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # find length of cycle
    current = nums[nums[slow]]
    length = 1
    while current != nums[slow]:
        current = nums[current]
        length += 1

    print("length = ", length)

    # find meeting point if known length of cycle i.e. advance the one pointer by length
    slow = nums[0]
    fast = nums[0]

    while length != 0:
        slow = nums[slow]
        length -= 1

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


print("====================================")
print(find_duplicate_without_modifying_nums([1, 4, 4, 3, 2]))
print(find_duplicate_without_modifying_nums([2, 1, 3, 3, 5, 4]))
print(find_duplicate_without_modifying_nums([2, 4, 1, 4, 4]))
print(find_duplicate_without_modifying_nums([5, 5, 4, 3, 2, 1]))
print(find_duplicate_without_modifying_nums([5, 4, 4, 3, 2, 1]))
