"""
Bucket sort is mainly useful when input is uniformly distributed over a range.
Sort a large set of floating point numbers which are in range from 0.0 to 1.0
and are uniformly distributed across the range.

bucketSort(arr[], n)
    1) Create n empty buckets (Or lists).
    2) Do following for every array element arr[i].
        a) Insert arr[i] into bucket[n*array[i]]
    3) Sort individual buckets using insertion sort.
    4) Concatenate all sorted buckets.
"""


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        hole = i
        current_val = nums[i]
        while hole > 0 and nums[hole - 1] > current_val:
            nums[hole] = nums[hole - 1]
            hole = hole - 1
        nums[hole] = current_val

    return nums


def bucket_sort(nums):
    """
    Bucket sort for input distributed uniformly between 0.0 and 1.0
    """
    bucket = []
    for num in nums:
        bucket.append([])

    n = len(nums)
    for num in nums:
        index = int(n * num)
        bucket[index].append(num)

    for i in range(len(bucket)):
        bucket[i] = insertion_sort(bucket[i])

    k = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            nums[k] = bucket[i][j]
            k += 1

    return nums


x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucket_sort(x))


"""
Pseudocode for bucket sort.

function bucketSort(array, k) is
    buckets ← new array of k empty lists
    M ← the maximum key value in the array
    for i = 0 to length(array) do
        insert array[i] into buckets[floor(k × array[i] / M)]
    for i = 0 to k do
        nextSort(buckets[i])
    return the concatenation of buckets[0], ...., buckets[k]

- Let array denote the array to be sorted and k denote the number of buckets to use.
- The function nextSort is a sorting function used to sort each bucket.
- The advantage of bucket sort is that once the elements are distributed into buckets, each bucket can be processed independently of the others.
- This means that you often need to sort much smaller arrays as a follow-up step than the original array.
- It also means that you can sort all of the buckets in parallel with one another.
- The disadvantage is that if you get a bad distribution into the buckets, you may end up doing a huge amount of extra work for no benefit or a minimal benefit.
"""
