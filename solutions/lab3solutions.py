#!/usr/bin/env python3 -tt
"""
File: lab3solutions.py
----------------------
Reference solutions to Lab 3 for CS41: Hap.py Code.

This lab incorporated a lot of exploration, so there's less
"code" per se.

Revision history:
@sredmond 04-20-2017 Incorporates Christina's solutions
@sredmond 05-18-2016 Incorporates Conner's solutions
@sredmond 04-16-2016 Adds comments
@sredmond 04-12-2016 Created
"""


######################################
# EXPLORING ARGUMENTS AND PARAMETERS #
######################################


def print_two(a, b):
    """Explore the mechanics of calling a Python function with two positional parameters.

    print_two()             # Invalid: TypeError for omitting both required positional args
    print_two(4, 1)         # Valid
    print_two(41)           # Invalid: TypeError for omitting 1 required positional arg
    print_two(a=4, 1)       # Invalid: SyntaxError for having non-keyword arg after keyword arg
    print_two(4, a=1)       # Invalid: TypeError for passing multiple values for 'a'
    print_two(4, 1, 1)      # Invalid: TypeError for passing 3 positional args instead of 2
    print_two(b=4, 1)       # Invalid: SyntaxError for having non-keyword arg after keyword arg
    print_two(a=4, b=1)     # Valid
    print_two(b=1, a=4)     # Valid
    print_two(1, a=1)       # Invalid: TypeError for passing multiple values for 'a'
    print_two(4, 1, b=1)    # Invalid: TypeError for passing multiple values for 'b'
    """
    print("Arguments: {0} and {1}".format(a, b))


def keyword_args(a, b=1, c='X', d=None):
    """Explore the mechanics of calling a function with one positional parameters
    and three keyword parameters.

    keyword_args(5)                 # Valid ==> a:  5 , b:  1 , c:  X , d:  None
    keyword_args(a=5)               # Valid ==> a:  5 , b:  1 , c:  X , d:  None
    keyword_args(5, 8)              # Valid ==> a:  5 , b:  8 , c:  X , d:  None
    keyword_args(5, 2, c=4)         # Valid ==> a:  5 , b:  2 , c:  4 , d:  None
    keyword_args(5, 0, 1)           # Valid ==> a:  5 , b:  0 , c:  1 , d:  None
    keyword_args(5, 2, d=8, c=4)    # Valid ==> a:  5 , b:  2 , c:  4 , d:  8
    keyword_args(5, 2, 0, 1, "")    # Invalid: TypeError for passing 5 args
    keyword_args(c=7, 1)            # Invalid: SyntaxError for passing non-keyword arg after keyword arg
    keyword_args(c=7, a=1)          # Valid ==> a:  1 , b:  1 , c:  7 , d:  None
    keyword_args(5, 2, [], 5)       # Valid ==> a:  5 , b:  2 , c:  [] , d:  5
    keyword_args(1, 7, e=6)         # Invalid: TypeError for passing unexpected keyword arg 'e'
    keyword_args(1, c=7)            # Valid ==> a:  1 , b:  1 , c:  7 , d:  None
    keyword_args(5, 2, b=4)         # Invalid: TypeError for passing multiple values for 'b'
    """
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


def variadic(*args, **kwargs):
    """Explore the mechanics of calling a function with variadic positional parameters
    and variadic keyword parameters.

    # Valid
    variadic(2, 3, 5, 7)
      Positional: (2, 3, 5, 7)
      Keyword: {}

    # Valid
    variadic(1, 1, n=1)
      Positional: (1, 1)
      Keyword: {'n': 1}

    # Invalid: SyntaxError for passing non-keyword arg after keyword arg
    variadic(n=1, 2, 3)

    # Valid
    variadic()
      Positional:  ()
      Keyword:  {}

    # Valid
    variadic(cs="Computer Science", pd="Product Design")
      Positional:  ()
      Keyword:  {'pd': 'Product Design', 'cs': 'Computer Science'}

    # Invalid: SyntaxError for repeating keyword arg
    variadic(cs="Computer Science", cs="CompSci", cs="CS")

    # Valid
    variadic(5,8,k=1,swap=2)
      Positional:  (5, 8)
      Keyword:  {'k': 1, 'swap': 2}

    # Valid
    variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
      Positional:  (8, 3, 4, 5)
      Keyword:  {'b': 'x', 'k': 1, 'a': 5}

    # Invalid: SyntaxError for multiple single-splats *
    variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})

    # Invalid: SyntaxError for multiple single-splats *
    variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})

    # Valid
    variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})
      Positional:  ({'b': 'x', 'a': 5}, 'b', 'a')
      Keyword:  {'b': 'x', 'a': 5}
    """
    print("Positional:", args)
    print("Keyword:", kwargs)


