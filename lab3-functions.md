# Lab 3: Functions

## Overview
Build familiarity with reading and writing Python functions with different types of formal parameters, explore some nuances of function execution semantics, and dive into the internals of functions.

*Disclaimer: we know that this lab is particularly focused on Python semantics, which may not seem exciting at first. However, mastering the mechanics of Python functions gives you access to a whole lot of powerful tools that either don't exist or are uncommon or hard-to-use in other languages! The skills you learn through this lab will allow you to write (and debug) powerful Pythonic code quickly and easily!*

**As with Lab 2, we don't expect you to finish all of the material here in one class period. If you do - great! But if not, you are encouraged to work through the extra material at your own pace - it explores interesting and intriguing aspects of Python functions.**

## Exploring Arguments and Parameters

With a partner, work through the following problems.

### Familiar Functions
Consider the following function definition:

```
def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))
```

For each of the following function calls, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?

*Note: make your predictions **before** running the code in the interactive interpreter. Then check yourself!*

```
# Valid or invalid?
print_two()
print_two(4, 1)
print_two(41)
print_two(a=4, 1)
print_two(4, a=1)
print_two(4, 1, 1)
print_two(b=4, 1)
print_two(a=4, b=1)
print_two(b=1, a=4)
print_two(1, a=1)
print_two(4, 1, b=1)
```

Write at least two more instances of function calls, not listed above, and predict their output. Are they valid or invalid? Check your hypothesis.

*These "write-some-more" problems are your chance to clarify your own understanding of function call semantics. You can skip them if you'd like, but using the interactive interpreter to test your own hypotheses is a crucial Python skill that lets you answer questions of the form "But what happens if I..."*

### Default Arguments

Consider the following function definition:

```
def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
```

For each of the following function calls, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?

```
keyword_args(5)
keyword_args(a=5)
keyword_args(5, 8)
keyword_args(5, 2, c=4)
keyword_args(5, 0, 1)
keyword_args(5, 2, d=8, c=4)
keyword_args(5, 2, 0, 1, "")
keyword_args(c=7, 1)
keyword_args(c=7, a=1)
keyword_args(5, 2, [], 5)
keyword_args(1, 7, e=6)
keyword_args(1, c=7)
keyword_args(5, 2, b=4)
```

Write at least two more instances of function calls, not listed above, and predict their output. Are they valid or invalid? Check your hypothesis.

### Exploring Variadic Argument lists
As before, consider the following function definition: 

```
def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
```

For each of the following function calls, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?

```
variadic(2, 3, 5, 7)
variadic(1, 1, n=1)
variadic(n=1, 2, 3)
variadic()
variadic(cs="Computer Science", pd="Product Design")
variadic(cs="Computer Science", cs="CompSci", cs="CS")
variadic(5, 8, k=1, swap=2)
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})
```

Write at least two more instances of function calls, not listed above, and predict their output. Are they valid or invalid? Check your hypothesis.

### *Optional: Putting it all together*
*If you feel confident that you understand how function calling works, you can skip this section. We suggest that you work through it anyway, but the final decision is up to you.*

Often, however, we don't just see keyword arguments of variadic parameter lists in isolated situations. The following function definition, which incorporates positional parameters, keyword parameters, variadic positional parameters, keyword-only default parameters and variadic keyword parameters, is valid Python. 

```
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)
```

For each of the following function calls, predict whether the call is valid or not. If it is valid, what will the output be? If it is invalid, what is the cause of the error?

```
all_together(2)
all_together(2, 5, 7, 8, indent=False)
all_together(2, 5, 7, 6, indent=None)
all_together()
all_together(indent=True, 3, 4, 5)
all_together(**{'indent': False}, scope='maximum')
all_together(dict(x=0, y=1), *range(10))
all_together(**dict(x=0, y=1), *range(10))
all_together(*range(10), **dict(x=0, y=1))
all_together([1, 2], {3:4})
all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})
all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})
```

Write at least two more instances of function calls, not listed above, and predict their output. Are they valid or invalid? Check your hypothesis.

## Writing Functions
### `speak_excitedly`
Write a function `speak_excitedly` that accepts one required positional argument (a message) and two optional keyword arguments, the first of which is a positive integer referring to the number of exclamation marks to put at the end of the message (defaults to 1), and the second of which is a boolean flag indicating whether or not to capitalize the message (defaults to False).

What would the function signature and implementation look like for this function?

```
def speak_excitedly(???):
    pass
```

How would you call this function to produce the following outputs?

```
"I love Python!"
"Keyword arguments are great!!!!"
"I guess Java is okay..."
"LET'S GO STANFORD!!"
```

### `average`
Write a function `average` that accepts a variable number of integer positional arguments and computes the average. If no arguments are supplied, the function should return `None`.

