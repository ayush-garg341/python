"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is
equal to the target number.

example1:
    Input: [4, 1, 2, -1, 1, -3], target=1
    Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
    Explanation: Both the quadruplets add up to the target.

example2:
    Input: [2, 0, -1, 1, -2, 2], target=2
    Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
    Explanation: Both the quadruplets add up to the target.
"""


def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    n = len(arr)
    for i in range(0, n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            start = j + 1
            end = len(arr) - 1

            while start < end:
                actual_sum = arr[i] + arr[j] + arr[start] + arr[end]

                if actual_sum == target:
                    quadruplets.append([arr[i], arr[j], arr[start], arr[end]])

                    start += 1
                    end -= 1

                    while arr[start] == arr[start - 1] and start < end:
                        start += 1

                    while arr[end] == arr[end + 1] and start < end:
                        end -= 1

                elif actual_sum > target:
                    end -= 1

                else:
                    start += 1

    return quadruplets


print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))
