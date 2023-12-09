"""
Given that a string, s, contains digits, return a list of all possible valid IP addresses that can be obtained from the string.
"""


def restore_ip_addresses(string: str):
    result = []
    generate_ip_addresses_rec(string, 0, 0, "", result)
    return result


def generate_ip_addresses_rec(ip, current_idx, dot_count, current_ip, result):
    if dot_count == 3:
        if is_valid_octet(ip[current_idx:]):
            result.append(current_ip + ip[current_idx:])
            return

    else:
        octet = ""
        for i in range(current_idx, min(current_idx + 3, len(ip))):
            octet += ip[i]
            if is_valid_octet(octet):
                generate_ip_addresses_rec(
                    ip, i + 1, dot_count + 1, current_ip + octet + ".", result
                )


def is_valid_octet(octet):
    if len(octet) == 0:
        return False
    dec = int(octet)
    if dec > 255:
        return False
    if dec >= 0 and dec <= 9:
        if len(octet) == 1:
            return True
    if dec >= 10 and dec <= 99:
        if len(octet) == 2:
            return True
    if dec >= 100 and dec <= 255:
        if len(octet) == 3:
            return True
    return False


print(restore_ip_addresses("25525525512"))
print(restore_ip_addresses("199219239"))
