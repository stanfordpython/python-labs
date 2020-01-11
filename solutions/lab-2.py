"""
File: lab-2.py
---------------
Reference solutions for Lab 2 for CS 41: Hap.py Code.
Credit to @psarin and @sredmond for contributing solutions.

@psarin 01-10-20 Add remaining solutions
@psarin 11-11-19 Created file
"""
import math
DICTIONARY_PATH = '/usr/share/dict/words'  # Feel free to change this to your dictionary

#############################################
#                  PART 1                   #
#############################################

###########
# WARMUPS #
###########
def say_hello():
    """Prints "Hello, world!" """
    print("Hello, World!")


def fizzbuzz(n):
    """Returns the sum of all numbers < n divisible by 3 or 5.

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
    very many easy functional ways to solve this problem.

    One benefit of this approach is that we do not store the entire
    sequence in memory - since we're only interested in the length, that
    would be wasteful.
    """
    length = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2  # We want to explicitly use integer division here, even though n is even.
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
    if n in cache:
        return cache[n]

    if n % 2 == 0:
        cache[n] = collatz_len_fast(n // 2, cache) + 1
    else:
        cache[n] = collatz_len_fast(3 * n + 1, cache) + 1
    return cache[n]


def max_collatz_len_fast(n):
    """Slightly faster way to compute the longest Collatz sequence for numbers < n

    We use the exact same tactic as in `max_collatz_len` above, with the added
    optimization that we only look over the second half of the range, since everything
    in the first half has a x2 preimage.
    """
    cache = {}
    return max(collatz_len_fast(i, cache) for i in range(n // 2, n))


def print_tictactoe():
    """Print out a tic tac toe board using print's `sep` keyword argument

    Note: this is just one of many ways to solve this problem, chosen to
    illustrate .join, list multiplication, .format, string multiplication,
    and, of course, `sep`.
    """
    row = '|'.join(['  '] * 3)      # row = '  |  |  '
    div = '\n{}\n'.format('+'.join(['-' * 2] * 3))  # div = '--+--+--'
    print(row, row, row, sep=div)


def print_tictactoe_zen():
    """Prints out a tic tac toe board. I bet you could've guessed that, huh?

    Along the lines of "readability counts," there's no reason to use crazy
    Python tricks if (1) they're legitimately slower (construct the string each time)
    and (2) they are not very readable. Instead, it's okay to make your life easy!
    You may have spent a few minutes on this problem. It took me just a few seconds to
    copy and paste! Remember, the Zen of Python makes life easier for the programmer
    rather than the program (and you can take that to the bank)!
    """
    # Using `\` at the end of one line in a multiline string removes the implicit newline.
    s = """\
  |  |
--+--+--
  |  |
--+--+--
  |  |  \
"""
    print(s)


def print_super_tictactoe():
    """Prints a super tic-tac-toe board using print's `sep` keyword.

    Note: As above, this is just one of many ways to accomplish this program, and
    it isn't very readable, or very fast! But, it does illustrate using the `sep`
    keyword.
    """
    row = 'H'.join(['  |  |  '] * 3)  # row = '  |  |  H  |  |  H  |  |  '
    div = '\n'+ 'H'.join(['--+--+--'] * 3) + '\n'  # div = '\n--+--+--H--+--+--H--+--+--\n'
    superdiv = '\n' + '+'.join(['=' * 8] * 3) + '\n'  # superdiv = '\n========+========+========\n'
    block = div.join([row] * 3)
    print(block, block, block, sep=superdiv)


def print_super_tictactoe_zen():
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


###################
# DATA STRUCTURES #
###################
def lattice_paths(m, n):
	"""Computes the number of lattice paths from the top-left corner
    of an m x n grid to the bottom-right, recursively.

    This problem is very self-similar. At any given point, you can step
    to the right or down. So, the number of paths from the top-left of 
    an m x n grid to the bottom-right is equal to:

        (# of paths that start          (# of paths that start
         by going to the right)    +     by going down        )

    The number of paths that start by going to the right is the number of
    paths from the top-left of an m x (n-1) grid to the bottom-right of
    that grid! That's because if you have a path for an m x (n-1) grid,
    you can convert it into a path for an m x n grid by first stepping to
    the right, and then following the path for the m x (n-1) grid.

    Similarly, the number of paths that start by going down is the number
    of paths from the top-left of an (m-1) x n grid to the bottom-right of
    that grid.

    That gives the recursive intution. For the base case, note that when 
    m == 0 or n == 0, the grid is actually one-dimensional, so there's 
    only one way to get to the end: just walk down the line."""
    if m == 0 or n == 0:
        return 1
    
    return lattice_paths(m-1, n) + lattice_paths(m, n-1)

def lattice_paths_memoized(m, n, memoization_dict):
	"""Efficiently computes the number of lattice paths from the 
    top-left corner of an m x n grid to the bottom-right, using recursive
    memoization.

	The base case is the same as the last function but now, we add
	tuples to the memoization dict if they aren't already in the dict.

	Then, at the end, we can just return the value stored in the dict."""
    if m == 0 or n == 0:
        return 1

    if (m, n) not in memoization_dict:
		memoization_dict[(m, n)] = lattice_paths_memoized(m-1, n) + lattice_paths_memoized(m, n-1)

    return memoization_dict[(m, n)]

lattice_paths_memoized(2, 2, {})   # => 6
lattice_paths_memoized(6, 6, {})   # => 924
lattice_paths_memoized(20, 20, {}) # => 137846528820
lattice_paths_memoized(40, 40, {}) # => 107507208733336176461620

def object_reference():
    """Explore the differences between objects and references to objects

    What's happening here? Lists store references to objects, and any operation which
    updates the underlying object in-place (like += on lists, which is equivalent to .extend)
    will change the object that all of the list entries point to. For strings and integers,
    adding a number won't update the underlying object in place, so only the first elements
    are changed. In fact, both strings and integers in Python are "immutable," in the sense
    that all modification operations (like .lower(), .upper(), etc) will create (and return!)
    a new object (a new suitcase).

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
    has been updated in place to contain a 1, printing `s` reflects this change across all of its indices.

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
    """Practice writing comprehensions.

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
    people = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]

    print([2 * num + 1 for num in nums])  # [1, 3, 5, 7]

    print([fruit[0].upper() for fruit in fruits])  # ['A', 'O', 'P']
    print([fruit for fruit in fruits if 'p' in fruit])  # ['apple', 'pear']

    print([name[3:] for name in people if name.startswith('TA_')])  # ["sam", "guido"]
    print([(fruit, len(fruit)) for fruit in fruits])  # [('apple', 5), ('orange', 6), ('pear', 4)]
    print({fruit:len(fruit) for fruit in fruits})  # {'orange': 6, 'apple': 5, 'pear': 4}



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


##################
# BONUS PROBLEMS #
##################
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
    """
    return all([is_cyclone_word(word) for word in phrase.split()])


#############################################
#                  PART 2                   #
#############################################
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


def print_pascal_triangle(n):
    """Print the first n rows of Pascal's triangle.

    We first generate a list of the first n rows of Pascal's triangle.
    This is kind of tricky because the function we've written generates
    the *next* row of Pascal's triangle, based on the previous one.

    The most Pythonic way to keep track of the previous row and update
    it as you generate the next row is using assignment expressions.
    Because you can assign a variable *and* use it at the same time,
    we can assign:

        prev := generate_pascal_row(prev)

    which will add `prev` to the list and update it for the next iteration
    of the loop.

    Then, we convert each of the rows to a string. There are several ways
    to do this. One way is using the map function:

        [' '.join(map(str, row)) for row in rows]

    This might seem a little complicated and perhaps un-Pythonic (for that
    reason), but I think it's reasonably nice because joining a map of 
    str onto an iterable is quite common and readable.

    We haven't learned what the map function is, yet, though, so one
    could instead use a list comprehension:

        [' '.join([str(e) for e in row]) for row in rows]

    This is funcitonally equivalent to the map-based solution, but less
    readable. Instead, this solution does it in two steps.

    The largest row, then, will be the last one, and we can easily 
    calculate its length using the `len` function.

    One of the trickiest pieces of the logic is printing out each
    of the rows, centered. Remember that the '^' alignment specifier
    will center text, where the number that appears after the '^'
    is the length of the string to be returned. So,

        '{:^10}'.format('CS41') # => '   CS41   '

    We can use nested format specification to fill out the string
    length with a variable:

        '{:^{}}'.format('CS41', 10) # => '   CS41   '

    Using that, we can get a centered row, where the width is equal
    to the width of the longest row."""
    prev = []
    rows = [prev := generate_pascal_row(prev) for _ in range(n)]
    
    rows = [[str(e) for e in row] for row in rows]
    rows = [' '.join(row) for row in rows]
    width = len(rows[-1])
    
    # Print each row
    for row in rows:
        print("{row:^{width}}".format(row=row, width=width))


def is_triad_word(word, english):
    """Returns whether a word is a triad word.

    There are many solutions to this problem, but the easiest is to slice our
    string using the slice syntax to extract two words (built from alternating
    letters), and then check that both of those words are valid English words.
    """
    return word[::2] in english and word[1::2] in english


def is_triad_phrase(phrase, english):
    """Returns whether all the space-delimited words in `phrase` are triad words

    A phrase is a triad phrase if and only if all of its component words are
    triad words, so we first split the phrase into words using .split(), and then
    check if all of the words are triad words.

    In Python, you can use `all` to check if all elements of an iterable are True-y,
    short-circuiting as soon as a False-y element is found. Currently, we're computing
    the triad-ness of all of the words before evaluating `all`, but there is a way to
    stream the words through is_triad_word to `all` using generator expressions, which
    we'll learn about Week 4.

    This strategy is repeated for the other types of phrases, and the same caveats apply
    for those problems as well.
    """
    return all([is_triad_word(word, english) for word in phrase.split()])


def character_distance(left, right):
    """Return the alphabetic distance between two uppercase one-character strings.

    For example, character_distance('R', 'B') returns 16, since 'B' has value 66
    and 'R' has value 82.
    """
    return abs(ord(left) - ord(right))


def is_surpassing_word(word):
    """Returns whether a word is a surpassing word.

    As usual, there are many solutions, but we choose to compute the distances between
    pairs of characters (zipping together word with word[1:]) first, and then check
    whether these distances are all increasing (again using zip). This is certainly not
    the fastest or most readable solution (since we are first computing all adjacent
    distances, and then only later checking to see if the distances are in increasing
    order), but it illustrates the use of zip to associate adjacent pairs of elements
    of a sequence. For example, consider the case where `word` is SUPERB.

        word     ->  S  U  P  E  R  B
        word[1:] ->  U  P  E  R  B
                     ----------------
                     SU UP PE ER RB
        zip(word, word[1:]) generates (S, U), (U, P), (P, E), (E, R), (R, B)

    Since the last B is unmatched, it isn't included in the results generated by zip.
    We immediately unpack the tuples generated by zip into a left term and a right term.

    We use the same trick to compare distances, checking if for all pairs, the left term
    is less than the right term (reminiscent of a stopping condition for bubble sort).
    """
    distances = [character_distance(left, right) for left, right in zip(word, word[1:])]
    return all(left < right for left, right in zip(distances, distances[1:]))


def is_surpassing_phrase(phrase):
    """Returns whether all the space-delimited words in `phrase` are surpassing words

    A phrase is a surpassing phrase if and only if all of its component words are
    triad words, so we first split the phrase into words using .split(), and then
    check if all of the words are triad words.
    """
    return all([is_surpassing_word(word) for word in phrase.split()])


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
    """
    return all([is_cyclone_word(word) for word in phrase.split()])


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


def get_word_counts():
    """Print the number of English words satisfying a number of conditions.

    Specifically, print the number of English words that are
        (1) Triad words
        (2) Surpassing words
        (3) Cyclone words
        (4) Triangle words
    """
    english = get_english_words(DICTIONARY_PATH)
    triad_words = [word for word in english if is_triad_word(word, english)]
    surpassing_words = [word for word in english if is_surpassing_word(word)]
    cyclone_words = [word for word in english if is_cyclone_word(word)]
    triangle_words = [word for word in english if is_triangle_word(word)]

    print("Number of triad words: {}".format(len(triad_words)))
    print("Number of surpassing words: {}".format(len(surpassing_words)))
    print("Number of cyclone words: {}".format(len(cyclone_words)))
    print("Number of triangle words: {}".format(len(triangle_words)))


def get_english_words(dictionary_path):
    """Returns a set of trimmed, capitalized English words from a path to a dictionary.

    The dictionary is assumed to have one English word per line.

    If dictionary_path can not be read or is formatted incorrectly, a default English word
    set is returned containing some fruits.

    Note that we keep the file open for as little time as possible, which is
    generally a good practice. One downside of this implementation is that it
    buffers all of the words in memory (first as a string, and later as a collection
    of lines, but the word list is a known finite size (and that size isn't *too*
    big), so this approach will work fine. Iterating through the lines in the file
    with a for loop could mitigate this downside.

    We then use a set comprehension to build an uppercased collection of all of
    the words in the dictionary.

    Note that we choose to represent the English words as a set, because we want fast
    membership testing (using `in`) and also want to be able to iterate over all words.
    """
    try:
        with open(dictionary_path, 'r') as f:
            content = f.read()
        return {line.strip().upper() for line in content.split('\n') if line}
    except OSError:
        return {'APPLE', 'BANANA', 'PEAR', 'ORANGE'}


def polygon_collision(poly1, poly2):
    """As a bonus problem, we're not publishing the solution to this :)

    If you're interested in reading more about the strategy to solve it,
    check out https://www.codeproject.com/Articles/15573/2D-Polygon-Collision-Detection
    """
    pass

