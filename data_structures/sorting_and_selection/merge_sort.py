def merge_sort(nums, low, high):
    if high <= low:
        return
    mid = (low + high) // 2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid + 1, high)
    merge(nums, low, mid, high)


def merge(nums, low, mid, high):
    aux_arr = [0] * len(nums)
    i, j = low, mid + 1
    count = low
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            aux_arr[count] = nums[i]
            i += 1
        else:
            aux_arr[count] = nums[j]
            j += 1
        count += 1

    while i <= mid:
        aux_arr[count] = nums[i]
        i += 1
        count += 1

    while j <= high:
        aux_arr[count] = nums[j]
        j += 1
        count += 1

    i = low
    while i < count:
        nums[i] = aux_arr[i]
        i += 1


nums = [85, 24, 63, 45, 17, 31, 96, 50]
merge_sort(nums, 0, len(nums) - 1)
print(nums)

nums = [-4, -5, -2, -1, -3]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
