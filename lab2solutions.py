#!/usr/bin/env python3 -tt
"""
File: lab2solutions.py
----------------------
Reference solutions to Lab 2 for CS41: Hap.py Code.

Revision history:
@sredmond 04-08-2016 Added lots of comments
@sredmond 04-07-2016 Minor bugs fixed
@sredmond 04-04-2016 Created
"""

import math

def hello():
    """Prints "Hello, world!" """
    print("Hello, World!")


def tictactoe():
    """Print out a tic tac toe board using print's `sep` keyword argument

    Note: this is just one of many ways to solve this problem, chosen to
    illustrate .join, list multiplication, .format, string multiplication,
    and, of course, `sep`.
    """
    row = '|'.join(['  '] * 3)      # row = '  |  |  '
    div = '\n{}\n'.format('-' * 8)  # div = '---------'
    print(row, row, row, sep=div)


def tictactoe_zen():
    """Prints out a tic tac toe board. I bet you could've guessed that, huh?

    Along the lines of "readability counts," there's no reason to use crazy
    Python tricks if (1) they're legitimately slower (construct the string each time)
    and (2) they are not very readable. Instead, it's okay to make your life easy!
    You may have spent a few minutes on this problem. It took me just a few seconds to
    copy and paste! Remember, the Zen of Python makes life easier for the programmer
    rather than the program (and you can take that to the bank)!
    """
    # using `\` at the end of one line in a multiline string removes the implicit newline.
    s = """\
  |  |
--+--+--
  |  |
--+--+--
  |  |  \
"""
    print(s)


def super_tictactoe():
    """Prints a super tic-tac-toe board using print's `sep` keyword.

    Note: As above, this is just one of many ways to accomplish this program, and
    it isn't very readable, or very fast! But, it does illustrate using the `sep`
    keyword.
    """
    row = 'H'.join(['  |  |  '] * 3) + '\n'
    div = 'H'.join(['--+--+--'] * 3) + '\n'
    superdiv = '+'.join(['=' * 8] * 3) + '\n'
    block = div.join([row] * 3)
    print(block, block, block, sep=superdiv)


def super_tictactoe_zen():
    """Prints a super tic tac toe board.

    This solution is much more readable than the one above. And it's faster! Great!
    """
    s = """\
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
========+========+========
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
========+========+========
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  \
"""
    print(s)


def fizzbuzz(n):
    """Returns the sum of all numbers <= n divisible by 3 or 5.

    This iterative approach will work really well, and if it gets the job done
    reasonably quickly, that's all we should ask for.

    If you want to write this in one line, the following will work:

        return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

    However, that line isn't particularly Pythonic, since we're basically just
    compressing the syntax of an iterative for loop into one line - no big changes
    except for the use of `sum`.

    Another approach, as we'll learn about soon, is to use `filter`:

        return sum(filter(lambda i: i % 3 == 0 and i % 5 == 0, range(n)))

    However, in many ways, this isn't much different, since we're still specifying a
    function (admittedly, a `lambda` or anonymous function - which we'll learn about Week 4)
    over our range of numbers.

    For a job this simple, the iterative approach will suffice.
    """
    count = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


def collatz_len(n):
    """Computes the length of the Collatz sequence starting at `n`.

    While this iterative approach might look "unpythonic" at first,
    the Collatz sequence is a very iterative algorithm, and there aren't
    very many good functional ways to solve this problem.

    One benefit of this approach is that we do not store the entire
    sequence in memory - since we're only interested in the length, that
    would be wasteful.
    """
    length = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        length += 1  # Note: Python has no increment operator (like ++), so we use += 1
    return length


def max_collatz_len(n):
    """Computes the longest Collatz sequence length for starting numbers < n

    In Python, the `max` function returns the largest element of some collection.
    Since "finding the max element" isn't naturally iterative (although it can be
    solved iteratively), we can use this functional-looking code to compute the
    maximal collatz length. Note, however, that this approach buffers the list of
    lengths in memory (due to the list comprehension). In general, we can mitigate
    this problem using a generator comprehension (look it up!) rather than a list
    comprehension, but we'll cover that later in the course.

    An even more Pythonic way to solve this problem is to use `map`, which applies a
    function to all elements of a sequence.

        return max(map(collatz_len, range(1, n)))

    """
    return max([collatz_len(i) for i in range(1, n)])


