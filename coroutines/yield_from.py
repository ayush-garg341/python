def parse_number():
    digits = []

    while True:
        ch = yield
        if ch.isdigit():
            digits.append(ch)
        else:
            break

    return int("".join(digits))


def parser():
    while True:
        result = yield from parse_number()
        print("Parsed number: ", result)


p = parser()
next(p)
for c in "123x45y":
    p.send(c)
