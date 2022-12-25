"""
Given a set of positive numbers (non zero) and a target sum ‘S’.
Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

example-1:
    Input: {1, 1, 2, 3}, S=1
    Output: 3
    Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

example-2:
    Input: {1, 2, 7, 1}, S=9
    Output: 2
    Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

Explanation: Need to find two subsets s.t S1-S2 = s
            We already know S1 + S2 = S
            Adding both equations:
                2*S1 = S + s
                S1 = (S + s)/2
"""


def find_target_subsets(arr, s):
    if any(i < 1 for i in arr):
        return -1  # invalid input, the problem expects only positive numbers

    # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
    total_sum = sum(arr)
    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0
    current_idx = 0
    return find_target_subsets_rec_brute_force(arr, current_idx, (s + total_sum) / 2)


def find_target_subsets_rec_brute_force(arr: list, current_idx: int, s: int) -> int:

    if s == 0:
        return 1

    if current_idx >= len(arr):
        return 0

    count = 0
    if arr[current_idx] <= s:
        count += find_target_subsets_rec_brute_force(
            arr, current_idx + 1, s - arr[current_idx]
        )

    count += find_target_subsets_rec_brute_force(arr, current_idx + 1, s)

    return count


print("=================== brute force recursive ============")
print(find_target_subsets([1, 1, 2, 3], 1))
print(find_target_subsets([1, 2, 7, 1], 9))
print(find_target_subsets([1, 2, 7, 1], 11))


def find_target_subsets_dp(arr, s):
    if any(i < 1 for i in arr):
        return -1

    total_sum = sum(arr)
    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0
    desired_sum = (s + total_sum) / 2
    current_idx = 0
    dp = [[0 for i in range(desired_sum + 1)] for j in range(len(arr))]
    return find_target_subsets_dp_top_bottom(arr, current_idx, desired_sum, dp)


def find_target_subsets_dp_top_bottom(arr: list, current_idx: int, s: int, dp: list):
    if s == 0:
        return 1

    if current_idx >= len(arr):
        return 0

    if dp[current_idx][s] == -1:
        count = 0
        if arr[current_idx] <= s:
            count += find_target_subsets_dp_top_bottom(
                arr, current_idx + 1, s - arr[current_idx], dp
            )

        count += find_target_subsets_dp_top_bottom(arr, current_idx + 1, s, dp)

        dp[current_idx][s] = count

    return dp[current_idx][s]


print("=================== top bottom dp recursive ============")
print(find_target_subsets([1, 1, 2, 3], 1))
print(find_target_subsets([1, 2, 7, 1], 9))
print(find_target_subsets([1, 2, 7, 1], 11))


# exact same solution will work for tabular approach as it worked in count subset sum
