"""
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

example1:
    Input: N=2
    Output: (()), ()()

example2:
    Input: N=3
    Output: ((())), (()()), (())(), ()(()), ()()()
"""

from collections import deque


class Parenthesis:
    def __init__(self, string, open_count, close_count):
        self.string = string
        self.open_count = open_count
        self.close_count = close_count


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(Parenthesis("", 0, 0))
    while queue:
        p = queue.popleft()
        if p.open_count == num and p.close_count == num:
            result.append(p.string)
        else:
            if p.open_count < num:
                queue.append(Parenthesis(p.string + "(", p.open_count + 1, p.close_count))
            if p.close_count < p.open_count:
                queue.append(Parenthesis(p.string + ")", p.open_count, p.close_count + 1))
    return result


def main():
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(3)))


main()