def collatz_len_fast(n, cache):
    """Slightly more clever way to find the collatz length.

    A dictionary is used as a cache of previous results, and since
    the dictionary passed in is mutable, our changes will reflect
    in the caller.
    """
    if n == 1:
        return 1
    if i in cache:
        return cache[i]

    if n % 2 == 0:
        cache[i] = collatz_len_fast(n / 2, cache) + 1
    else:
        cache[i] = collatz_len_fast(3 * n + 1, cache) + 1
    return cache[i]

def max_collatz_len_fast(n):
    """Slightly faster way to compute the longest Collatz sequence for numbers < n

    We use the exact same tactic as in `max_collatz_len` above, with the added
    optimization that we only look over the second half of the range, since everything
    in the first half has a x2 preimage.

    """
    cache = {}
    return max([collatz_len_fast(i) for i in range(n / 2, n)])

def converter():
    """Convert a temperature from Fahrenheit to Celsius.

    This problem exists only to check that you're running Python 3, where
    `input` returns a string and division is double division by default, in
    contrast to Python 2, where `input` quasi-evaluates it's input and division
    is integer (floored) division by default.

    Note: There's some extra code here (the try/except/else stuff) so that the
    solutions can continue to run after you break out of the converter. We'll
    talk about advanced exception handling Week 5.
    """
    print("Convert from Fahrenheit to Celsius with this lovely tool!")
    print("For the purposes of the lab solutions, hit CTRL+C to quit.")
    while True:
        try:
            fahr = float(input("Temperature F? "))
        except KeyboardInterrupt:
            print("\nExiting converter...")
            break
        except ValueError as exc:
            print(exc)
        else:
            cels = (fahr - 32) * 5 / 9
            # cels = round(cels, 2)  # Round to two decimal places
            print("It is {} degrees Celsius".format(cels))


###################
# DATA STRUCTURES #
###################

def object_reference():
    """Explore the differences between objects and references to objects

    What's happening here? Lists store references to objects, and any operation which
    updates the underlying object in place (like += on lists, which expands to .extend)
    will change the object that all of the list entries point to. For strings and integers,
    adding a number won't update the underlying object in place, so only the first elements
    are changed. In fact, both strings and integers in Python are "immutable," in the sense
    that all modification operations (like .lower(), .upper(), etc) will create (and return!)
    a new string object.

    Visually, it looks something like this (forgive the ASCII art):

        s = [[]]

        # s[0] ----->  []    s[0] points to one list object

        s *= 3

        # s[0] __
        #        \\
        # s[1] ---==>  []    All three indices point to the same (individual!) list object!
        #         /
        # s[2] __/

        s[0].append(1)

        # s[0] __
        #        \\
        # s[1] ---==>  [1]   The update reflects across all list indices.
        #         /
        # s[2] __/

    Since all the elements of the list are references to the (one and only) list object that
    has been updated to contain a 1, printing `s` reflects this change across all of its indices.

    Bonus! Setting one of the elements of `s` to point to a new object will change this structure.
    For example,

        s[0] = [4, 1]  # Creates a new list objects containing [4, 1] and points s[0] there

        # s[0] ----->  [4, 1]
        # s[1] ----=>  [1]   Now, only s[1] and s[2] share a reference.
        # s[2] __/
    """
    s = [0] * 3
    s[0] += 1
    print(s)  # [1, 0, 0]

    s = [''] * 3
    s[0] += 'a'
    print(s)  # ['a', '', '']

    s = [[]] * 3
    s[0] += [1]
    print(s)  # [[1], [1], [1]]... what?!


def gcd(a, b):
    """Return the GCD of two numbers.

    The GCD can be computed iteratively as shown below, with the two elements
    progressively getting smaller and smaller. The use of tuple-packing and
    unpacking allows us to communicate this paired update step in one line
    without needing to use a temporary variable.

    For example, gcd(91, 35) is evaluated as follows:

    gcd(91, 35)
        a, b = 91, 35
        a, b = (35, 91 % 35) = 35, 21
        a, b = (21, 35 % 21) = 21, 14
        a, b = (14, 21 % 14) = 14,  7
        a, b = ( 7, 14 %  7) =  7,  0
        b = 0, so we return 7

    Note: if a < b, then a % b = a, so the values of a and b will be swapped.
    """
    while b:
        a, b = b, a % b
    return a


