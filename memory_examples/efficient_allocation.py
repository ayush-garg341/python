"""
memray run -fo test.bin memory_examples/efficient_allocation.py
memray summary test.bin --temporary-allocations

"""


def foo(n):
    return [None] * n


foo(1_000_000)
