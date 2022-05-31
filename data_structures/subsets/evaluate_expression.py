"""
Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can
be evaluated by grouping the numbers and operators using parentheses.

example1:
    Input: "1+2*3"
    Output: 7, 9
    Explanation:
      1+(2*3) => 7
      (1+2)*3 => 9

example2:
    Input: "2*3-4-5"
    Output: 8, -12, 7, -7, -3
    Explanation:
      2*(3-(4-5)) => 8
      2*(3-4-5) => -12
      2*3-(4-5) => 7
      2*(3-4)-5 => -7
      (2*3)-4-5 => -3
"""


def different_ways_to_eval_expression(input_str: str):
    result = []
    if "+" not in input_str and "*" not in input_str and "-" not in input_str:
        result.append(input_str)
    else:
        for i in range(len(input_str)):
            char = input_str[i]
            if not char.isdigit():
                left_op = different_ways_to_eval_expression(input_str[:i])
                right_op = different_ways_to_eval_expression(input_str[i + 1 :])
                for l in left_op:
                    for r in right_op:
                        if char == "+":
                            result.append(int(l) + int(r))
                        elif char == "*":
                            result.append(int(l) * int(r))
                        else:
                            result.append(int(l) - int(r))

    return result


print(different_ways_to_eval_expression("1+2*3"))
# print(different_ways_to_eval_expression("2*3-4-5"))
