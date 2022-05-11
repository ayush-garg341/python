"""
Given a set with distinct elements, find all of its distinct subsets.

example1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]

example2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


def find_subsets(nums):
    subsets = []
    if len(nums) == 0:
        return subsets
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            new_set = list(subsets[i])
            new_set.append(num)
            subsets.append(new_set)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