def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """Explore the mechanics of calling a function with a combination of all
    the parameter types we've talked about.

    # Invalid - TypeError: all_together() missing 1 required positional argument: 'y'
    all_together(2)

    # Valid
    all_together(2, 5, 7, 8, indent=False)
      ==> x:  2 , y:  5 , z:  7
      ==> nums:  (8,) , indent:  False , spaces:  4 , options:  {}

    # Valid
    all_together(2, 5, 7, 6, indent=None)
     ==> x:  2 , y:  5 , z:  7
     ==> nums:  (6,) , indent:  None , spaces:  4 , options:  {}

    # Invalid - TypeError: all_together() missing 2 required positional arguments: 'x' and 'y'
    all_together()

    # Invalid - SyntaxError: non-keyword arg after keyword arg
    all_together(indent=True, 3, 4, 5)

    # Invalid - SyntaxError: double splay before keyword argument
    all_together(**{'indent': False}, scope='maximum')

    # Valid
    all_together(dict(x=0, y=1), *range(10))
      ==> x:  {'x': 0, 'y': 1} , y:  0 , z:  1
      ==> nums:  (2, 3, 4, 5, 6, 7, 8, 9) , indent:  True , spaces:  4 , options:  {}

    # Invalid - SyntaxError for splat after double splat
    all_together(**dict(x=0, y=1), *range(10))

    # Invalid - TypeError: got multiple values for 'x'
    all_together(*range(10), **dict(x=0, y=1))

    # Valid
    all_together([1, 2], {3:4})
      ==> x:  [1, 2] , y:  {3: 4} , z:  1
      ==> nums:  () , indent:  True , spaces:  4 , options:  {}

    # Invalid - TypeError: got multiple values for 'x'
    all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})

    # Valid
    all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
      ==> x:  8 , y:  9 , z:  10
      ==> nums:  (2, 4, 6) , indent:  True , spaces:  0 , options:  {'b': 'x', 'a': [4, 5]}

    # Invalid - SyntaxError: multiple single-splats *
    # all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})
    """
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)


#####################
# WRITING FUNCTIONS #
#####################


def speak_excitedly(message, num_exclamations=1, enthusiasm=False):
    """Return a message followed by some exclamations points, possibly capitalized."""
    message += '!' * num_exclamations
    if not enthusiasm:
        return message
    return message.upper()


def test_speak_excitedly():
    """Sample function calls illustrating the `speak_excitedly` function."""
    # "I love Python!"
    print(speak_excitedly("I love Python"))

    # "Keyword arguments are great!!!!"
    print(speak_excitedly("Keyword arguments are great", num_exclamations=4))

    # "I guess Java is okay..."
    print(speak_excitedly("I guess Java is okay...", num_exclamations=0))

    # "LET'S GO STANFORD!!"
    print(speak_excitedly("Let's go Stanford", num_exclamations=2, enthusiasm=True))


def average(*nums):
    """Return the average of numeric arguments or None if no arguments are supplied."""
    if not nums:  # Avoid ZeroDivisionError from an empty collection
        return None
    return sum(nums) / len(nums)


def test_average():
    """Sample function calls illustrating the `average` function."""
    avg_cheer = average(2, 4, 6, 8)
    print("Average of 2, 4, 6, 8 is {}".format(avg_cheer))

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    avg_primes = average(*primes)
    print("Average of first 10 primes is {}".format(avg_primes))


