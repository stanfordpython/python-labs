#!/usr/bin/env python3 -tt
"""Reference solutions to Lab 4 for CS41: Hap.py Code.

As in lecture slides, a data source surrounded by angle brackets such as:

    <1, 2, 3>

is our notation for an iterable over those elements.

Revision history:
@sredmond 01-31-2019 Minor tweaks for W19
@sredmond 04-26-2016 Added challenge problem solutions
@sredmond 04-23-2016 Commented ALL the things
@sredmond 04-20-2016 Small changes to parallel lab changes
@sredmond 04-18-2016 Created
"""
import collections  # OrderedDict
import functools    # reduce, wraps
import inspect      # Signature
import itertools    # permutations, cycle, starmap, zip_longest
import operator     # mul
import math         # gcd
import random       # choice


####################
# Functional Tools #
####################


def test_map():
    """Practice writing transformations using `map`."""
    # ['12', '-2', '0'] -> [12, -2, 0]
    map(int, ['12', '-2', '0'])
    # ['hello', 'world'] -> [5, 5]
    map(len, ['hello', 'world'])
    # ['hello', 'world'] -> ['olleh', 'dlrow']
    map(lambda s: s[::-1], ['hello', 'world'])
    # range(2, 6) -> [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
    map(lambda n: (n, n ** 2, n ** 3), range(2, 6))
    # zip(range(2, 5), range(3, 9, 2)) -> [6, 15, 28]
    map(lambda l, r: l * r, zip(range(2, 5), range(3, 9, 2)))

def test_filter():
    # ['12', '-2', '0'] -> ['12', '0']
    filter(lambda x: int(x) >= 0, ['12', '-2', '0'])
    # ['hello', 'world'] -> ['world']
    filter(lambda x: x == 'world', ['hello', 'world'])
    # ['Stanford', 'Cal', 'UCLA'] -> ['Stanford']
    filter(lambda x: x[0] == 'S', ['Stanford', 'Cal', 'UCLA'])
    # range(20) -> [0, 3, 5, 6, 9, 10, 12, 15, 18]
    filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))

def lcm(*nums):
    return functools.reduce(lambda x, y: x * y // math.gcd(x, y), nums, 1)

make_change = lambda target, coins: ( (sum(map(lambda choice: make_change(target - choice, coins[1:]), range(0, target + 1, coins[0]))), 0))[0]

def fact(n):
    return functools.reduce(operator.mul, range(1, n+1))

def testfact():
    fact(3)
    fact(7)

## Custom Comparison
def testcomparisons():
    words = ['pear', 'cabbage', 'apple', 'bananas']
    min(words)  # => 'apple'
    words.sort(key=lambda s: s[-1])  # Alternatively, key=operator.itemgetter(-1)
    words  # => ['cabbage', 'apple', 'pear', 'bananas'] ... Why 'cabbage' > 'apple'?
    # Because the builtin sort is stable - even though they both have the smae
    # value after application of the key function, cabbage appears before apple
    # in the original list, so it also is before apple in the sorted list
    max(words, key=len)  # 'cabbage' ... Why not 'bananas'?
    # same reason
    x= min(words, key=lambda s: s[1::2])  # What will this value be?
    # bananas, since it's aaa under the action of the sort key
    print(x)

def highest_alphanumeric_score():
    def alpha_score(upper_letters):
        """Computes the alphanumeric sum of letters in a string.
        Prerequisite: upper_letters is composed entirely of capital letters.
        """
        return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

    # alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

    def two_best(words):
        words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
        return words[:2]

    print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))
    # => ['PyThOn', 'wOrLD']

def functional():
    """
    if score == 1:
        return "Winner"
    elif score == -1:
        return "Loser"
    else:
        return "Tied"
    """
    # return (score == 1 and "Winner") or (score == -1 or "Loser") or "Tied"

## Iterators
def iterator_consumption():
    it = iter(range(100))
    67 in it  # => True
    # After the above two lines are executed, the iterator has been
    # run until it finds the 67, that is, until the point when next(it)
    # returned 67

    next(it)  # => 68
    37 in it  # => False, and in searching runs the iterator to exhaustion
    next(it)  # => raises StopIteration

def test_itertools():
    for el in itertools.permutations('XKCD', 2):
        print(el, end=', ')
    # ('X', 'K'), ('X', 'C'), ('X', 'D'), \
    # ('K', 'X'), ('K', 'C'), ('K', 'D'), \
    # ('C', 'X'), ('C', 'K'), ('C', 'D'), \
    # ('D', 'X'), ('D', 'K'), ('D', 'C'), \

    # for el in itertools.cycle('LO'):
    #     print(el, end='')  # Don't run this one. Why not?
    # Loops infinitely! Prints out LOLOLOLOLO...

    itertools.starmap(operator.mul, itertools.zip_longest([3,5,7],[2,3], fillvalue=1))
    """ We'll figure out what this code does by looking from the inside out
    itertools.zip_longest([3, 5, 7], [2, 3], fillvalue=1) generates
        < (3, 2), (5, 3), (7, 1) >
    itertools.starmap(fn, iterable) is equivalent to
        (fn(*element) for element in iterable)
    In our case, this generates
        operator.mul(*(3, 2))  # => 6, and then
        operator.mul(*(5, 3))  # => 15, and then
        operator.mul(*(7, 1))  # => 7
    So what we get back is an iterator that generates
        < 6, 15, 7 >
    """

