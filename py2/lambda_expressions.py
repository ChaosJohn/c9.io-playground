"""Lambda Expressions"""


def make_incrementor(increment):
    """make incrementor"""
    return lambda x: x + increment

F = make_incrementor(42)

print F(0)
print F(1)
print

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print pairs
