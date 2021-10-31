from contextlib import suppress

with suppress(FileNotFoundError):
    with open('abc.txt') as fobj:
        for line in fobj:
            print(line)