## Linear Algebra
def dot_product(u, v):
    assert len(u) == len(v)
    return sum(itertools.starmap(operator.mul, zip(u, v)))

def transpose(m):
    return tuple(zip(*m))

def transpose_lazy(m):
    return zip(*m)

def matmul(m1, m2):
    return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))

def matmul_lazy(m1, m2):
    return map(lambda row: (dot_product(row, col) for col in transpose(m2)), m1)

## Generator Expressions
"""
(1) Searching for a given entity in the entries of a 1TB database.
    Generator expression! We couldn't buffer the entire database in memory
    (where can you even buy 1TB of RAM?), and since we're searching for an
    entity, we only need to keep one element - the current element - in memory for comparison
(2) Calculate cheap airfare using journey-to-destination flight information.
(3) Finding the first palindromic Fibonacci number greater than 1,000,000.
(4) Determine all multi-word anagrams of user-supplied 1000-character-or-more strings (very expensive to do).
(5) Generate a list of names of Stanford students whose SUNet ID numbers are less than 5000000.
(6) Return a list of all startups within 50 miles of Stanford.
"""

## Generators
def generate_triangles():
    n = 0
    total = 0
    while True:
        total += n
        n += 1
        yield total

def triangles_under(n):
    for triangle in generate_triangles():  # Lazy generation
        if triangle >= n:
            break
        print(triangle)

## Functions in Data Structures
def make_divisibility_test(n):
    return lambda m: m % n == 0


def generate_composites():
    tests = []
    i = 2
    while True:
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
        # If not prime, then composite!
        else:
            yield i
        i += 1

def nth_composite(n):
    """ Pre: n > 0

    1 -> 4
    2 -> 6
    3 -> 8
    4 -> 9
    """
    g = generate_composites()
    for i in range(n - 1):
        next(g)
    return next(g)

# nth_composite(1000) # => 1197

## Nested Functions and Closures
"""
```
def outer():
    def inner(a):
        return a
    return inner

f = outer()
print(f)  # <function outer.<locals>.inner at 0x1044b61e0>
f(10)  # => 10

f2 = outer()
print(f2)  # <function outer.<locals>.inner at 0x1044b6268> (Different from above!)
f2(11)  # => 11
```

Both `f` and `f2` were created at different times. Each function was created (defined)
at the time when the `outer` function was called, once in the first place, once in the
second place.
Note: the above description is assuming a CPython implementation.
"""

"""
```
def outer(l):
    def inner(n):
        return l * n
    return inner

l = [1, 2, 3]
f = outer(l)
print(f(3))  # => [1, 2, 3, 1, 2, 3, 1, 2, 3]

l.append(4)
print(f(3))  # => [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
```

What's happening? `f`, when it was defined as `inner`, wrapped a closure around
a *reference* to the list object `l`. Closures don't copy the objects, but rather
copy the references to the enclosed objects. So, when the underlying list `l` changes
then when `f` executes and tries to resolve the name `l`, it find the original `l` object
which has been changed.
"""

## Decorators
def bind_args(function, *args, **kwargs):
    r"""Returns an map from the names of function's arguments to values given by *args and **kwargs

    This is more or less an implementation of Python argument bind semantics, but it's not super accurate
    ¯\_(ツ)_/¯
        For example, it doesn't resolve any closure elements or anything, because ahh that's awful

    First, positional arguments are bound

    If you're a student reading this, you can ignore this implementation.

    Pre: *args and **kwargs represent valid parameters
    """
    argspec = inspect.getfullargspec(function)
    sig = inspect.Signature.from_function(function)
    ba = sig.bind(*args, **kwargs)
    print(argspec, ba)
    bindings = ba.arguments.copy()
    # default values for keyword arguments
    if argspec.defaults:
        for var_name, default_value in zip(reversed(argspec.args), reversed(argspec.defaults)):
            if var_name not in bindings:
                bindings[var_name] = default_value
    # default values for keyword-only argument
    if argspec.kwonlydefaults:
        for var_name, default_value in argspec.kwonlydefaults.items():
            if var_name not in bindings:
                bindings[var_name] = default_value
    if argspec.varargs and argspec.varargs not in bindings:
        bindings[argspec.varargs] = tuple()
    if argspec.varkw and argspec.varkw not in bindings:
        bindings[argspec.varkw] = dict()
    return bindings

