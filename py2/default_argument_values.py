"""Default Argument Values."""
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    """Ask Prompt"""
    while True:
        answer = raw_input(prompt)
        if answer in ('y', 'ye', 'yes'):
            return True
        if answer in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint


I = 5
def f_2(arg=I):
    """The default values are evaluated at the point of function definition in the defining scope."""
    print arg

I = 6
f_2()

def f_3(a, L=[]):
    L.append(a)
    return L

print f_3(1)
print f_3(2)
print f_3(3)

def f_4(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f_4(1)
print f_4(2)
print f_4(3)

print f_2.__doc__
