"""
Remove min parenthesis to make valid Parenthesis string.
"""


def min_remove_parentheses(s):
    stack_paren = []
    s_list = list(s)
    for idx in range(len(s)):
        char = s[idx]
        if char == ")":
            if len(stack_paren) and stack_paren[-1][0] == "(":
                stack_paren.pop()
            else:
                stack_paren.append((char, idx))
        elif char == "(":
            stack_paren.append((char, idx))

    for idx in stack_paren:
        s_list[idx[1]] = ""

    return "".join(s_list)


print(min_remove_parentheses("(((abc)(to)((q)()("))