What would the function signature and implementation look like for this function?

```
def average(???):
    pass
```

It should be possible to call the function as follows:

```
average()  # => None
average(5) # => 5.0
average(6, 8, 9, 11)  # => 8.5
```

Suppose that we have a list `l = [???]` supplied by the user of unknown length. How can we use the `average` function we just wrote function to compute the average of this list? For this problem, do not use the builtin `sum` or `len` functions.

### Challenge: `make_table`

Write a function to make a table out of an arbitrary number of keyword arguments. There should be two parameters, `key_justify` and `value_justify`, whose default values are `'left'` and `'right'` respectively, and which control the justification for keys and values in the table. Valid options for these parameters are `['left', 'right', 'center']`. There should be an extra space of padding on either side of the keys and values.

What would the function signature and implementation look like for this function?

```
def make_table(???):
    pass
```

As an example:

```
make_table(
    first_name="Sam",
    last_name="Redmond",
    shirt_color="pink"
)
```

should produce

```
=========================
| first_name  |     Sam |
| last_name   | Redmond |
| shirt_color |    pink |
=========================
```

and

```
make_table(
    key_justify="right",
    value_justify="center",
    song="Style",
    artist_fullname="Taylor $wift",
    album="1989"
)
```

should produce

```
==================================
|            song |     Style    |
| artist_fullname | Taylor $wift |
|           album |     1989     |
==================================
```

Hint: you may find Python's string `.format()` [alignment specifiers](https://pyformat.info/#string_pad_align) useful.

## Function Nuances
### Return

Predict the output of the following code snippet. Then, run the code to check your hypothesis.

```
def say_hello():
    print("Hello!")

print(say_hello())  # => ?

def echo(arg=None):
    print("arg:", arg)
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

If you made any incorrect predictions, talk to a partner about why!

### Parameters and Object Reference

*Optional Reading: [Jeff Knupp's Blog](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/)*

Suppose we have the following two functions:

```
def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1) 
    print("Inside append_one: arr = {}".format(arr))
```

Predict what the following code snippet will output. What's the difference between the sections? What is the cause of this difference?

```
l = [4]
print("Before reassign: arr={}".format(l))  # => ?
reassign(l)
print("After reassign: arr={}".format(l))  # => ?

l = [4]
print("Before append_one: arr={}".format(l))  # => ?
append_one(l)
print("After append_one: arr={}".format(l))  # => ?
```

### Scope
*Optional Reading: [Python's Execution Model](https://docs.python.org/3.4/reference/executionmodel.html), especially Section 4.2.2.*

Predict the output of the next two Python programs, then run them to confirm or refute your hypothesis.

```
# Case 1
x = 10

def foo():
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
```

and

```
# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
```

Draw a picture of the variable bindings at each scope (global scope and `foo` function-level scope) in each case. 

#### UnboundLocalError

If we swap just two lines of code, something unusual happens. What is the error? Why might it be happening?

```
x = 10

def foo():
    print("(inside foo) x:", x)  # We swapped this line
    x = 8                        # with this one
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
```

In a similar vein, `foo` as defined in

```
lst = [1,2,3]
def foo():
    lst.append(4)
foo()
```

will compile (that is, the function object will be byte-compiled without problem), but

```
lst = [1,2,3]
def foo():
    lst = lst + [4]
foo()
```

will raise an UnboundLocalError. Why? It doesn't, surprisingly, have to do with the fact that `.append` is in place and `+` is not.

This is such a common problem that the Python FAQ has [a section](https://docs.python.org/3.4/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value) dedicated to this type of `UnboundLocalError`.

*Note, the `global` and `nonlocal` keywords can be used to assign to a variable outside of the currently active (innermost function) scope. If you're interested, you can read more about scoping rules in the optional reading, or in the [appropriate FAQ section](https://docs.python.org/3.4/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python).*

### Default Mutable Arguments - A Dangerous Game

A function's default values are evaluated at the point of function definition in the defining scope. For example

```
x = 5

def square(num=x):
    return num * num

x = 6
f()   # => 25, not 36
f(x)  # => 36
```

**Warning: A function's default values are evaluated *only once*, when the function definition is encountered. This is important when the default value is a mutable object such as a list or dictionary**

Predict what the following code will do, then run it to test your hypothesis:

```
def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst
   
# Works well when the keyword is provided
append_twice(1, lst=[4])  # => [4, 1, 1]
append_twice(11, lst=[2, 3, 5, 7])  # => [2, 3, 5, 7, 11, 11]