def make_table(key_justify='left', value_justify='right', **table_elems):
    """Construct a human-readable table of key-value pairs specified as keyword arguments.

    The keyword argument key_justify (default 'left') specifies alignment for the keys in
    the table, and value_justify (default 'right') specifies alignment for values in the table.
    Valid values are ['left', 'right', 'center'].

    For example,

        make_table(
            first_name="Sam",
            last_name="Redmond",
            shirt_color="pink"
        )

    should produce the table

        =========================
        | first_name  |     Sam |
        | last_name   | Redmond |
        | shirt_color |    pink |
        =========================

    """
    # Map from human-readable justifications to .format alignment specifiers
    justification = {
        'left': '<',
        'right': '>',
        'center': '^'
    }
    if key_justify not in justification or value_justify not in justification:
        raise ValueError("Invalid justification specifier. Choose from {}".format(list(justification.keys())))

    key_alignment_specifier = justification[key_justify]
    value_alignment_specifier = justification[value_justify]

    max_key_length = max(len(key) for key in table_elems.keys())
    max_value_length = max(len(value) for value in table_elems.values())

    # '| ' + padded_key + ' | ' + padded_value + ' |'
    total_length = 2 + max_key_length + 3 + max_value_length + 2

    print('=' * total_length)
    for key, value in table_elems.items():
        # Cool! We're formatting the format specifiers into the format string.
        print('| {:{key_align}{key_pad}} | {:{value_align}{value_pad}} |'.format(key, value,
            key_align=key_alignment_specifier, key_pad=max_key_length,
            value_align=value_alignment_specifier, value_pad=max_value_length
        ))
    print('=' * total_length)


def test_make_table():
    """Sample function calls illustrating the `make_table` function."""

    # =========================
    # | first_name  |     Sam |
    # | last_name   | Redmond |
    # | shirt_color |    pink |
    # =========================
    make_table(
        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink"
    )

    # ==================================
    # |            song |     Style    |
    # | artist_fullname | Taylor $wift |
    # |           album |     1989     |
    # ==================================
    make_table(
        key_justify="right",
        value_justify="center",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
    )


####################
# FUNCTION NUANCES #
####################


def nuance_return():
    """Explore the nuances of function return values."""
    def say_hello():
        """Says hello. :)"""
        print("Hello!")

    print(say_hello())   # None

    def echo(arg=None):
        """Prints an argument (default None) and returns it."""
        print("arg:", arg)
        return arg

    print(echo())         # None
    print(echo(5))        # 5
    print(echo("Hello"))  # Hello

    def drive(has_car):
        """Vroom vroom"""
        if not has_car:
            # Please never actually signal an error like this
            return "Oh no!"
        return 100  # miles

    print(drive(False))   # "Oh no!"
    print(drive(True))    # 100


def parameters_and_object_reference():
    """Explore parameters and object references.

    Why does calling `reassign(l)` not seem to change the value of `l` in the outer scope
    but calling `append_one(l)` does seem to change it? Remember, functions introduce scopes,
    and in particular at function invocation time, both `reassign` and `append_one` have local
    named (titled `arr`) which resolve to the externally-visible array also named by `l`.
    However, in `reassign`, this local name is changed (reassigned) to point to some new element,
    and the original array object named by `l` is unchanged. In contrast, in `append_one`, the
    name `arr` resolves to that single array object which is updated in place. After we append,
    both `arr` and `l` are names which resolve to the same updated array.
    """
    def reassign(arr):
        """Assign arr to [4, 1] and print it."""
        arr = [4, 1]
        print("Inside reassign: arr={}".format(arr))

    def append_one(arr):
        """Append the value 1 to arr and print it."""
        arr.append(1)
        print("Inside append_one: arr={}".format(arr))

    l = [4]
    print("Before reassign: arr={}".format(l))  # => Before reassign: arr=[4]
    reassign(l)                                 # => Inside reassign: arr=[4, 1]
    print("After reassign: arr={}".format(l))  # =>  After reassign: arr=[4]

    l = [4]
    print("Before append_one: arr={}".format(l))  # => Before append_one: arr=[4]
    append_one(l)                                 # => Inside append_one: arr=[4, 1]
    print("After append_one: arr={}".format(l))  # =>  After append_one: arr=[4, 1]


