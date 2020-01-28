#!/usr/bin/env python3
"""
File: lab-4.py
--------------

Reference solutions for CS41 Lab 4.

As in lecture slides, a data source surrounded by angle brackets such as:
    <1, 2, 3>
is our notation for an iterable over those elements.

Many thanks to Sam Redmond (@sredmond) for writing some of these solutions.

Revision History:
    @psarin 1-27-2020   Created file
"""

##############
##############
##  PART 1  ##
##############
##############


########################################
#  EXPLORING ARGUMENTS AND PARAMETERS  #
########################################
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
    # Valid
    variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
      Positional: (8, 3, 4, 5)
      Keyword: {'k': 1, 'a': 5, 'b': 'x'}
    # Valid
    variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
      Positional: (3, 4, 5, 8, 4, 1)
      Keyword: {'k': 1, 'a': 5, 'b': 'x'}
    # Valid
    variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})
      Positional:  ({'b': 'x', 'a': 5}, 'b', 'a')
      Keyword:  {'b': 'x', 'a': 5}
    """
    print("Positional:", args)
    print("Keyword:", kwargs)


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


def make_table(key_justify='left', value_justify='right', **table_elems):
    """
    Construct a human-readable table of key-value pairs specified as keyword 
    arguments. The keyword argument key_justify (default 'left') specifies 
    alignment for the keys in the table, and value_justify (default 'right') 
    specifies alignment for values in the table.
    
    Valid values are ['left', 'right', 'center'].
    
    For example,
        make_table(
            first_name="Parth",
            last_name="Sarin",
            fav_animal="Unicorn"
        )
    should produce the table
        ========================
        | first_name |   Parth |
        | last_name  |   Sarin |
        | fav_animal | Unicorn |
        ========================
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

    # ========================
    # | first_name |   Parth |
    # | last_name  |   Sarin |
    # | fav_animal | Unicorn |
    # ========================
    make_table(
        first_name='Parth',
        last_name='Sarin',
        fav_animal='Unicorn'
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


############################
#  FUNCTIONAL PROGRAMMING  #
############################
def comprehension_read():
    """Practice reading comprehensions and explore oddities with function calls
    Each list comprehension is replicated below with an explanation:
    [x for x in [1, 2, 3, 4]]
    # => [1, 2, 3, 4]
        Constructs a list containing exactly the elements in [1, 2, 3, 4].
        Not a very interesting list comprehension at all, since the `x for x`
        means that no transformation will happen over the range.
    [n - 2 for n in range(10)]
    # => [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        Subtracts 2 from each of the elements in range(10). For example, the
        first element of range(10) is n = 0, so the first element of our generated
        list is n - 2 = -2. The pattern then continues for the rest of the elements.
    [k % 10 for k in range(41) if k % 3 == 0]
    # => [0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9]
        Gets the last digit of any number under 41 that is a multiple of 3.
        Note that the `if k % 3 == 0` is a filtering condition! We'll see more
        about filtering Week 4.
    [s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]]
    # => ['python']
        Builds the lowercased words if the first character is smaller than
        the last character.
        For example, when s = 'Python', we have s[0] = 'P' and s[-1] = 'n',
        and since 'P' < 'n' (compared by ASCII values), we pass our filter
        condition, and so contribute 'python' to the final list.
        On the other hand, both 'iS' and 'cOoL' do not satisfy s[0] < s[-1],
        so they are not passed to s.lower() for inclusion in the final list.
    arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    print([el.append(el[0] * 4) for el in arr])
    # => [None, None, None]
    print(arr)
    # => [
      [3, 2, 1, 12],
      ['a', 'b', 'c', 'aaaa'],
      [('do',), ['re'], 'mi', ('do', 'do', 'do', 'do')]
    ]
        What's going on here? .append() is a function that returns None,
        so the list comprehension returns a list of three Nones, but the
        effect of the append still takes place - that is, the array elements
        themselves are still updated. Since 3 is an integer, 3 * 4 = 12 is
        appended to the end of the first list. Since 'a' is a string,
        'a' * 4 = 'aaaa' is appended to the end of the second list. Since
        ('do',) is a tuple, ('do',) * 4 = ('do', 'do', 'do', 'do') is appended
        to the end of the third list. Note that this is an example of duck-typing
        in action!
    [letter for letter in "pYthON" if letter.isupper()]
    # => ['Y', 'O', 'N']
        Simple enough. Keeps only the upper case letters in "pYthON", which are
        'Y', 'O', and 'N'. Interesting, the result is a list of characters, not
        a string, as you might guess. This is because the list comprehension
        traverses the string "pYthON" as a sequence of 1-character strings.
    {len(w) for w in ["its", "the", "remix", "to", "ignition"]}
    # => {2, 3, 5, 8}
        Our first set comprehension, this gives all the unique lengths of words
        in the argument list, which in this case are [3, 3, 5, 2, 8] respectively.
        Since sets don't keep duplicate elements, we're left with {2, 3, 5, 8}.
    """
    print([x for x in [1, 2, 3, 4]])
    print([n - 2 for n in range(10)])
    print([k % 10 for k in range(41) if k % 3 == 0])
    print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

    # Something is fishy here. Can you spot it?
    arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    print([el.append(el[0] * 4) for el in arr])  # => [None, None, None]
    print(arr)

    print([letter for letter in "pYthON" if letter.isupper()])
    print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})


