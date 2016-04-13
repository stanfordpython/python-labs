
''' (1) Exploring Arguments and Parameters '''

def print_two(a, b):
	print("Arguments: {} and {}".format(a,b))

#print_two(4, 1, b=1) # invalid -- TypeError for passing multiple values for 'b'
#print_two(1, a=1) # invalid -- TypeError for passing multiple values for 'a'
#print_two(b=1, a=4) # valid
#print_two(a=4, b=1) # valid
#print_two(b=4, 1) # invalid -- SyntaxError for having non-keyword arg after keyword arg
#print_two(4, 1, 1) # invalid -- TypeError for passing 3 positional args instead of 2
#print_two(4, a=1) # invalid -- TypeError for passing multiple values for 'a'
#print_two(a=4, 1) # invalid -- SyntaxError for having non-keyword arg after keyword arg
#print_two(41) # invalid -- TypeError for omitting 1 required positional arg
#print_two(4, 1) # valid
#print_two() # invalid -- TypeError for omitting both required positional args



def bar(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

#bar(5) # valid
#bar(a=5) # valid, same output as above
#bar(5, 8) # valid
#bar(5, 2, c=4) # valid
#bar(5, 0, 1) # valid
#bar(5, 2, d=8, c=4) # valid
# bar(5, 2, 0, 1, "") # invalid -- TypeError for passing 5 args
# bar(c=7, 1) # invalid -- SyntaxError for passing non-keyword arg after keyword arg
# bar(c=7, a=1) # valid
# bar(5, 2, [], 5) # valid
# bar(1, 7, e=6) # invalid -- TypeError for passing unexpected keyword arg 'e'
# bar(1, c=7) # valid
# bar(5, 2, b=4) # invalid -- TypeError for passing multiple values for'b'

def baz(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

#baz(2, 3, 5, 7) # valid
    # output: 
    # Positional: (2, 3, 5, 7)
    # Keyword: {}


# baz(1, 1, n=1) # valid
    # output: 
    # Positional: (1, 1)
    # Keyword: {'n': 1}
# baz(n=1, 2, 3) # invalid -- SyntaxError for passing non-keyword arg after keyword arg
# baz() # valid
# baz(cs="Computer Science", pd="Product Design") # valid
# baz(cs="Computer Science", cs="CompSci", cs="CS") # invalid -- SyntaxError for repeating keyword arg
# baz(5, 8, k=1, swap=2) # valid
# baz(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'}) # invalid -- SyntaxError for double *
# baz(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'}) # valid
# baz(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'}) # invalid -- SyntaxError for double *
# baz({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'}) # valid
    #  output: 
    # Positional: ({'b': 'x', 'a': 5}, 'b', 'a')
    # Keyword: {'b': 'x', 'a': 5}

''' skipping optional part '''


''' (2) Writing Functions '''

def speak_excitedly(msg, numExclamations=1, capitalize=False):
    result = msg + '!' * numExclamations
    print(result if not capitalize else result.upper())

def average(*args):
    if not args: return 0   # avoid ZeroDivisionError if args is an empty tuple
    return sum(args) / len(args)

def make_table(**kwargs):
    longestKey = max([len(key) for key in kwargs.keys()])
    longestValue = max([len(val) for val in kwargs.values()])
    upperLowerBound = '=' * (longestValue + longestKey + 5)

    print(upperLowerBound)
    for k, v in kwargs.items():

        left = '|' + k + ' ' * (longestKey - len(k) + 1)
        right = ' ' * (longestValue - len(v) + 1) + v
        print(left, right
            , sep='|', end='|\n')

    print(upperLowerBound)


''' (3) Function Nuances '''

def say_hello():
    print("Hello!")

print(say_hello())  # => None

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())  # => None
print(echo(5)) # => 5
print(echo("Hello")) # => Hello

def drive(has_car):
    if not has_car:
        return
    return 100  # miles

print(drive(False))  # => None
print(drive(True)) # => 100