# But what happens here?
print(append_twice(1))
print(append_twice(2))
print(append_twice(3))
```

After you run the code, you should see the following printed to the screen:

```
[1, 1]
[1, 1, 2, 2]
[1, 1, 2, 2, 3, 3]
```
Discuss with a partner why this is happening.

If you don’t want the default value to be shared between subsequent calls, you can use a sentinel value as the default value (to signal that no keyword argument was explicitly provided by the caller). If so, your function may look something like:

```
def append_twice(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    lst.append(a)
    return lst
```

Sometimes, however, this odd keyword value initialization behavior can be desirable. For example, it can be used as a cache that is modifiable and accessible by all invocations of a function:

```
def fib(n, cache={0: 1, 1: 1}):
   if n in cache:  # Note: default value captures our base cases
       return cache[n]
   out = fib(n-1) + fib(n-2)
   cache[n] = out
   return out
```

Cool, right? The cache follows the function around, as an attribute on the function object, rather than being the responsibility of the caller! Even so, there are better, more Pythonic ways to capture this particular cache design pattern (see [functools.lru_cache](https://docs.python.org/3.4/library/functools.html#functools.lru_cache)). Nevertheless, it's a neat trick that might come in useful!


## Investigating Function Objects

At the end of Monday's class, we explored some of the attributes of function objects. We'll explore several of these attributes more in depth here.

Usually, this information isn't particularly useful for practitioners (you'll rarely want to hack around with the internals of functions), but even seeing that you *can* in Python is very cool.

#### Default Values (`__defaults__` and `__kwdefaults__`)

As stated earlier, any default values (either normal default arguments or the keyword-only default arguments that follow a variadic positional argument parameter) are bound to the function object at the time of function definition. Consider our `all_together` function from earlier:

```
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options): pass

all_together.__defaults__  # => (1, )
all_together.__kwdefaults__  # => {'indent':True, 'spaces':4}
```

Why might the `__defaults__` attribute be a tuple, but the `__kwdefaults__` attribute be a dictionary?

#### Documentation (`__doc__`)

The first string literal in any function, if it comes before any expression, is bound to the function's `__doc__` attribute. 

```
def my_function():
    """Summary line: do nothing, but document it.
        
    Description: No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
# Summary line: Do nothing, but document it.
#
#     Description: No, really, it doesn't do anything.
```

As stated in lecture, lots of tools use these documentation strings to great advantage. For example, the builtin `help` function displays information from docstrings, and many API-documentation-generation tools like [Sphynx](http://www.sphinx-doc.org/en/stable/) or [Epydoc](http://epydoc.sourceforge.net/) use information contained in the docstring to form smart references and hyperlinks on documentation websites.

Furthermore, the [doctest](https://docs.python.org/3.4/library/doctest.html) standard library module, in it's own words, "searches [the documentation string] for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown." Cool!

#### Code Object (`__code__`)

In CPython, the reference implementation of Python that many people (including us) use, functions are compiled into bytecode when defined. This code object is bound to the `__code__` attribute, and has a ton of interesting properties, best illustrated by example.

```
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """A useless comment"""
    print(x + y * z)
    print(sum(nums))
    for k, v in options.items():
        if indent:
            print("{}\t{}".format(k, v))
        else:
            print("{}{}{}".format(k, " " * spaces, v))
            
code = all_together.__code__
```

| Attribute  | Sample Value | Explanation |
| --- | --- | --- |
| `.co_argcount` | `3` | number of positional arguments (including arguments with default values) |
| `.co_cellvars` | `()` | tuple containing the names of local variables that are referenced by nested functions |
| `.co_code` | `b't\x00\x00...\x00\x00S'` | string representing the sequence of bytecode instructions |
| `.co_consts` | `('A useless comment', '{}\t{}', '{}{}{}', ' ', None)` | tuple containing the literals used by the bytecode - our `None` is from the implicit `return None` at the end |
| `.co_filename` | `<stdin>` | file in which the function was defined |
| `.co_firstlineno` | `1` | line of the file the first line of the function appears |
| `.co_flags` | `79` | AND of compiler-specific binary flags whose internal meaning is (largely) unspecified |
| `.co_freevars` | `()` | tuple containing the names of free variables |
| `.co_kwonlyargcount` | `2` | number of keyword-only arguments |
| `.co_lnotab` | `b'\x00\x02\x12\x01\x10\x01\x19\x01\x06\x01\x19\x02'` | string encoding the mapping from bytecode offsets to line numbers |
| `.co_name` | `"all_together"` | the function name  |
| `.co_names` | `('print', 'sum', 'items', 'format')` | tuple containing the names used by the bytecode |
| `co_nlocals` | `9` | number of local variables used by the function (including arguments) |
| `co_stacksize` | `6` | required stack size (including local variables) |
| `co_varnames` | `('x', 'y', 'z', 'indent', 'spaces', 'nums', 'options', 'k', 'v')` | tuple containing the names of the local variables (starting with the argument names) |

More info on this, and on all types in Python, can be found at the [data model reference](https://docs.python.org/3.4/reference/datamodel.html#the-standard-type-hierarchy). For code objects, you have to scroll down to "Internal Types."

##### Security

As we briefly mentioned in class, this can lead to a pretty glaring security vulnerability. Namely, the code object on a given function can be hot-swapped for the code object of another (perhaps malicious function) at runtime!

```
def nice(): print("You're awesome!")
def mean(): print("You're... not awesome. OOOOH")

# Overwrite the code object for nice
nice.__code__ = mean.__code__
nice()  # prints "You're... not awesome. OOOOH"
```
 
##### `dis` module

The `dis` module, for "disassemble," exports a `dis` function that allows us to disassemble Python byte code (at least, for Python distributions implemented in CPython for existing versions). The disassembled code isn't exactly normal assembly code, but rather is a specialized Python syntax

```
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
import dis
dis.dis(gcd)
"""
  2           0 SETUP_LOOP              27 (to 30)
        >>    3 LOAD_FAST                1 (b)
              6 POP_JUMP_IF_FALSE       29

  3           9 LOAD_FAST                1 (b)
             12 LOAD_FAST                0 (a)
             15 LOAD_FAST                1 (b)
             18 BINARY_MODULO
             19 ROT_TWO
             20 STORE_FAST               0 (a)
             23 STORE_FAST               1 (b)
             26 JUMP_ABSOLUTE            3
        >>   29 POP_BLOCK

  4     >>   30 LOAD_FAST                0 (a)
             33 RETURN_VALUE