def flip_dict(d):
    """Swap the keys and values in a dictionary, where duplicated values map to a list of keys

    The easiest way to solve this problem is by looping over the keys and values
    of the dictionary using `.items()`. If the value hasn't been seen before, we need
    to set some reasonable default value in our dictionary - in this case, a list to
    store the associated keys. Then, we can append (in-place!) our key to the list
    of keys associated to this value.

    It's possible to write this update step in one line using the default of `.get()`

        out[value] = out.get(value, []).append(key)

    However, I don't think that looks nearly as readable.

    Note: there is a tool in the `collections` module from the standard library
    called `defaultdict` which exports this functionality. You provide it a factory
    method for creating default values in the dictionary (in this case, a list.)
    """
    out = {}
    for key, value in d.items():
        if value not in out:
            out[value] = []
        out[value].append(key)
    return out


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
        a string, as you might guess.

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
    """Practice writing comprehensions.

    To generate [1, 3, 5, 7] from [0, 1, 2, 3], we need to multiply each element
    by 2 and add 1.

        [2 * num + 1 for num in arr]

    To generate [True, False, True, False] from [3, 5, 9, 8], we could use whether
    each element is divisible by 3 (or any other such test).

        [num % 3 == 0 for num in arr]

    To extract the TA's names from a class list, we first filter by whether the
    element starts with 'TA_' and then extract the name using slice syntax.

        [name[3:] for name in arr if name.startswith('TA_')]

    To get the first capitalized letter, we convert the 0th character to uppercase.

        [fruit[0].upper() for fruit in arr]

    To keep only 'apple' and 'pear', we filter on whether the fruit has a 'p' in it
    (although we could use any other appropriate test as well).

        [fruit for fruit in arr if 'p' in fruit]

    To construct a list of tuples, we can build the tuples on the fly inside the list
    comprehension.

        [(fruit, len(fruit)) for fruit in arr]

    To build a dictionary mapping fruits to their lengths, we can use a dictionary
    comprehension with syntax {key_fn(el): value_fn(el) for el in arr}

        {fruit:len(fruit) for fruit in arr}
    """
    arr = [0, 1, 2, 3]
    print([2 * num + 1 for num in arr])  # [1, 3, 5, 7]

    arr = [3, 5, 9, 8]
    print([num % 3 == 0 for num in arr])  # [True, False, True, False]

    arr = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
    print([name[3:] for name in arr if name.startswith('TA_')])  # ["sam", "guido"]

    arr = ['apple', 'orange', 'pear']
    print([fruit[0].upper() for fruit in arr])  # ['A', 'O', 'P']
    print([fruit for fruit in arr if 'p' in fruit])  # ['apple', 'pear']
    print([(fruit, len(fruit)) for fruit in arr])  # [('apple', 5), ('orange', 6), ('pear', 4)]
    print({fruit:len(fruit) for fruit in arr})  # {'orange': 6, 'apple': 5, 'pear': 4}


def is_cyclone_word(word):
    """Returns whether a word is a cyclone word.

    There are many different approach to solving this problem, but the one
    shown below using a clever, little-known feature of Python list-slicing.
    List slices can be assigned into! For example,

        l = [0, 0, 0, 0, 0, 0, 0, 0]
        l[:4] = range(4)
        print(l)  # => [0, 1, 2, 3, 0, 0, 0, 0]

    In this case, we put the first half of the word into every other character
    (slicing with a step size of 2) starting at index 0, and put the reversed
    second half of the word into every other character starting at index 1.

    Then, we can test if each letter is less than its neighbor alphabetically
    by zipping together the letters and the offset letters, and tuple-unpack
    inside the list comprehension.

    To be completely honest, a purely iterative approach would work just as
    well, if not better (less auxiliary memory, more readable), but I wanted
    to illustrate some cool features of Python (assigning into list slices as
    Lvalues, zipping a sequence with itself to generate pairs, etc).
    """
    word = word.upper()
    letters = [None] * len(word)
    half = (len(word) + 1) // 2
    letters[::2] = word[:half]
    letters[1::2] = word[:half - 1:-1]
    return all([left <= right for left, right in zip(letters, letters[1:])])


