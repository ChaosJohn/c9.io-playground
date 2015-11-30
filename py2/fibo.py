"""Write a Fibonacci series up to max_num."""
def fib(max_num):
    """Print a Fibonacci series up to max_num."""
    first, second = 0, 1
    while first < max_num:
        print first,
        first, second = second, first + second

# Now call the fuction we just defined.
#fib(2000)
#print
#print fib(0)

#"""Write an another Fibonacci series up to max_num."""
def fib2(max_num):
    """Return a list containing the Fabonacci series up to max_num."""
    result = []
    var_a, var_b = 0, 1
    while var_a < max_num:
        result.append(var_a)
        var_a, var_b = var_b, var_a + var_b
    return result

#F100 = fib2(100)
#print F100

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))


