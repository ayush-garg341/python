import itertools


def averager():
    sum = float((yield))
    counter = itertools.count(start=1)
    while True:
        sum += yield sum / next(counter)


avg = averager()
next(avg)
print(avg.send(10))
print(avg.send(20))
print(avg.send(30))
avg.close()
