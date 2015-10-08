# TODOs
Varargs, var kwargs (writing and calling), bonus?

# Lab 3.2: Functions

## Overview
Build familiarity with writing and calling Python functions with different types of formal parameter types and explore nuances of function execution semantics.

### Time
As with Lab 2.2, there is more material here than anyone could feasibly cover in eighty minutes.

Expect to spend the first hour working on the lab, and the last twenty minutes of class working on Assignment 1.

## Function Definitions and Function Execution
### Basic Function
Consider the following function definition:
```
def foo(a, b):
    print("a:", a)
    print("b:", b)
```

For each of the following function calls, determine whether the call is valid or not. If it is valid, what will the output be?

```
foo()
foo(0)
foo(0, 1)
foo(a=0, 1)
foo(b=0, 1)
foo(a=0, b=1)
foo(b=1, a=0)
foo(0, a=0)
foo(0, a=1)
foo(0, 1, 1)
foo(0, 1, b=1)
```

Write at least two more function calls, not listed above, predict their output, and then check your guess. This is your chance to clarify your own understanding of function call semantics. Remember, the interactive interpreter is your friend! It is a wonderful tool for answering questions of the form "But what happens if I..."

### Keyword Arguments
Consider the following function definition:
```
def bar(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
```

For each of the following function calls, determine whether the call is valid or not. If it is valid, what will the output be?

```
bar(5)
bar(a=5)
bar(5, 8)
bar(5, 2, c=4)
bar(5, 0, 1)
bar(5, 2, d=8, c=4)
bar(5, 2, 0, 1, "")
bar(c=7, 1)
bar(c=7, a=1)
bar(5, 2, [], 5)
bar(1, 7, e=6)
bar(1, c=7)
bar(5, 2, b=4)
```

Write at least two more function calls, not listed above, predict their output, and then check your guess.

### Exploring Variadic Argument lists
```
def baz(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
```
For each of the following function calls, determine whether the call is valid or not. If it is valid, what will the output be?
```
baz(2, 3, 5, 7)
baz(1, 1, n=1)
baz(n=1, 2, 3)
baz()
baz(cs="Computer Science", pd="Product Design")
baz(5, 8, k=1, swap=2)
```

Write at least two more function calls, not listed above, predict their output, and then check your guess.

### *Optional:* Putting it all together
*If you feel confident that you understand how function calling works, you can skip this section. We suggest that you work through it anyway, but the final decision is up to you.*

Often, however, we don't just see keyword arguments of variadic parameter lists in isolated situations.
```
def all_together(x, y, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)
```
For each of the following function calls, determine whether the call is valid or not. If it is valid, what will the output be?


## Writing Functions
### `speak_excitedly`
Write a function `speak_excitedly` that accepts one required positional argument (a message) and two optional keyword arguments, the first of which is a positive integer referring to the number of exclamation marks to put at the end of the message (defaults to 1), and the second of which is a boolean flag indicating whether or not to capitalize the message (defaults to False).

How would you call this function to produce the following outputs?
```
"I love Python!"
"Keyword arguments are great!!!!"
"I guess Java is okay..."
"LET'S GO STANFORD!!"
```

### `average`
Write a function `average` that accepts a variable number of integer positional arguments and computes the average. If no arguments are supplied, the function should return 0. It should be possible to call the function as follows:
```
average()  # => 0
average(5) # => 5
average(6,8,9,11)  # => 8.5
```

Suppose that we have a list `l = [0, 3, 4, 8]`. How can we use our `average` function to compute the average of this list? For this problem, do not use the builtin `sum` or `len` functions.

### `make_table`

## Nuances
### Return
Predict the output of the following code snippet. Then, run the code to check your hypothesis.
```
def say_hello():
    print("Hello!")

print(say_hello())  # => ?

def echo(arg=None):
    print(arg)
    return arg

print(echo())  # => ?
print(echo(5)) # => ?
print(echo("Hello")) # => ?

def drive(has_car):
    if not has_car:
        return
    return 100  # miles

drive(False)  # => ?
drive(True)   # => ?
```

### Pass by Value? Pass by Reference? Neither!
Read [Jeff Knupp's awesome post](https://www.jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/) about Python's pass-by-object-reference semantics. (Note! This post is technical, but you should spend time reading and understanding the material. If you understand Python's name binding, everything else will make sense.),

Alternatively, for a more visual, less comprehensive overview of Python's parameter passing semantics, read:
[Rob Heaton's narrative](http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/), [Understanding Python Variables](http://foobarnbaz.com/2012/07/08/understanding-python-variables/) up through the header 'A bit about Python's memory management'

If you're still confused, read through [this lovely StackOverflow explanation](http://stackoverflow.com/a/986145)

```
def rename(arr):
    arr = arr + [0]

def appendZeroTo(arr):
    arr.append(0)

l = [0]
print(l)  # => ?
rename(l)
print(l)  # => ?

l = [0]
print(l)  # => ?
appendZeroTo(l)
print(l)  # => ?
```

### Scope
*Optional Reading: [Python's Name Resolution Semantics](https://docs.python.org/3.4/reference/executionmodel.html#resolution-of-names)*

Contrast the following two Python programs
```
x = 10

def foo():
    y = 5
    print(x * y, end=' ')

print(x)
foo()  # => 50 10
```
and
```
x = 10

def foo():
    x = 8
    y = 5
    print(x * y, end=' ')

print(x)

foo()  # => 40 10
```

Additionally, the `global` and `nonlocal` can be used to assign to a variable outside of the currently active (innermost function) scope. If you're interested, you can read more about scoping rules in the optional reading.

### Default Mutable Arguments

A function's default values are evaluated at the point of function definition in the defining scope, so that

```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```
will print 5.

Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or any instance of most classes.

Predict what the following code will do, then run it to test your hypothesis:
```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

After you run the code, you should see the following printed to the screen:
```
[1]
[1, 2]
[1, 2, 3]
```
Discuss with a partner why this is happening.

If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

## Bonus: Investigating Function Objects
### Function Attributes


**Credit, as always, to PSF and the linked online resources.**