def is_cyclone_phrase(phrase):
    """Returns whether all the space-delimited words in phrases are cyclone words

    A phrase is a cyclone phrase if and only if all of its component words are
    cyclone words, so we first split the phrase into words using .split(), and then
    check if all of the words are cyclone words.

    In Python, you can use `all` to check if all elements of an iterable are True-y,
    short-circuiting as soon as a False-y element is found. Currently, we're computing
    the cyclone-ness of all of the words before evaluating `all`, but there is a way to
    stream the words through is_cyclone_word to all using generator expressions, which
    we'll learn about Week 4.
    """
    return all([is_cyclone_word(word) for word in phrase.split()])


def generate_pascal_row(row):
    """Generate the successive row in Pascal's triangle.

    While there are many iterative approaches, we can zip together offsets of
    the given row to generate pairs of elements, which we sum to form the final
    data structure.

    For example, if row = [1, 4, 6, 4, 1], then

        [0] + row  # => [0, 1, 4, 6, 4, 1]
        row + [0]  # => [1, 4, 6, 4, 1, 0]

    Adding together corresponding entries with zip and a list comprehension gives

                        [1, 5, 10, 10, 5, 1]

    Just like we wanted!
    """
    if not row: return [1]
    return [left + right for left, right in zip([0] + row, row + [0])]


def is_triangle_number(num):
    """Returns whether a number is a triangle number.

    A triangle number n is one for which there exists an integer x with
    n = (x^2 + x) / 2. Solving this quadratic equation gives

        x = (-1 +- sqrt(1 + 8n)) / 2

    which will be an integer if and only if 1 + 8n is a perfect square.
    Note: if 1 + 8n is a perfect square, it's square root will be odd,
    so we don't need to worry about the division by 2.

    A number is a perfect square if and only if the square of the floor of
    the square root gives back the original number.

    Note: there are other ways to solve this problem (notably, the iterative
    approach of generating triangle numbers until you either hit or pass num)
    which will work fine! In which cases would each approach be better?
    """
    discrim = 8 * num + 1
    base = int(math.sqrt(discrim))
    return base * base == discrim


def is_triangle_word(word):
    """Returns whether a word is a triangle word.

    A word is a triangle word if and only if the sum of its character values is
    a triangle number. Here, we show the iterative approach (as a change-of-pace),
    although we'll see a way to solve this functionally Week 4.
    """
    count = 0
    for ch in word.upper().strip():
        count += ord(ch) - ord('A') + 1
    return is_triangle_number(count)


def triangle_words():
    """Returns the number of triangle words in the English dictionary.

    Note that we keep the file open for as little time as possible, which is
    generally a good practice. One downside of this implementation is that it
    buffers all of the words in memory, but the word list is a known finite size
    (and that size isn't *too* big), so this approach will work fine. Iterating
    through the lines in the file with a for loop with mitigate this downside.

    We then use a set comprehension to build an uppercased collection of all of
    the triangle words in the dictionary, and return its length.
    """
    with open('/usr/share/dict/words', 'r') as f:
        lines = f.readlines()

    triangle_words = {line.upper().strip() for line in lines if is_triangle_word(line)}
    return len(triangle_words)


def polygon_collision(poly1, poly2):
    """As a bonus problem, we're not publishing the solution to this :)

    If you're interested in reading more about the strategy to solve it,
    check out http://www.phailed.me/2011/02/polygonal-collision-detection/
    """
    pass  #


if __name__ == '__main__':
    """Runs each of the lab solution functions and prints the docstring"""
    fns = [
        # Comment out any functions that you do not want to run
        (hello, (), {}),
        (tictactoe, (), {}),
        (tictactoe_zen, (), {}),
        (super_tictactoe, (), {}),
        (super_tictactoe_zen, (), {}),
        (fizzbuzz, (1001,), {}),
        (max_collatz_len, (1000,), {}),
        (converter, (), {}),
        (object_reference, (), {}),
        (gcd, (91, 35), {}),
        (flip_dict, ({"CA": "US", "NY": "US", "ON": "CA"},), {}),
        (comprehension_read, (), {}),
        (comprehension_write, (), {}),
        (is_cyclone_phrase, ("all alone at noon",), {}),
        (generate_pascal_row, ([1, 4, 6, 4, 1],), {}),
        (triangle_words, (), {}),
    ]
    for fn, args, kwargs in fns:
        name = fn.__name__
        print("*" * len(name))     # header
        print(name)                # function name
        print(fn.__doc__)          # function docstring
        res = fn(*args, **kwargs)  # variadic argument unpacking - cool stuff! More Week 3.
        if res:
            print(res)
        input("Press [ENTER] to continue...")
    print("Done!")