def print_args(function):
    """Decorate the given function to print out it's arguments and return val if not None

    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        bound_arguments = bind_args(function, *args, **kwargs)
        print("{name}({call})".format(
            name=function.__name__,
            call=', '.join("{}={}".format(arg, val) for arg, val in bound_arguments.items())
        ))
        retval = function(*args, **kwargs)
        if retval is not None:
            print("(return) {!r}".format(retval))
        return retval
    return wrapper

def test_print_args():
    @print_args
    def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
        """The all_together function from Lab 3."""
        pass

    # all_together(2)
    all_together(2, 5, 7, 8, indent=False)
    all_together(2, 5, 7, 6, indent=None)
    all_together()
    # all_together(indent=True, 3, 4, 5)
    # all_together(**{'indent': False}, scope='maximum')
    all_together(dict(x=0, y=1), *range(10))
    # all_together(**dict(x=0, y=1), *range(10))
    # all_together(*range(10), **dict(x=0, y=1))
    all_together([1, 2], {3:4})
    all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})
    all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
    # all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})


def cache(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in function._cache:
            return function._cache[key]
        retval = function(*args, **kwargs)
        function._cache[key] = retval
        return retval
    return wrapper

@cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1

def cache_challenge(max_size=None, eviction_policy='LRU'):
    assert eviction_policy in ['LRU', 'MRU', 'random']
    def decorator(function):
        function._cache = collections.OrderedDict()
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in function._cache:
                # Before accessing this element, move it to the MRU side
                # of the list
                function._cache.move_to_end(key)
                return function._cache[key]
            retval = function(*args, **kwargs)

            # Check for eviction
            if max_size and len(function._cache) == max_size:
                if eviction_policy == 'LRU':
                    function._cache.popitem(last=False)
                elif eviction_policy == 'MRU':
                    function._cache.popitem(last=True)
                else:
                    randkey = random.choice(list(function._cache.keys()))
                    function._cache.pop(randkey)
            # Now that we know there's space, insert the element
            function._cache[key] = retval
            return retval
        return wrapper
    return decorator

@cache_challenge(max_size=16, eviction_policy='LRU')
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1


def enforce_types(function):
    expected = function.__annotations__
    if not expected:
        return function
    assert(all(map(lambda exp: type(exp) == type, expected.values())))
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        bound_arguments = bind_args(function, *args, **kwargs)
        for arg, val in bound_arguments.items():
            if arg in expected and not isinstance(val, expected[arg]):
                print("(Bad Argument Type!) argument '{arg}={val}': expected {exp}, received {r}".format(
                    arg=arg,
                    val=val,
                    exp=expected[arg],
                    r=type(val)
                ))

        retval = function(*args, **kwargs)

        # Check the return value
        if 'return' in expected and not isinstance(retval, expected['return']):
            print("(Bad Return Value!) return '{ret}': expected {exp}, received {r}".format(
                ret=retval,
                exp=expected['return'],
                r=type(retval)
            ))
        return retval
    return wrapper

def test_enforce_types():
    @enforce_types
    def foo(a: int, b: str) -> bool:
        if a == -1:
            return 'Gotcha!'
        return b[a] == 'X'

    try:
        foo(3, 'XYZXYZ')  # => True
        foo(2, 'python')  # => False
        foo(1, 4)  # prints "(Bad Argument Type!) argument b=4: expected <class 'str'>, received <class 'int'>" and then crashes
        foo(-1, '')  # prints "(Bad Return Value!) return Gotcha!: expected <class 'bool'>, received <class 'str'>" and returns "Gotcha!"
    except TypeError:
        pass



def enforce_types_challenge(severity=1):
    assert severity in (0, 1, 2)
    if severity == 0:
        # Return a no-op decorator
        return lambda function: function

    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)

    def decorator(function):
        expected = function.__annotations__
        if not expected:
            return function
        assert(all(map(lambda exp: type(exp) == type, expected.values())))

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bound_arguments = bind_args(function, *args, **kwargs)
            for arg, val in bound_arguments.items():
                if arg in expected and not isinstance(val, expected[arg]):
                    msg("(Bad Argument Type!) argument '{arg}={val}': expected {exp}, received {r}".format(
                        arg=arg,
                        val=val,
                        exp=expected[arg],
                        r=type(val)
                    ))

            retval = function(*args, **kwargs)

            # Check the return value
            if 'return' in expected and not isinstance(retval, expected['return']):
                msg("(Bad Return Value!) return '{ret}': expected {exp}, received {r}".format(
                    ret=retval,
                    exp=expected['return'],
                    r=type(retval)
                ))
            return retval
        return wrapper
    return decorator


@enforce_types_challenge(severity=2)
def bar(a: list, b: str) -> int:
    return 0

@enforce_types_challenge()
def baz(a: bool, b: str) -> str:
    return ''

if __name__ == '__main__':
    """Runs each of the lab solution functions and prints the docstring"""
    test_map()
    test_filter()
    test_print_args()
