"""
You are given a sorted array of integers, nums, and two integers, target and k.
Your task is to return k number of integers that are close to the target value, target.
The integers in the output array should be in a sorted order.
"""

# Naive solution
def find_closest_elements(nums, k, target):

    # Replace this placeholder return statement with your code
    result = []
    distances = []
    for num in nums:
        distances.append([abs(target - num), num])
    distances.sort(key = lambda x: x[0])
    print(distances)
    for i in range(k):
        result.append(distances[i][1])

    result.sort(key=lambda x: x)
    return result

print(find_closest_elements([25, 41, 81, 85, 103, 117, 319], 3, 99))

# Better solution
def find_closest_elements_better(nums, k, target):
    pass
