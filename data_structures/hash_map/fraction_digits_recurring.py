"""
Given the two integer values of a fraction, numerator and denominator,
implement a function that returns the fraction in string format.
If the fractional part repeats, enclose the repeating part in parentheses.

ex:- 2/4 = "0.5"
8/666 = 0.012012012 = "0.(012)"
5/333 = 0.015015015 = "0.(015)"
"""


def fraction_recurring(num, denom):
    result, fraction = "", dict()
    if num == 0:
        return "0"
    if num < 0 or denom < 0:
        result += "-"
        num = abs(num)
        denom = abs(denom)

    quotient = num // denom
    rem = (num % denom) * 10
    result += str(quotient)
    if rem == 0:
        return result
    result += "."
    while rem != 0:
        if rem in fraction.keys():
            start = fraction[rem]
            left = result[0:start]
            right = result[start:]
            return left + "(" + right + ")"
        fraction[rem] = len(result)
        quotient = rem // denom
        rem = (rem % denom) * 10
        result += str(quotient)

    return result


print(fraction_recurring(5, 333))
print(fraction_recurring(8, 666))
print(fraction_recurring(2, 4))
