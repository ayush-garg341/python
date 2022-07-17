def reverseWordsInString(string):
    """
    Reserve all the spaces and their numbers as well.
    """
    # Write your code here.
    aux_string = ""
    result_str = ""
    n = len(string)
    if n == 1:
        return string
    for i in range(n - 1, -1, -1):
        aux_string += string[i]

    word = False
    start = 0
    for i in range(0, len(aux_string)):
        if aux_string[i] == " ":
            if word:
                for x in range(i - 1, start - 1, -1):
                    result_str += aux_string[x]
            result_str += " "
            word = False
        else:
            if not word:
                start = i
                word = True

    if word:
        for x in range(n - 1, start - 1, -1):
            result_str += aux_string[x]

    return result_str


print("'{0}'".format(reverseWordsInString("    Ayush Garg")))


def reverseWords(s: str) -> str:
    """
    Trim the trailing and leading spaces from the reversed string and if multiple spaces are present, trim down to single one.
    """
    word = False
    processed_str = ""
    result_str = ""
    n = len(s)
    for i in range(n - 1, -1, -1):
        char = s[i]
        if char == " ":
            if len(processed_str) == 0:
                continue
            else:
                if not word:
                    continue
                else:
                    processed_str += char
            word = False
        else:
            processed_str += char
            word = True

    # if processed_str[-1] == " ":
    #     processed_str = processed_str[0: len(processed_str)-1]

    word = False
    start = 0
    n = len(processed_str)
    for i in range(n):
        if processed_str[i] == " ":
            if word:
                for j in range(i - 1, start - 1, -1):
                    result_str += processed_str[j]
            word = False
            if i != n - 1:
                result_str += " "
        else:

            if not word:
                start = i
                word = True
    if word:
        for i in range(n - 1, start - 1, -1):
            result_str += processed_str[i]
    return result_str


print("'{0}'".format(reverseWords("    Ayush   Garg  ")))