def scope(case=1):
    """Explore function scope and name resolution, by case (default 1)

    In case 1, we only declare an x in the outer scope, so when `foo` tries to resolve
    `x` it encounters the `x` in an outer scope. In case 2, however, in resolving the
    name `x` in order to print `x` and `x * y`, `foo` at function-compile-time determines
    that there is an `x` in the local scope and uses the local scope in order to resolve `x`.

    In any other case, we raise an UnboundLocalError by referencing a name that `foo`
    knows is in the local scope (determined at function-compile-time) before it is attached
    to any value. UnboundLocalError is a subclass of NameError.

    Specifically, when you make an assignment to a variable in a scope, that variable becomes
    local to that scope and shadows any similarly named variable in the outer scope. Since the
    last statement in foo assigns a new value to x, the compiler recognizes it as a local variable.
    Consequently, the earlier print(x) attempts to print the uninitialized local variable and an
    error results.

    Read https://docs.python.org/3.4/reference/executionmodel.html#resolution-of-names for more information.
    """
    if case == 1:
        x = 10

        def foo():
            """Print some values."""
            print("(inside foo) x:", x)
            y = 5
            print('value:', x * y)

        print("(outside foo) x:", x)
        foo()
        print("(after foo) x:", x)

        # (outside foo) x: 10
        # (inside foo) x: 10
        # value: 50
        # (after foo) x: 10

    elif case == 2:  # Case 2
        x = 10

        def foo():
            """Print some values."""
            x = 8  # Only added this line - everything else is the same
            print("(inside foo) x:", x)
            y = 5
            print('value:', x * y)

        print("(outside foo) x:", x)
        foo()
        print("(after foo) x:", x)

        # (outside foo) x: 10
        # (inside foo) x: 8
        # value: 40
        # (after foo) x: 10

    else:  # UnboundLocalError
        x = 10

        def foo():
            """Print some values."""
            # Raises an UnboundLocalError
            print("(inside foo) x:", x)  # We swapped this line
            x = 8                        # with this one
            y = 5
            print('value:', x * y)

        print("(outside foo) x:", x)
        foo()
        print("(after foo) x:", x)


def default_mutable_arguments():
    """Explore default mutable arguments, which are a dangerous game in themselves.

    Why do mutable default arguments suffer from this apparent problem? A function's
    default values are evaluated at the point of function definition in the defining
    scope. In particular, we can examine these bindings by printing
    append_twice.__defaults__ after append_twice has been defined. For this function,
    we have

        print(append_twice.__defaults__)  # ([],)

    If a binding for `lst` is not supplied, then the `lst` name inside append_twice
    falls back to the array object that lives inside append_twice.__defaults__.

    In particular, if we update `lst` in place during one function call, we have changed
    the value of the default argument. That is,

        print(append_twice.__defaults__)  # ([], )
        append_twice(1)
        print(append_twice.__defaults__)  # ([1, 1], )
        append_twice(2)
        print(append_twice.__defaults__)  # ([1, 1, 2, 2], )

    In each case where a user-supplied binding for `lst is not given, we modify the
    single (mutable) default value, which leads to this crazy behavior.
    """
    def append_twice(a, lst=[]):
        """Append a value to a list twice."""
        lst.append(a)
        lst.append(a)
        return lst

    print(append_twice(1, lst=[4]))  # => [4, 1, 1]
    print(append_twice(11, lst=[2, 3, 5, 7]))  # => [2, 3, 5, 7, 11, 11]

    print(append_twice(1)) # => [1,1]
    print(append_twice(2)) # => [1,1,2,2]
    print(append_twice(3)) # => [1,1,2,2,3,3]


##################################
# INVESTIGATING FUNCTION OBJECTS #
##################################


# This portion of the lab was all informative - no coding necessary!


if __name__ == '__main__':
    # Runs some test cases only if invoked as a script.
    test_speak_excitedly()
    test_average()
    test_make_table()
    nuance_return()
    parameters_and_object_reference()
    scope(case=1)
    scope(case=2)
    default_mutable_arguments()
