def reverseWordsInString(string):
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
