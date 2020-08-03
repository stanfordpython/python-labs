"""
File: data-structures.py
------------------------

Data structures, woo hoo!
"""
import math
from typing import *

#############################################
#                  PART 1                   #
#############################################

###########
# WARMUPS #
###########
def say_hello():
    """
    Prints "Hello, world!"
    """
    pass


def fizzbuzz(n: int):
    """
    Returns the sum of all numbers < n divisible by 3 or 5.
    """
    pass


def test_fizzbuzz():
    print(fizzbuzz(41))   # => 408
    print(fizzbuzz(1001)) # => ???


def collatz_len(n: int):
    """
    Computes the length of the Collatz sequence starting at `n`.
    """
    pass


def max_collatz_len(n: int):
    """
    Computes the longest Collatz sequence length for starting numbers < n
    """
    pass


def test_max_collatz_len():
    print(collatz_len(13))  # => 10
    print(max_collatz_len(1000))

    # Challenge: Only attempt to solve these if you feel very comfortable with 
    # this material.
    # print(max_collatz_len(1000000))
    # print(max_collatz_len(100000000))


def print_tictactoe():
    """Print out a specific partially-filled tic-tac-toe board."""
    pass


def print_super_tictactoe():
    """Print an empty SUPER tic-tac-toe board."""
    pass


###################
# DATA STRUCTURES #
###################
def comprehension_read():
    """
    Practice reading comprehensions and explore oddities with function calls by
    uncommenting various lines of this function.
    """
    # print([x for x in [1, 2, 3, 4]])
    # print([n - 2 for n in range(10)])
    # print([k % 10 for k in range(41) if k % 3 == 0])
    # print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

    # Something is fishy here. Can you spot it?
    # arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    # print([el.append(el[0] * 4) for el in arr]) # What is printed?
    # print(arr) # What is the content of arr at this point?

    # print([letter for letter in "pYthON" if letter.isupper()])
    # print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})


def comprehension_write():
    """
    Practice writing comprehensions.
    """
    nums = [0, 1, 2, 3]
    fruits = ['apple', 'orange', 'pear']
    people = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]

    # Add your comprehensions here!


def lattice_paths(m: int, n: int):
    """
    Computes the number of lattice paths from the top-left corner
    of an m x n grid to the bottom-right, recursively.
    """
    pass


def test_lattice_paths():
    print(lattice_paths(2, 2)) # => 6
    print(lattice_paths(6, 6)) # => 924
    #print(lattice_paths(20, 20)) # => this takes too long without memoization!
    #print(lattice_paths(40, 40)) # => this takes WAY too long without memoization!


def lattice_paths_cached(m, n, cache):
    """
    Efficiently computes the number of lattice paths from the 
    top-left corner of an m x n grid to the bottom-right, using recursive
    memoization.
    """
    pass


def test_lattice_paths_memoized():
    cache = {}
    lattice_paths_cached(2, 2, cache)   # => 6
    lattice_paths_cached(6, 6, cache)   # => 924
    lattice_paths_cached(20, 20, cache) # => 137846528820
    lattice_paths_cached(40, 40, cache) # => 107507208733336176461620


def object_reference():
    """
    Explore the differences between objects and references to objects.
    """
    s = [0] * 3
    s[0] += 1
    print(s)

    s = [''] * 3
    s[0] += 'a'
    print(s)

    s = [[]] * 3
    s[0] += [1]
    print(s)


def gcd(a: int, b: int):
    """
    Return the GCD of two numbers.
    """
    pass


def test_gcd():
    gcd(10, 25) # => 5
    gcd(14, 15) # => 1
    gcd(3, 9) # => 3
    gcd(1, 1) # => 1


def flip_dict(d: Dict):
    """
    Swap the keys and values in a dictionary, where duplicated values map to a 
    list of keys.
    """
    pass


def test_flip_dict():
    fav_animals = {
        'parth': 'unicorn',
        'michael': 'unicorn',
        'sam': 'unicorn',
        'zheng': 'tree',
        'theo': 'unicorn',
        'alex': 'dog',
        'nick': 'daisy'
    }
    print(flip_dict(fav_animals))


##################
# BONUS PROBLEMS #
##################
def generate_pascal_row(row: List[int]):
    """
    Generate the successive row in Pascal's triangle.
    """
    pass


def test_generate_pascal_row():
    generate_pascal_row([1, 2, 1])  # => [1, 3, 3, 1]
    generate_pascal_row([1, 4, 6, 4, 1])  # => [1, 5, 10, 10, 5, 1]
    generate_pascal_row([])  # => [1]


def print_pascal_triangle(n: int):
    """
    Print the first n rows of Pascal's triangle.
    """
    pass


# Feel free to change this to your dictionary:
DICTIONARY_PATH = '/usr/share/dict/words'
def load_english():
    """
    Load and return a collection of english words from the DICTIONARY_FILE.
    """
    pass


def is_cyclone_word(word: str):
    """
    Returns whether a word is a cyclone word.
    """
    pass


def is_cyclone_phrase(phrase: str):
    """
    Returns whether all the space-delimited words in phrases are cyclone words
    """
    pass


def all_cyclone_words():
    """
    Returns a list of all cyclone words.
    """
    pass


def is_triad_word(word: str):
    """
    Returns whether a word is a triad word.
    """
    pass


def is_triad_phrase(phrase: str):
    """
    Returns whether all the space-delimited words in `phrase` are triad words
    """
    pass


def all_triad_words():
    """
    Returns a list of all triad words.
    """
    pass


def character_distance(left: str, right: str):
    """
    Return the alphabetic distance between two uppercase one-character strings.

    For example, character_distance('R', 'B') returns 16, since 'B' has value 66
    and 'R' has value 82.
    """
    return abs(ord(left) - ord(right))


def is_surpassing_word(word: str):
    """
    Returns whether a word is a surpassing word.
    """
    pass


def is_surpassing_phrase(phrase: str):
    """
    Returns whether all the space-delimited words in `phrase` are surpassing 
    words.
    """
    pass


def all_surpassing_words():
    """
    Returns a list of all surpassing words.
    """
    pass


def is_triangle_number(num: int):
    """
    Returns whether a number is a triangle number. This might be a helpful 
    function to implement!
    """
    pass


def is_triangle_word(word: str):
    """
    Returns whether a word is a triangle word.
    """
    pass


def all_triangle_words():
    """
    Returns a list of all surpassing words.
    """
    pass


def polygon_collision(poly1: List[Tuple[int, int]], 
                      poly2: List[Tuple[int, int]]):
    """
    Determines if poly1 and poly2 intersect.
    """
    pass


TESTABLE = [
    say_hello,
    fizzbuzz,
    test_fizzbuzz,
    collatz_len,
    max_collatz_len,
    test_max_collatz_len,
    print_tictactoe,
    print_super_tictactoe,
    comprehension_read,
    comprehension_write,
    lattice_paths,
    test_lattice_paths,
    test_lattice_paths_memoized,
    object_reference,
    gcd,
    test_gcd,
    flip_dict,
    test_flip_dict,
    generate_pascal_row,
    test_generate_pascal_row,
    print_pascal_triangle,
    load_english,
    is_cyclone_word,
    is_cyclone_phrase,
    all_cyclone_words,
    is_triad_word,
    is_triad_phrase,
    all_triad_words,
    character_distance,
    is_surpassing_word,
    is_surpassing_phrase,
    all_surpassing_words,
    is_triangle_number,
    is_triangle_word,
    all_triangle_words,
    polygon_collision
]