def comprehension_write():
    """
    Practice writing comprehensions.
    
    To generate [1, 3, 5, 7] from [0, 1, 2, 3], we need to multiply each element
    by 2 and add 1.
        [2 * num + 1 for num in nums]
    
    To get the first capitalized letter, we convert the 0th character to uppercase.
        [fruit[0].upper() for fruit in fruits]
    
    To keep only 'apple' and 'pear', we filter on whether the fruit has a 'p' in it
    (although we could use any other appropriate test as well).
        [fruit for fruit in fruits if 'p' in fruit]
    
    To extract the TA's names from a class list, we first filter by whether the
    element starts with 'TA_' and then extract the name using slice syntax.
        [name[3:] for name in people if name.startswith('TA_')]
    
    To construct a list of tuples, we can build the tuples on the fly inside the list
    comprehension.
        [(fruit, len(fruit)) for fruit in fruits]
    
    To build a dictionary mapping fruits to their lengths, we can use a dictionary
    comprehension with syntax {key_fn(el): value_fn(el) for el in collection}
        {fruit:len(fruit) for fruit in fruits}
    """
    nums = [0, 1, 2, 3]
    fruits = ['apple', 'orange', 'pear']
    people = ["TA_parth", "student_poohbear", "TA_michael", "TA_guido", "student_htiek"]

    print([2 * num + 1 for num in nums])  # [1, 3, 5, 7]

    print([fruit[0].upper() for fruit in fruits])  # ['A', 'O', 'P']
    print([fruit for fruit in fruits if 'p' in fruit])  # ['apple', 'pear']

    print([name[3:] for name in people if name.startswith('TA_')])  # ["sam", "guido"]
    print([(fruit, len(fruit)) for fruit in fruits])  # [('apple', 5), ('orange', 6), ('pear', 4)]
    print({fruit:len(fruit) for fruit in fruits})  # {'orange': 6, 'apple': 5, 'pear': 4}


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
    """ 
    We'll figure out what this code does by looking from the inside out
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

####################
#  LINEAR ALGEBRA  #
####################
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


##############
##############
##  PART 2  ##
##############
##############

################
#  DECORATORS  #
################
def memoize(max_size=None, eviction_policy='LRU'):
    # This will throw an error if the eviction policy is invalid
    assert eviction_policy in ['LRU', 'MRU', 'random']

    """
    This is tricky, but we have to define a *new* decorator, based on the
    memoize parameters that just accepts the function.
    """
    def decorator(function):
        # Store the cache on the function
        function._cache = collections.OrderedDict()

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            # Serialize the arguments
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


@memoize(max_size=16, eviction_policy='LRU')
def fib(n):
    """
    What's going on here?

    Calling @memoize(...) will return a *decorator* based on the arguments that
    you provide. That decorator is waiting to take in a function. Because we've
    put it above a function with the @... syntax, the decorator will replace
    this function.
    """
    return fib(n-1) + fib(n-2) if n > 2 else 1


def bind_args(function, *args, **kwargs):
    r"""
    Returns an map from the names of function's arguments to values given by 
    *args and **kwargs. This is more or less an implementation of Python 
    argument bind semantics, but it's not super accurate...
        ¯\_(ツ)_/¯
    
    For example, it doesn't resolve any closure elements or anything, because 
    ahh that's awful. First, positional arguments are bound...

    If you're a student reading this, you can ignore this implementation.
    Pre: *args and **kwargs represent valid parameters
    """
    argspec = inspect.getfullargspec(function)
    sig = inspect.Signature.from_callable(function)
    ba = sig.bind(*args, **kwargs)
    # print(argspec, ba)
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
    """
    Decorate the given function to print out it's arguments and return val if 
    not None.
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
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    print(is_prime(198239813))
    # is_prime(n=198239813)
    # (return) False
    # False

    print(is_prime(4028769383))
    # is_prime(n=4028769383)
    # (return) False
    # False

    @print_args
    def stylize_quote(quote, **kwargs):
        print('> {}'.format(quote))
        print('-'*(len(quote) + 2))
        
        for k, v in kwargs.items():
            print('{k}: {v}'.format(k=k, v=v))

    stylize_quote('Doth mother know you weareth her drapes?', speaker='Iron Man', year='2012', movie='The Avengers')
    # stylize_quote(quote=Doth mother know you weareth her drapes?, kwargs={'speaker': 'Iron Man', 'year': '2012', 'movie': 'The Avengers'})
    # > Doth mother know you weareth her drapes?
    # ------------------------------------------
    # speaker: Iron Man
    # year: 2012
    # movie: The Avengers


    @print_args
    def draw_table(num_rows, num_cols):
        sep = '+' + '+'.join(['-'] * num_cols) + '+'
        line = '|' + '|'.join([' '] * num_cols) + '|'
        
        for _ in range(num_rows):
            print(sep)
            print(line)
        print(sep)
        
    draw_table(10, 10)
    # draw_table(num_rows=10, num_cols=10)
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+
    # | | | | | | | | | | |
    # +-+-+-+-+-+-+-+-+-+-+

    draw_table(3, 8)
    # draw_table(num_rows=3, num_cols=8)
    # +-+-+-+-+-+-+-+-+
    # | | | | | | | | |
    # +-+-+-+-+-+-+-+-+
    # | | | | | | | | |
    # +-+-+-+-+-+-+-+-+
    # | | | | | | | | |
    # +-+-+-+-+-+-+-+-+

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


###################################
#  NESTED FUNCTIONS AND CLOSURES  #
###################################
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

###############
#  FUNCTIONS  #
###############
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
    # Invalid - TypeError: all_together() missing 2 required positional arguments: 'x' and 'y'
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
      ==> nums:  (2, 4, 6) , indent:  True , spaces:  0 , options:  {'a': [4, 5], 'b': 'x'}
    # Valid
    all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})
      ==> x:  8 , y:  9 , z:  2
      ==> nums:  (4, 6, 'z') , indent:  True , spaces: 0 , options:  {'a': [4, 5], 'b': 'x'}
    """
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)


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

    print(append_twice(1)) # => [1, 1]
    print(append_twice(2)) # => [1, 1, 2, 2]
    print(append_twice(3)) # => [1, 1, 2, 2, 3, 3]