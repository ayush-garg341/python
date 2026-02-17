def gen():
    try:
        val = yield
        yield val
        yield 1
        yield 2
    except ValueError:
        print("Caught value error inside generator")


g = gen()
next(g)
print(g.send(10))
print(next(g))
# g.close()
g.throw(ValueError)
