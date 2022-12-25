def balancedBrackets(string):
    # Write your code here.
    stack = []
    for char in string:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")" or char == "]" or char == "}":
            if stack:
                top = stack.pop()
                if (
                    (char == ")" and top == "(")
                    or (char == "]" and top == "[")
                    or (char == "}" and top == "{")
                ):
                    continue
            return False

    return len(stack) == 0


print(balancedBrackets("([])(){}(())()()"))
