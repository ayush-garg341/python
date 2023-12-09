"""
Repeatedly remove adjacent duplicate letters, one pair at a time.
Both members of a pair of adjacent duplicate letters need to be removed.
"""


def remove_duplicates(string):
    # Replace this placeholder return statement with your code
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        else:
            top = stack[-1]
            if top == char:
                stack.pop()
            else:
                stack.append(char)

    return "".join(stack)


print(remove_duplicates("azxxzy"))
