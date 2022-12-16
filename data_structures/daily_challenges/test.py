# This  is test file.

"""
input -> "python is my fav language"
output -> "language fav my is python"
"""


# def reverse_words_in_string(string):
# reverse_string = ""

# n = len(string)

# print("len of original string is : ", n)

# for i in range(n-1, -1, -1):
# reverse_string += string[i]

# print("len of reversed string is : ", len(reverse_string))

# reverse_word_by_word = ""

# start = -1
# end = -1
# white_space = True

# for j in range(n):
# if reverse_string[j] != " ":
# end += 1
# white_space = False
# else:
# if not white_space:
# for char in range(end, start, -1):
# reverse_word_by_word += reverse_string[char]
# white_space = True
# reverse_word_by_word += " "
# start = j
# end = j

# if not white_space:
# for char in range(end, start, -1):
# reverse_word_by_word += reverse_string[char]

# print("reverse word by word : ", len(reverse_word_by_word))

# return reverse_word_by_word

# # inp = "python is my fav language"
# # print(reverse_words_in_string(inp))

# # inp2 = "I love c  "
# # print(reverse_words_in_string(inp2))

# # inp3 = "  I hate JS  "
# # print(reverse_words_in_string(inp3))


# def find_permutation(string, pattern):
# pattern_dict = {}
# total_match = 0
# pattern_len = len(pattern)
# for char in pattern:
# if char not in pattern_dict:
# pattern_dict[char] = 0
# pattern_dict[char] += 1
# window_start = 0
# for window_end in range(len(string)):
# char = string[window_end]
# if char in pattern_dict:
# pattern_dict[char] -= 1
# if pattern_dict[char] == 0:
# total_match += 1

# if total_match == len(pattern_dict):
# return True
# if window_end - window_start + 1 == pattern_len:
# start_char = string[window_start]
# if start_char in pattern_dict:
# if pattern_dict[start_char] == 0:
# total_match -= 1
# pattern_dict[start_char] += 1
# window_start += 1

# return False

# # print(find_permutation("eidbaooo", "ab"))
# # print(find_permutation("ooolleoooleh", "hello"))
# # print(find_permutation("dcda", "adc"))


# def longest_subsseq(str1, str2):
# longest = longest_subsseq_rec(str1, str2, 0, 0)
# return longest

# def longest_subsseq_rec(str1, str2, i, j):
# if len(str1) == i or len(str2) == j:
# return 0

# if str1[i] == str2[j]:
# return 1 + longest_subsseq_rec(str1, str2, i+1, j+1)

# count1 = longest_subsseq_rec(str1, str2, i+1, j)
# count2 = longest_subsseq_rec(str1, str2, i, j+1)

# return max(count1, count2)

# # print(longest_subsseq("ZXVVYZW", "XKYKZPW"))
# # print(longest_subsseq("ABCDEFG", "APPLES"))

# from collections import deque

# def longest_subsseq_tabulation(str1, str2):
# n1 = len(str1)
# n2 = len(str2)

# dp = [[0 for j in range(n1+1)] for i in range(n2+1)]

# for i in range(1, n2+1):
# for j in range(1, n1+1):
# if str2[i-1] == str1[j-1]:
# dp[i][j] = 1 + dp[i-1][j-1]
# else:
# dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# output = deque()

# i = n2
# j = n1
# while i >= 1 and j >= 1:
# if dp[i][j] != dp[i-1][j] and dp[i][j] != dp[i][j-1]:
# output.appendleft(str2[i-1])
# i = i - 1
# j = j - 1
# else:
# if dp[i][j] == dp[i-1][j]:
# i = i-1
# elif dp[i][j] == dp[i][j-1]:
# j = j - 1
# return list(output)


# # print(longest_subsseq_tabulation("ZXVVYZW", "XKYKZPW"))
# # print(longest_subsseq_tabulation("ABCDEFG", "APPLES"))


# def longest_subsseq_tabulation_another_method(str1, str2):
# n1 = len(str1)
# n2 = len(str2)

