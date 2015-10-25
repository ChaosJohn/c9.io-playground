"""A third argument can be passed to indicate the starting value"""

def sum_by_reduce(seq, starting_value):
    """the sum function using reduce"""
    def add(var_a, var_b):
        """add function"""
        return var_a + var_b

    return reduce(add, seq, starting_value)

print sum_by_reduce(range(1, 11), 0)
print sum_by_reduce(range(1, 11), 2)
print sum_by_reduce([], 999)

