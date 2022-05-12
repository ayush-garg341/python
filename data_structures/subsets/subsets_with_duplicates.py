"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

example1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]

example2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
"""


def find_subsets_naive_wrong(nums):
    subsets = []
    if len(nums) == 0:
        return subsets
    subsets.append([])
    dup = set()
    dup.add("")
    for num in nums:
        n = len(subsets)
        for i in range(n):
            new_set = list(subsets[i])
            new_set.append(num)
            # if elements are same there order might be completely different and hence will get list with same elements
            # but with different order which is completely wrong.
            string = "-".join(str(elt) for elt in new_set)
            if string not in dup:
                subsets.append(new_set)
                dup.add(string)
    return subsets


def find_subsets(nums):
    subsets = []
    if len(nums) == 0:
        return subsets
    subsets.append([])
    nums.sort()
    old_set = []
    for i in range(len(nums)):
        if i > 0:
            if nums[i] != nums[i - 1]:
                old_set = []
                n = len(subsets)
                for j in range(n):
                    new_set = list(subsets[j])
                    new_set.append(nums[i])
                    old_set.append(new_set)
                    subsets.append(new_set)
            else:
                n = len(old_set)
                while n:
                    new_set = list(old_set.pop(0))
                    new_set.append(nums[i])
                    old_set.append(new_set)
                    subsets.append(new_set)
                    n -= 1

        else:
            new_set = list(subsets[i])
            new_set.append(nums[i])
            old_set.append(new_set)
            subsets.append(new_set)

    return subsets


def main():

    # print("Here is the list of subsets: " + str(find_subsets_naive_wrong([1, 3, 3])))
    # print("Here is the list of subsets: " + str(find_subsets_naive_wrong([1, 5, 3, 3])))

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 1])))
    print("Here is the list of subsets: " + str(find_subsets([1, 2, 2])))


main()
