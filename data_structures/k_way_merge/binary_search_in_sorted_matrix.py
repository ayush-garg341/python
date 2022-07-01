"""
Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

example:
    Input: Matrix=[
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11]
      ],
      K=5
    Output: 7
    Explanation: The 5th smallest number in the matrix is 7.

Algorithm:
1. Rather than doing binary search on index, go on range search
2. Take middle number of start and end that might or might not be in matrix.
3. start -> samllest (0, 0)
4. end -> largest (N-1, N-1)
5. Count all numbers less than equal to middle.
6. lets assume smallest number greater than middle n1
7. Let's assume biggest number less than equal to middle n2
8. If count == k, then return n2 as kth smallest
9. if k < count, then reduce the range search with end = n2
10. if k > count then reduce the range search by making start = n1
"""


def find_Kth_smallest_using_binary_search(matrix, k):
    row = len(matrix)
    col = len(matrix[0])
    start = matrix[0][0]
    end = matrix[col - 1][col - 1]

    while start < end:
        mid = (start + end) // 2
        smaller, larger = matrix[0][0], matrix[row - 1][row - 1]
        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)
        if count == k:
            return smaller
        elif count > k:  # search smaller range
            end = smaller
        else:  # search higher range
            start = larger
    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = 0, n - 1
    while row < n and col >= 0:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            col -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += col + 1
            row += 1

    return count, smaller, larger


print("Kth smallest number is: " + str(find_Kth_smallest_using_binary_search([[1, 4], [2, 5]], 2)))

print("Kth smallest number is: " + str(find_Kth_smallest_using_binary_search([[-5]], 1)))

print("Kth smallest number is: " + str(find_Kth_smallest_using_binary_search([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

print(
    "Kth smallest number is: " + str(find_Kth_smallest_using_binary_search([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
)
