"""
You are given a string of len 12 or smaller, containing only digits.
Write a function that returns all the possible IP addresses that can be created by inserting 3 dots .

An IP address is not valid if any of the individual integers contains leading 0.
Each individual integer is within the range 0-255, inclusive.
ex. "192.168.00.1" and "192.168.0.01" are invalid IP addresses.

ex. input -> "1921680"
    output -> [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0",
        ]
"""


def gen_valid_ip_add(string):
    result = []
    gen_valid_ip_add_rec(string, 0, 0, "", result)
    return result


def gen_valid_ip_add_rec(string, current_idx, dot_count, current_ip, result):
    if dot_count == 3:
        temp_num = string[current_idx:]
        if is_valid(temp_num):
            current_ip += temp_num
            result.append(current_ip)
        return
    else:
        temp_num = ""
        for i in range(current_idx, min(current_idx + 3, len(string))):
            temp_num += string[i]
            if is_valid(temp_num):
                gen_valid_ip_add_rec(
                    string, i + 1, dot_count + 1, current_ip + temp_num + ".", result
                )


def is_valid(num):
    if num == "":
        return False
    dec = int(num)
    if 0 <= dec and dec < 10:
        if len(num) == 1:
            return True
    elif 10 <= dec and dec < 100:
        if len(num) == 2:
            return True
    elif 100 <= dec and dec <= 255:
        if len(num) == 3:
            return True
    else:
        return False


result = gen_valid_ip_add("1921680")
print(result)
print(len(result))
