"""
Not a comparison based algorithm.
Sorts the elements by first grouping the individual digits of the same place value.
Based on radix (base) of number system.
base = 10, create 10 buckets and put the elements in there.
base = 2, create 2 buckets and put the elements in there.

Find the max digit in array and count the number of digits in it.
Iterate that many times, based on lsb to msb digit.

ex. arr = [243, 225]
max digit = 243, no of digits = 3
lsb = 3 => put it in bucket num 3
then = 4 => puit it in bucket num = 4
then = 1 => put it in bucket num = 2

Do the same for 225 and rest of the numbers and finally take them out of bucket and put them in original array.
This is a stable algorithm and lexicographically (alphabetically) sort the elements.

We put elements from original array to bucket and then from bucket to original array.
We repeat this no of digit times in max number.
Time complexity -> O(d.n)
"""


def radix_sort(nums):
    max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]

    number_of_digits = 0
    while max != 0:
        max //= 10
        number_of_digits += 1

    divisor = 1
    while number_of_digits:
        bucket = []
        for i in range(10):
            bucket.append([])
        for num in nums:
            index = int(num / divisor) % 10
            bucket[index].append(num)

        k = 0
        for i in range(len(bucket)):
            for j in range(len(bucket[i])):
                nums[k] = bucket[i][j]
                k += 1

        divisor *= 10
        number_of_digits -= 1

    return nums


nums = [121, 432, 564, 23, 1, 45, 788]
print(radix_sort(nums))

nums = [237, 196, 259, 348, 152, 163, 235, 48, 36, 62]
print(radix_sort(nums))
