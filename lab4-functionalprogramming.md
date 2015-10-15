# Lab 4.2: Functional Programming

## Functional Tools
### Lambdas

Recall that lambda functions are anonymous, unnamed function objects created on the fly. As an example,

```Python
(lambda val: val ** 2)(5)  # => 25
(lambda x, y: x * y)(3, 8)  # => 24
(lambda s: s.upper())('pytHoN')  # => 'PYTHON'
```

Lambdas on their own aren't particularly useful, as you can see above. They're most often seen used as arguments to `map`, `filter` and as return values from higher-order functions.

### Map
Recall from class that `map(func, iterable)` applies a function over elements of an iterable.

Write statements using `map` that convert the following sequences from the left column to the right column:

From  | To
--- | ---
`['12', '-2', '0']` | `[12, -2, 0]`
`['hello', 'world']`  | `[5, 5]`
`['hello', 'world']`|`['olleh', 'dlrow']`
`range(2, 6)`|`[(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]`
`zip(range(2, 5), range(3, 9, 2))`|`[6, 15, 28]`

#### Using Multiple Iterables
The `map` function can accept a variable number of iterables as arguments. Thus, `map(func, iterA, iterB, iterC)` is equivalent to `map(func, zip(iterA, iterB, iterC))`. This can be used as follows:

```Python
map(int, ('10110', '0xCAFE', '42'), (2, 16, 10))  # generates 22, 51966, 42
```
*This works because* `int` *takes an optional second argument specifying the conversion base*

### Filter

Recall from class that `filter(pref, iterable)` keeps only those elements from an iterable that satisfy a predicate function.

Write statements using `filter` that convert the following sequences from the left column to the right column:

From  | To
--- | ---
`['12', '-2', '0']` | `[12, 0]`
`['hello', 'world']`  | `[5, 5]`
`['Stanford', 'Cal', 'UCLA']`|`['Stanford']`
`range(20)`|`[0, 3, 5, 6, 9, 10, 12, 15, 18]`

### Other Useful Tools