# dp = [[[None, 0, None, None] for j in range(n1+1)] for i in range(n2+1)]

# for i in range(1, n2+1):
# for j in range(1, n1+1):
# if str2[i-1] == str1[j-1]:
# dp[i][j] = [str1[j-1], 1 + dp[i-1][j-1][1], i-1, j-1]
# else:
# if dp[i-1][j][1] > dp[i][j-1][1]:
# dp[i][j] = [None, dp[i-1][j][1], i-1, j]
# else:
# dp[i][j] = [None, dp[i][j-1][1], i, j-1]

# i = n2
# j = n1
# result = []
# while i!=0 and j!=0:
# current_record = dp[i][j]
# if current_record[0] is not None:
# result.append(current_record[0])
# i = current_record[2]
# j = current_record[3]
# return list(reversed(result))

# # print(longest_subsseq_tabulation_another_method("ZXVVYZW", "XKYKZPW"))
# # print(longest_subsseq_tabulation_another_method("ABCDEFG", "APPLES"))

# import math
# def minWindow(str1: str, pattern: str) -> str:
# pat_map = {}
# for char in pattern:
# if char not in pat_map:
# pat_map[char] = 0
# pat_map[char] += 1
# window_start = 0
# match_len = 0
# min_len = math.inf
# start_window = 0
# for window_end in range(len(str1)):
# char = str1[window_end]
# if char in pat_map:
# pat_map[char] -= 1
# if pat_map[char] == 0:
# match_len += 1

# while match_len == len(pat_map):
# start_char = str1[window_start]
# if start_char in pat_map:
# if pat_map[start_char] == 0:
# match_len -= 1
# pat_map[start_char] += 1
# if window_end - window_start + 1 < min_len:
# min_len = window_end - window_start + 1
# start_window = window_start
# # min_len = min(min_len, window_end - window_start + 1)
# window_start += 1
# substr = ""
# if min_len != math.inf:
# end = start_window + min_len
# return str1[start_window: end]
# return substr

# # print(minWindow("cabwefgewcwaefgcf","cae"))


# from typing import List
# def findSubstring(s:str, words: List[str]) -> List[int]:
# word_map = {}
# total_char_count = 0
# for word in words:
# for char in word:
# if char not in word_map:
# word_map[char] = 0
# total_char_count += 1
# word_map[char] += 1

# window_start = 0
# match_len = 0
# indices = []
# for window_end in range(len(s)):
# char = s[window_end]
# if char in word_map:
# word_map[char] -= 1
# if word_map[char] == 0:
# match_len += 1

# if match_len == len(word_map):
# # substr = s[window_start:window_start + total_char_count]
# individual_list = []
# word_len = len(words[0])
# for i in range(window_start, window_start+total_char_count, word_len):
# individual_list.append(s[i:i+word_len])

# # check for individual word if that's in substr
# found = True
# for word in words:
# if word not in individual_list:
# found = False
# break
# else:
# index = individual_list.index(word)
# individual_list.pop(index)
# if found:
# indices.append(window_start)

# if window_end - window_start + 1 >= total_char_count:
# start_char = s[window_start]
# if start_char in word_map:
# if word_map[start_char] == 0:
# match_len -= 1
# word_map[start_char] += 1

# window_start += 1

# return indices

# # print(findSubstring("barfoothefoobarman", ["foo","bar"]))
# # print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
# # print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))


# def backspace_compare(str1, str2):
# substr1 = []
# count_space = 0

# for i in range(len(str1)-1, -1, -1):
# if str1[i] == "#":
# count_space += 1
# else:
# if count_space:
# count_space -= 1
# else:
# substr1.append(str1[i])

# count_space = 0
# i = 0
# for j in range(len(str2)-1, -1, -1):
# if str2[j] == "#":
# count_space += 1
# else:
# if count_space:
# count_space -= 1
# else:
# if i < len(substr1) and substr1[i] == str2[j]:
# i += 1
# continue
# else:
# return False
# if i != len(substr1):
# return False
# return True
# # substr2.append(str2[j])

