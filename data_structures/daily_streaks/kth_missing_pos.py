"""
We have an array called nums with positive sorted strictly increasing values, and also have an integer k.
We have to find the kth positive integer that is missing from this array.

example1:
    input = [1,2,4,8,12], k = 6
    [3,5,6,7,9,10,11], here the 6th term is 10
"""


def find_kth_missing_sorted_array(nums, k):
    num = 1
    count = 0
    while count < k:
        if num not in nums:
            count += 1
        if count == k:
            return num
        num = num + 1

    return num


print(find_kth_missing_sorted_array([1, 2, 4, 8, 12], 6))
print(find_kth_missing_sorted_array([1, 2, 3, 4, 5, 6, 7, 8], 4))