#### Module: `functools`
There is another utility in the `functools` module called `reduce`. This function is well-explained by the [official documentation](https://docs.python.org/3.4/library/functools.html#functools.reduce):

> `functools.reduce(function, iterable[, initializer])`
>> Apply `function` of two arguments cumulatively to the items of `iterable`, from left to right, so as to reduce the iterable to a single value. For example, `functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` calculates `((((1+2)+3)+4)+5)`. The left argument, `x`, is the accumulated value and the right argument, `y`, is the update value from the sequence. If the optional `initializer` is present, it is placed before the items of the sequence in the calculation, and serves as a default when the iterable is empty. If `initializer` is not given and `iterable` contains only one item, the first item is returned.

Use the `reduce` function to find the least common multiple of a arbitrary list of arguments. This can be accomplished in one line of Python.

```Python
from functools import reduce

def gcd(a, b):
    """Reference implementation of finding the
    greatest common denominator of two numbers"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    # Your implementation here: Use reduce and use only one line! 
```

#### Module: `operator`

Frequently, you might find yourself writing anonymous functions similar to `lambda x, y: x + y`. This feels a little redundant, since Python already knows how to add two values together. Unfortunately, we can't just refer to `+` as a function - it's a builtin syntax element. To solve this problem, The `operator` module exports callable functions for each builtin operation. These operators can simplify some common uses of lambdas, and should be used wherever possible.

```Python
import operator
operator.add(1, 2)  # => 3
operator.mul(3, 10)  # => 30
operator.pow(2, 3)  # => 8
operator.itemgetter(1)([1, 2, 3]) # => 2
```

Take a moment to skim over the [official documentation for the `operator` module](https://docs.python.org/3.4/library/operator.html).

Use `reduce` in conjunction with a function from the `operator` module to compute factorials in one line of Python:

```Python
from functools import reduce

def fact(n):
    # Your implementation here: Use reduce, an operator, and only one line! 
```

#### Custom comparison for `sort`, `max`, and `min`

Python defaults to ordering sequences by a default ordering. For instances, strings sort alphabetically, and tuples sort lexicographically. Sometimes, however, we need to sort based on a custom key value. In Python, we can supply an optional `key` argument to `sorted(seq)`, `max(seq)`, `min(seq)`, and `seq.sort()` which determines the values used for primarily ordering elements in a sequence.

For example:

```Python
words = ['pear', 'cabbage', 'apple', 'bananas']
min(words)  # => 'apple'
words.sort(key=lambda s: s[-1])  # Alternatively, key=operator.itemgetter(-1)
words  # => ['cabbage', 'apple', 'pear', 'bananas'] ... Why 'cabbage' > 'apple'?
max(words, key=len)  # 'cabbage' ... Why not 'bananas'?
min(words, key=lambda s: s[1::2])  # What will this value be?
```

Write a function to return the five words with the highest alphanumeric score of uppercase letters:

```Python
def alpha_score(upper_letters):
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')
alpha('hEllO')  # => 20 = 5 ('E') + 15 ('O')

def five_best(words):
    pass  # Your implementation here

```Python
You may want to use `filter` too.

## Purely Functional Programming

As a purely academic exercise, let's investigate how we would use Python in a purely functional programming paradigm. Ultimately, we will try to remove statements and replace them with expressions.

### Replacing Control Flow
The first thing that needs to go are control flow statements - `if/elif/else`. Luckily, Python, like many other languages, short circuits boolean expressions. This means that we can rewrite

```Python
if <cond1>:   func1()
elif <cond2>: func2()
else:         func3()
```

as the equivalent expression

```Python
(<cond1> and func1()) or (<cond2> and func2()) or (func3())
```

Rewrite the following code block without using `if/elif/else`:

```Python
if s == 0:  s += 1
else:       s -= 1
```

### Replacing Returns

However, we would still need return values to do anything useful. Since lambdas implicitly return their expression, we will use lambdas to eliminate return statements. We can bind these temporary conditional conjunctive normal form expressions to a lambda function.

```Python
echo = lambda arg: arg  # In practice, you should never bind lambdas to local names
cond_fn = lambda x: (x==1 and echo("one")) \
                 or (x==2 and echo("two")) \
                 or (echo("other"))
```

### Replacing Loops

Getting rid of loops is easy! We can use `map` over a sequence, instead of looping over the sequence. For example:

```Python
for e in lst:
    func(e)
```

becomes

```Python
map(func, lst)
```

### Replacing Action Sequence
Most programs take the form a sequence of steps, written out line by line. By using an apply function and map, we can replicate a sequence of function calls.

```Python
apply = lambda f: f()

# Suppose f1, f2, f3 are actions
map(apply, [f1, f2, f3])
```

Our main function can be a single call to such a map expression.

#### Note
In fact, Python has an `eval` and `exec` function builtin. Don't use them! They are dangerous.

### Closing
Python supports functional programming paradigms, but as you can see, in some cases FP introduces unnecessary complexity.

If you really enjoyed this section, read [Part 1](http://www.ibm.com/developerworks/linux/library/l-prog/index.html), [Part 2](http://www.ibm.com/developerworks/linux/library/l-prog2/index.html), and [Part 3](http://www.ibm.com/developerworks/linux/library/l-prog3/index.html) of IBM's articles on FP in Python.

## Iterators

Recall from class than an iterator is an object that represents a stream of data returned one value at a time.

### Iterator Consumption
Suppose the following two lines of code have been run:

```Python
it = iter(range(100))
67 in it  # => True
```

What is the output of each of the following lines of code?

```Python
next(it)  # => ??
37 in it  # => ??
next(it)  # => ??
```

With a partner, discuss why we see these results.

### Module: `itertools`

Python ships with a spectacular module for manipulating iterators called `itertools`. Take a moment to read through the [documentation page for itertools](https://docs.python.org/3.4/library/itertools.html).

Predict the output of the following pieces of code:

```Python
import itertools
import operator

for el in itertools.permutations('XKCD', 2):
    print(el, end=', ')

for el in itertools.cycle('LO'):
    print(el, end='')  # Don't run this one. Why not?

itertools.starmap(operator.mul, itertools.zip_longest([3,5,7],[2,3], fillvalue=1))
```

## Generator Expressions

Recall that generator expressions are a way to lazily compute values on the fly, without buffering the entire contents of the list in place.

For each of the following scenarios, discuss whether it would be more appropriate to use a generator expression or a list comprehension:

1. Searching for a given entity in the entries of a 1TB database.
2. Storing journey-to-destination flight information in order to calculate cheap airfare.
3. Finding the first palindromic Fibonacci number greater than 1,000,000.
4. Generate all multi-word anagrams of user-supplied 1000-character-or-more strings (very expensive to do).
5. Generate a list of names of Stanford students whose SUNet ID numbers are less than 5000000.
6. Return a list of all startups within 50 miles of Stanford.

## Generators

Write a infinite generator that successively yields the triangle numbers `0, 1, 3, 6, 10, ...`

```Python
def generate_triangles():
    pass  # Your implementation here
```

## Functions in Data Structures

In class, we quickly showed a highly unusual way to generate primes. Take some time to read through it again, and talk with a partner about how and why this successfully generates prime numbers.

```Python
def primes_under(n):
    tests = []
    for i in range(2, n):
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
            yield i
```

## Nested Functions and Closures

In class, we saw that functions can be defined within the scope of another function (recall from Week 3 that functions introduce new scopes via a new local symbol table). An inner function is only in scope inside of the outer function, so this type of function definition is usually only used when the inner function is being returned to the outside world.

```Python
def outer():
    def inner(a):
        return a
    return inner

f = outer()
f  # => <function inner at 0x1004340c8>
f(10)  # => 10

f2 = outer()
f2  # => <function inner at 0x1004341b8> ... Different from above!
f2(11)  # => 11
f(12)  # => 12
```

### Closure
As we saw above, the definition of the inner function occurs during the execution of the outer function. This implies that a nested function has access to the environment in which it was defined. Therefore, it is possible to return an inner function that remembers the state of the outer function, even after the outer function has completed execution. This model is referred to as a closure.

```Python
def make_adder(n):
    def add_n(m):  # Captures the outer variable in a closure
        return m + n
    return add_n

add1 = make_adder(1)
print(add1)  # <function make_adder.<locals>.add_n at 0x103edf8c8>
add1(4)  # => 4
add1(5)  # => 6
add2 = make_adder(2)
print(add2)  # <function make_adder.<locals>.add_n at 0x103ecbf28> (different from above!)
add2(4)  # => 6
add2(5)  # => 7
```

The information in a closure is available in the function's `__closure__` attribute. For example:

```Python
closure = add1.__closure__
cell0 = closure[0]
cell0.cell_contents  # => 1 (this is the n = 1 passed into make_adder)
``` 

As another example, consider the function:

```Python
def foo(a, b, c=-1, *d, e=-2, f=-3, **g):
    def wraps():
        print(a, c, e, g)        
``` 

The `print` call induces a closure of `wraps` over `a`, `c`, `e`, `g` from the enclosing scope of `foo`. Or, you can imagine that wraps "knows" that it will need `a`, `c`, `e`, and `g` from the enclosing scope, so at the time `wraps` is defined, Python takes a "screenshot" of these variables from the enclosing scope and stores references to the underlying objects in the `__closure__` attribute of the `wraps` function.

```Python
w = foo(1, 2, 3, 4, 5, e=6, f=7, y=2, z=3)
list(map(lambda cell: cell.cell_contents, w.__closure__))
# = > [1, 3, 6, {'y': 2, 'z': 3}]
```

## Building Decorators

Recall that a decorator is a special type of function that accepts a function as an argument and (usually) returns a modified version of that function. In class, we saw the `debug` decorator - review the slides if you still feel uncomfortable with the idea of a decorator.

Furthermore, recall that the `@decorator` syntax is syntactic sugar.

```Python
@decorator
def fn():
    pass
```

is equivalent to

```Python
def fn():
    pass
fn = decorator(fn)
```

### `print_args`
The `debug` decorator we wrote in class isn't very good. It doesn't tell us which function is being called, and it just gives us a tuple of positional arguments and a dictionary of keywords arguments - it doesn't even know what the names of the positional arguments are! If the default arguments aren't overridden, it won't show us their value either.

Use function attributes to improve our `debug` decorator into a `print_args` decorator that is as good as you can make it.

```Python
def print_args(function):
    def wrapper(*args, **kwargs):
        # (1) You could do something here
		retval = function(*args, **kwargs)
		# (2) You could also do something here
		return retval
    return wrapper
```

Hint: Consider using the attributes `fn.__name__`, `fn.__defaults__`, and `foo.__code__`. You'll have to investigate all of these attributes, but I will say that the last one is a code object which contains a number of useful attributes - for instance, `fn.__code__.co_varnames`. Check it out!

#### Note
There are a lot of subtleties to this function, since functions can be called in a number of different ways. If you're interested in other ways to customize this function, look at `fn.__kwdefaults__` (for keyword-only default arguments) and other attributes of `fn.__code__`.

### Automatic Caching
Write a decorator `cache` that will automatically cache any calls to the decorated function. You can assume that all arguments passed are hashable types.

```Python
def cache(function):
    pass  # Your implementation here
```

For example:

```Python
@cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1

fib(10)  # 55 (takes a moment to execute)
fib(10)  # 55 (returns immediately)
fib(100) # doesn't take forever
fib(500) # doesn't raise RecursionError
```

Hint: You can set arbitrary attributes on a function (e.g. `fn._cache`). When you do so, the attribute-value pair also gets inserted into `fn.__dict__`. Take a look for yourself. Are the extra attributes and `.__dict__` always in sync?

#### Note
This is actually implemented as part of the language in `functools.lru_cache`

### Static Type Checker

Recall that functions in Python can be optionally annotated by semantically-useless but structurally-valuable type annotations. For example:

```Python
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'

foo.__annotations__  # => {'a': int, 'b': str, 'return': bool}
```

Write a static type checker, implemented as a decorator, that enforces the parameter types and return type of Python objects.

```Python
def enforce_types(function):
    pass  # Your implementation here
```

For example:

```Python
@enforce_types
def foo(a: int, b: str) -> bool:
    if a == -1:
        return 'Gotcha!'
    return b[a] == 'X'

foo(3, 'abcXde')  # => True
foo(2, 'python')  # => False
foo(1, 4)  # prints "Invalid argument type for b: expected str, received int
foo(-1, '')  # prints "Invalid return type: expected bool, received str
```

There are lots of nuances to this function. When you think you're done, check with us.

#### Bonus: Optional Debug Argument
*Warning! This extension is very hard*

Extend the `enforce_types` decorator to accept a keyword argument `severity` which modifies the extent of the enforcement. If `severity == 0`, disable type checking. If `severity == 1` (which is the default), just print a message if there are any type violations. If `severity == 2`, raise an Exception if there are any type violations.

For example:

```Python
@enforce_types(severity=2)
def bar(a: list, b: str) -> int:
    return 0

@enforce_types  # Note that there are no parentheses
def baz(a: bool, b: str) -> str:
    return ''
```

## Credit
Credit goes to a lot of websites, whose names I've unfortunately forgotten along the way. Credit to everyone!