# # if len(substr1) != len(substr2):
# # return False
# # for i in range(len(substr1)):
# # if substr1[i] != substr2[i]:
# # return False

# # return True

# # print(backspace_compare("xy#z", "xzz#"))
# # print(backspace_compare("xy#z", "xyz#"))
# # print(backspace_compare("xywrrmp", "xywrrmu#p"))


# def backspace_compare_efficient(str1, str2):
# i = len(str1) - 1
# j = len(str2) - 1
# while i >= 0 or j >= 0:
# i = get_next_non_space_index(str1, i)
# j = get_next_non_space_index(str2, j)

# if i < 0 and j < 0:
# return True
# if i < 0 or j < 0:
# return False

# if str1[i] != str2[j]:
# return False

# i = i - 1
# j = j - 1

# return True

# def get_next_non_space_index(string, current_idx):
# count_space = 0
# while current_idx >= 0:
# if string[current_idx] == "#":
# count_space += 1
# elif count_space:
# count_space -= 1
# else:
# break

# current_idx -= 1

# return current_idx

# # print(backspace_compare_efficient("xy#z", "xzz#"))
# # print(backspace_compare_efficient("xy#z", "xyz#"))
# # print(backspace_compare_efficient("xywrrmp", "xywrrmu#p"))
# # print(backspace_compare_efficient("bbbextm", "bbb#extm"))


# def shortest_window_sort(arr):
# start = 1
# end = len(arr) - 1
# start_idx = end
# end_idx = 0
# while start <= end:
# if arr[start] < arr[start-1]:
# start_idx = start - 1
# break
# start += 1

# while end > 0:
# if arr[end-1] > arr[end]:
# end_idx = end
# break
# end -= 1

# if start_idx >= end_idx:
# return 0

# max_elt = -math.inf
# min_elt = math.inf
# for i in range(start_idx, end_idx + 1):
# if arr[i] > max_elt:
# max_elt = arr[i]
# if arr[i] < min_elt:
# min_elt = arr[i]

# # print(max_elt, min_elt)

# for i in range(len(arr)):
# if min_elt < arr[i]:
# start_idx = i
# break

# for j in range(len(arr)-1, -1, -1):
# if max_elt > arr[j]:
# end_idx = j
# break

# return end_idx - start_idx + 1


# print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
# print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
# print(shortest_window_sort([1, 2, 3]))
# print(shortest_window_sort([3, 2, 1]))


# def happy_number(num):
# sum_of_sqaures = sum_sqaures(num)
# sum_of_sqaures_next = sum_sqaures(sum_sqaures(num))
# if sum_of_sqaures == 1 or sum_of_sqaures_next == 1:
# return True
# while sum_of_sqaures != sum_of_sqaures_next:
# if sum_of_sqaures_next == 1 or sum_of_sqaures == 1:
# return True
# else:
# sum_of_sqaures = sum_sqaures(sum_of_sqaures)
# sum_of_sqaures_next = sum_sqaures(sum_sqaures(sum_of_sqaures_next))
# return False

# def sum_sqaures(num):
# s = 0
# while num != 0:
# digit = num % 10
# num = num // 10
# s += digit * digit
# return s

# print(happy_number(23))
# print(happy_number(12))


# def longest_palindromic_substring(s):
# n = len(s)
# dp = [[0 for i in range(n)] for j in range(n)]
# for i in range(n):
# dp[i][i] = 1

# for i in range(n-2, -1, -1):
# for j in range(i+1, n):
# if s[i] == s[j]:
# if dp[i+1][j-1] == j - (i+1):
# dp[i][j] = 2 + dp[i+1][j-1]
# else:
# dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# else:
# dp[i][j] = max(dp[i+1][j], dp[i][j-1])

# return dp[0][n-1]


# print(longest_palindromic_substring("abacab"))
# print(longest_palindromic_substring("aaa"))
# print(longest_palindromic_substring("abcdefghi"))
# print(longest_palindromic_substring("abccc"))
# print(longest_palindromic_substring("axcdxa"))
# print(" ============  ")

