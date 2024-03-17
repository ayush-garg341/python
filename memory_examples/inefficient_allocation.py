def foo(n):
    x = []
    for _ in range(n):
        x.append(None)
    return x


foo(1_000_000)
