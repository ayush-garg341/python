def calculator(s):
    stack = []
    result = 0
    number = 0
    sign = 1
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char in "+-":
            result += number * sign
            sign = 1 if char == "+" else -1
            number = 0
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = 0
        elif char == ")":
            result += number * sign
            pop_sign = stack.pop()
            result *= pop_sign
            second_val = stack.pop()
            result += second_val
            number = 0

    return result + sign * number


print(calculator("1+2"))
print(calculator("4 + (52 - 12) + 99"))