# def longest_palindromic_subseq(s):
# n = len(s)
# if n == 0:
# return 0
# dp = [[0 for i in range(n)] for j in range(n)]
# for i in range(n):
# dp[i][i] = 1

# for i in range(n-2, -1, -1):
# for j in range(i+1, n):
# if s[i] == s[j]:
# dp[i][j] = 2 + dp[i+1][j-1]
# else:
# dp[i][j] = max(dp[i+1][j], dp[i][j-1])

# return dp[0][n-1]

# print(longest_palindromic_subseq("axcdxa"))
# print(longest_palindromic_subseq("axcdexa"))
# print(longest_palindromic_subseq("abccc"))
# print(longest_palindromic_subseq("abcs"))

"""
Calculate maximum profit by buying stock on day and selling them on some other day.
"""
# def maximize_profit(prices) -> int:
# n = len(prices)
# dp = [0 for i in range(n)]
# min_so_far = prices[0]

# for i in range(1, n):
# if prices[i] > min_so_far:
# dp[i] = max(dp[i-1], prices[i] - min_so_far)
# else:
# min_so_far = min(prices[i], min_so_far)
# dp[i] = dp[i-1]

# return dp[n-1]

# print(maximize_profit( [7,1,5,3,6,4]))


"""
Generate valid pair of parentheses
"""
# def generate_possible_combinations(n) -> list:
# list_of_valid_parenthesis = []
# gen_parenthesis_rec(n, list_of_valid_parenthesis, "", 0, 0)
# return list_of_valid_parenthesis


# def gen_parenthesis_rec(n, list_of_valid_parenthesis, cur_str, open_paren, close_paren):
# if close_paren >= n:
# list_of_valid_parenthesis.append(cur_str)
# if close_paren < open_paren:
# gen_parenthesis_rec(n, list_of_valid_parenthesis, cur_str + ")", open_paren, close_paren + 1)
# if open_paren < n:
# for i in range(open_paren, n):
# cur_str += "("
# gen_parenthesis_rec(n, list_of_valid_parenthesis, cur_str + ")", i+1, close_paren+1)


# print(generate_possible_combinations(3))

# from collections import deque

# class Parenthesis:
# def __init__(self, str, open_paren, close_paren):
# self.str = str
# self.open_paren = open_paren
# self.close_paren = close_paren

# def generate_possible_combinations_bfs(n) -> list:
# result = []
# q = deque()
# q.append(Parenthesis("(", 1, 0))
# while len(q):
# pop = q.popleft()
# s = pop.str
# open_paren = pop.open_paren
# close_paren = pop.close_paren
# if close_paren < open_paren:
# new_s = s + ")"
# q.append(Parenthesis(new_s, open_paren, close_paren+1))
# if open_paren < n:
# str  = s + "("
# q.append(Parenthesis(str, open_paren+1, close_paren))

# if close_paren == n:
# result.append(s)

# return result
# print(generate_possible_combinations_bfs(3))


def triangle_sum_without_dp(triangle):
    return triangle_sum_without_dp_rec(triangle, 0, 0)


def triangle_sum_without_dp_rec(triangle, row, index):
    if row >= len(triangle):
        return 0
    if index >= len(triangle[row]):
        return 0

    sum1, sum2 = 0, 0
    sum1 += triangle[row][index] + triangle_sum_without_dp_rec(triangle, row + 1, index)

    sum2 += triangle[row][index] + triangle_sum_without_dp_rec(
        triangle, row + 1, index + 1
    )

    return min(sum1, sum2)


# print(triangle_sum_without_dp([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# print(triangle_sum_without_dp([[2], [3, 4]]))

import math