"""
```

Details on the instructions themselves can be found [here](https://docs.python.org/3.4/library/dis.html#python-bytecode-instructions).
You can read more about the `dis` module [here](https://docs.python.org/3.4/library/dis.html).

#### Parameter Annotations (`__annotations__`)

As we saw in class, Python allows us to offer type annotations on functions

```
def annotated(a: int, b: str) -> list:
    return [a, b]

print(annotated.__annotations__)
# {'b': <class 'str'>, 'a': <class 'int'>, 'return': <class 'list'>}
```

This information can be used to build some really neat offline type-checkers for Python!

For more info, check out [PEP 3107](https://www.python.org/dev/peps/pep-3107/) on function annotations or [Pep 484](https://www.python.org/dev/peps/pep-0484/) on type hinting (which was introduced in Python 3.5)

#### Call (`__call__`)

All Python functions have a `__call__` attribute, which is the actual object called when you use parentheses to "call" a function. That is,

```
def greet(): print("Hello world!")

greet() # "Hello world!"
# is just syntactic sugar for
greet.__call__()  # "Hello world!"
```

This means that any object (including instances of custom classes) with a `__call__` method can use the parenthesized function call syntax! We'll see a lot more about using these so-called "magic methods" to exploit Python's apparent operators (like function calling, `+` (`__add__`) or `*` (`__mul__`), etc) in Week 5.

#### Name Information (`__module__`, `__name__`, and `__qualname__`)

Python functions also store some name information, generally for the purposes of friendly printing.

`__module__` refers to the module that was active at the time the function was defined. Any functions defined in the interactive interpreter will have `__module__ == '__main__'`, but, for example, `encrypt_caesar.__module__ == 'crypto'`.

`__name__` is the function's name. Nothing special here.

`__qualname__`, which stands for "qualified name," only differs from `__name__` when you're dealing with nested functions, which we'll talk about more Week 4.

#### Closure (`__closure__`)

If you're familiar with closures in other languages, Python closures work almost the exact same way. Closures really only arise when dealing with nested functions, so we'll see more Week 4. This bit of text is just to give you a teaser for what's coming soon - yes, Python has closures! 

#### `inspect` module

As a brief note, all of this mucking around with the internals of Python functions can't be good for our health. Luckily, there's a standard library module for this! The `inspect` module gives us a lot of nice tools for interacting not only with the internals of functions, but also the internals of a lot of other types as well. Check out [the documentation](https://docs.python.org/3.4/library/inspect.html) for some nice examples.

## Finished Early?
Scan through [PEP 257](https://www.python.org/dev/peps/pep-0257/), Python's suggestions for docstring conventions, as well as [PEP 8](https://www.python.org/dev/peps/pep-0008/), Python's style guide, if you didn't get a chance to read it last week.

## Submitting Labs

Woohoo! There's nothing to officially submit for this lab, but before you go, call over a TA to sign off on your work. After that, you're free to leave as soon as you would like! However, you're also welcome to stick around and work on Assignment 1. :)

**Major credit to PSF for incredibly clear/readable documentation making this all possible, as well as the linked resources.**

> With <3 by @sredmond
