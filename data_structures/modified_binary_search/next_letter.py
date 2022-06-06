"""
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array
greater than a given ‘key’.
Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter.
This also means that the smallest letter in the given array is greater than the last letter of the array and is also
the first letter of the array.

Write a function to return the next letter of the given ‘key’.

example1:
    Input: ['a', 'c', 'f', 'h'], key = 'f'
    Output: 'h'
    Explanation: The smallest letter greater than 'f' is 'h' in the given array.
example2:
    Input: ['a', 'c', 'f', 'h'], key = 'b'
    Output: 'c'
    Explanation: The smallest letter greater than 'b' is 'c'.
example3:
    Input: ['a', 'c', 'f', 'h'], key = 'm'
    Output: 'a'
    Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
example4:
    Input: ['a', 'c', 'f', 'h'], key = 'h'
    Output: 'a'
    Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""


def search_next_letter(letters, key):
    if len(letters) == 0:
        return -1
    n = len(letters)
    if letters[n - 1] < key:
        return letters[0]
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if letters[mid] == key:
            return letters[(mid + 1) % n]
        elif key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % n]


def main():
    print(search_next_letter(["a", "c", "f", "h"], "f"))
    print(search_next_letter(["a", "c", "f", "h"], "b"))
    print(search_next_letter(["a", "c", "f", "h"], "m"))
    print(search_next_letter(["a", "c", "f", "h"], "h"))


main()