def triangle_sum_dp(triangle):
    dp = []
    for i in range(len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
            temp.append(math.inf)
        dp.append(temp)
    return triangle_sum_dp_rec(triangle, dp, 0, 0)


def triangle_sum_dp_rec(triangle, dp, row, index):
    if row >= len(triangle):
        return 0
    if index >= len(triangle[row]):
        return 0

    if dp[row][index] == math.inf:
        sum1, sum2 = 0, 0
        sum1 += triangle[row][index] + triangle_sum_dp_rec(triangle, dp, row + 1, index)
        sum2 += triangle[row][index] + triangle_sum_dp_rec(
            triangle, dp, row + 1, index + 1
        )

        dp[row][index] = min(sum1, sum2)

    return dp[row][index]


# print(triangle_sum_dp([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# print(triangle_sum_dp([[2], [3, 4]]))


def triangle_sum_top_bottoms(triangle):
    dp = []
    for i in range(len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
            temp.append(math.inf)
        dp.append(temp)

    min_sum = math.inf
    dp[0][0] = triangle[0][0]
    for row in range(1, len(triangle)):
        for index in range(len(triangle[row])):
            if index < len(triangle[row - 1]) and index > 0:
                dp[row][index] = triangle[row][index] + min(
                    dp[row - 1][index], dp[row - 1][index - 1]
                )
            elif index == 0:
                dp[row][index] = triangle[row][index] + dp[row - 1][index]
            elif index >= len(triangle[row - 1]):
                dp[row][index] = triangle[row][index] + dp[row - 1][index - 1]

    n = len(dp)
    for index in range(len(dp[n - 1])):
        min_sum = min(min_sum, dp[n - 1][index])

    return min_sum


# print(triangle_sum_top_bottoms([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# print(triangle_sum_top_bottoms([[2], [3, 4]]))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head, k):
    reverse = True
    temp = head
    start_node = head
    count = 0
    prev_to_temp = None
    not_reversed_head = None
    while temp:
        if reverse:
            count += 1
            prev_to_temp = temp
            temp = temp.next
            if count % k == 0:
                prev_to_temp.next = None
                new_temp_head = reverse_head(start_node)
                if count // k == 1:
                    new_head = new_temp_head
                else:
                    not_reversed_head.next = new_temp_head
                start_node.next = temp
                reverse = False
        else:
            count += 1
            prev_to_temp = temp
            temp = temp.next
            if count % k == 0:
                not_reversed_head = prev_to_temp
                start_node = temp
                if temp:
                    reverse = True

    print(reverse)
    if reverse:
        new_temp_head = reverse_head(start_node)
        not_reversed_head.next = new_temp_head
        start_node.next = temp
    return new_head


def reverse_head(head):
    temp = head
    prev = None
    while temp:
        temp = temp.next
        head.next = prev
        prev = head
        head = temp
    return prev


# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)
# head.next.next.next.next.next.next = Node(7)
# head.next.next.next.next.next.next.next = Node(8)

# print("Nodes of original LinkedList are: ", end="")
# head.print_list()
# result = reverse_alternate_k_elements(head, 3)
# print("Nodes of reversed LinkedList are: ", end="")
# result.print_list()


def rotate(head, rotations):
    temp_1 = head
    length = 0
    last_node = None
    while temp_1:
        length += 1
        last_node = temp_1
        temp_1 = temp_1.next
    actual_rot = length - (rotations % length)
    temp = head
    prev = None
    while actual_rot:
        prev = temp
        temp = temp.next
        actual_rot -= 1
    prev.next = None
    last_node.next = head
    return temp


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)


# print("Nodes of original LinkedList are: ", end="")
# head.print_list()
# result = rotate(head, 8)
# print("Nodes of rotated LinkedList are: ", end="")
# result.print_list()


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    return find_path_recursive(root, sequence, 0)


def find_path_recursive(root, seq, idx):
    if root is None or root.val != seq[idx] or idx >= len(seq):
        return False
    if (
        root.val == seq[idx]
        and idx == len(seq) - 1
        and root.left is None
        and root.right is None
    ):
        return True

    return find_path_recursive(root.left, seq, idx + 1) or find_path_recursive(
        root.right, seq, idx + 1
    )


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
