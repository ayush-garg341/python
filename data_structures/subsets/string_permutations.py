"""
Given a string, find all of its permutations preserving the character sequence but changing case.

example1:
    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52"

example2:
    Input: "ab7c"
    Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


def find_letter_case_string_permutations(string):
    permutations = []
    if len(string) == 0:
        return permutations
    permutations.append(string)
    for i in range(len(string)):
        if (string[i] <= "z" and string[i] >= "a") or (string[i] <= "Z" and string[i] >= "A"):
            n = len(permutations)
            for j in range(n):
                old_per = permutations[j][:]
                if old_per[i] == old_per[i].lower():
                    upper_case = old_per[:i] + old_per[i].upper() + old_per[i + 1 :]
                else:
                    upper_case = old_per[:i] + old_per[i].lower() + old_per[i + 1 :]
                permutations.append(upper_case)

    return permutations


def main():
    print("String permutations are: " + str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " + str(find_letter_case_string_permutations("ab7c")))
    print("String permutations are: " + str(find_letter_case_string_permutations("C")))


main()
