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


def gen_valid_paren(num):
    result = []
    gen_valid_paren_rec(num, "", 0, 0, result)
    return result


def gen_valid_paren_rec(num, string, open_count, close_count, result):
    if close_count == num and open_count == num:
        result.append(string)
    else:
        if open_count < num:
            gen_valid_paren_rec(num, string + "(", open_count + 1, close_count, result)

        if close_count < open_count:
            gen_valid_paren_rec(num, string + ")", open_count, close_count + 1, result)


def main():
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(3)))

    print(" ================================ ")
    print("All combinations of balanced parentheses are: " + str(gen_valid_paren(2)))
    print("All combinations of balanced parentheses are: " + str(gen_valid_paren(3)))


main()
