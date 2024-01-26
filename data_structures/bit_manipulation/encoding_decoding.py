"""
Encoding string to transfer over the network.
"""


def encode(strings):
    # Replace this placeholder return statement with your code
    encoded = ""
    for string in strings:
        encoded += str(len(string)) + "/" + string
    return encoded


def decode(string):
    # Replace this placeholder return statement with your code
    decoded = []
    i = 0
    while i < len(string):
        e = ""
        while i < len(string) and string[i] != "/":
            e += string[i]
            i += 1
        length = int(e)
        decoded.append(string[i + 1 : i + 1 + length])
        i += length + 1

    return decoded


ec = encode(["I", "love", "educative"])
dc = decode(ec)
print(dc)

ec = encode(["6^Hello_5", "5_World^6"])
dc = decode(ec)
print(dc)
