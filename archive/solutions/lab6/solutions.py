#!/usr/bin/env python3 -tt
"""
File: lab6solutions.py
----------------------
Reference solutions to Lab 3 for CS41: Hap.py Code.

Honestly, there wasn't much code for this lab, so this file is relatively small.

Did you read through [some modules](https://docs.python.org/3.4/library/) from the Standard Library?
Scouring Python's documentation is a fantastic way to learn new tools.


Revision history:
@sredmond 05-11-2017 Updates for spr-1617
@sredmond 05-02-2016 Created
"""
import re
import collections
import string
import itertools

DICTIONARY_FILENAME = '/usr/share/dict/words'

def horsin_around():
    Animal = collections.namedtuple('Animal', ['name', 'kind', 'color', 'age'])
    lassie = Animal('Lassie', 'dog', 'black', 12)
    astro = Animal('Astro', 'dog', 'grey', 15)
    mrpb = Animal('Mr. Peanut Butter', 'dog', 'golden', 35)
    tinkles = Animal('Mr. Tinkles', 'cat', 'white', 7)
    pupper = Animal('Bella', 'pupper', 'brown', 0.5)
    doggo = Animal('Max', 'doggo', 'brown', 5)
    seuss = Animal('The Cat in the Hat', 'cat', 'stripey', 27)
    pluto = Animal('Pluto (Disney)', 'dog', 'orange', 3)
    yertle = Animal('Yertle', 'turtle', 'green', 130)

    animals = [lassie, astro, mrpb, tinkles, pupper, doggo, seuss, pluto, yertle]

    for animal in animals:
        if animal.kind in ['dog', 'doggo', 'pupper']:
            if animal.age > 5:
                age_descriptor = 'an old'
            else:
                age_descriptor = 'a young'

            # You can use named format parameters, which is more readable,
            # although it can get verbose.
            print('{name} is {descr} {color} {kind} who is {age} years old.'.format(
                    name=animal.name, descr=age_descriptor, color=animal.color,
                    kind=animal.kind, age=animal.age
            ))
        else:
            # Or you can use positional format parameters, which are shorter
            # at the expense of readability.
            print('{} is a non-canine {} {}.'.format(animal.name, animal.color, animal.kind))

def most_common_words():
    with open(DICTIONARY_FILENAME) as f:
        return collections.Counter(map(len, f.read().split())).most_common(3)

def mask(word, letter):
    return ''.join('-' if letter != ch else letter for ch in word)

def largest_families(words, letter, num_families):
    # We maintain a counter for the size of masks, and a defaultdict of the families
    families = collections.defaultdict(list)
    family_sizes = collections.Counter()
    for word in words:
        word_mask = mask(word, letter)
        families[word_mask].append(word)
        family_sizes[word_mask] += 1

    largest = []
    for family_key, _unused_family_count in family_sizes.most_common(num_families):
        largest.append(families[family_key])
    return largest

def test_largest_families():
    with open(DICTIONARY_FILENAME, 'r') as f:
        words = f.read().lower().split()

    print(largest_families(words, 'e', 2))

def wordplay():
    with open(DICTIONARY_FILENAME, 'r') as f:
        for line in f:
            if not re.match(r'.*a.*e.*i.*o.*u.*', line.strip()):
                continue
            print(line.strip())



def regex_crossword_check(horizontal_patterns, vertical_patterns, candidate, alphabet=string.ascii_uppercase):
    # Check horizontal clues
    for pattern, horiz_line in zip(horizontal_patterns, candidate):
        line = ''.join(horiz_line)
        if not re.match(pattern, line):
            return False

    # Check vertical clues
    for pattern, vert_line in zip(vertical_patterns, zip(*candidate)):
        line = ''.join(vert_line)
        if not re.match(pattern, line):
            return False

    return True

def test_regex_crossword_check():
    horiz = [r'HE|LL|O+', r'[PLEASE]+']
    vert = [r'[^SPEAK]+', r'EP|IP|EF']
    candidate = [
        ['H', 'E'],
        ['L', 'P']
    ]
    print(regex_crossword_check(horiz, vert, candidate))

    horiz = [r'(Y|F)(.)\2[DAF]\1', r'(U|O|I)*T[FRO]+', r'[KANE]*[GIN]*']
    vert = [r'(FI|A)+', r'(YE|OT)K', r'(.)[IF]+', r'[NODE]+', r'(FY|F|RG)+']
    candidate = [
        ['F', 'O', 'O', 'D', 'F'],
        ['I', 'T', 'F', 'O', 'R'],
        ['A', 'K', 'I', 'N', 'G']
    ]
    print(regex_crossword_check(horiz, vert, candidate))


def regex_crossword_solve(horizontal_patterns, vertical_patterns, width, height, alphabet=string.ascii_uppercase):
    """Solves a regex crossword.

    As a super challenge, we implement a very naive solution to this problem. For each horizontal patttern, we generate
    all satisfying strings, and then for every element in the product of these possibilities, we verify the vertical patterns."""

    # Optimization: if width > height, solve for height first
    if width > height:
        for transposed_solution in regex_crossword_solve(vertical_patterns, horizontal_patterns, height, width, alphabet):
            yield tuple(''.join(horiz_letters) for horiz_letters in zip(*transposed_solution))
        return

    horizontal_possibilities = []
    horizontal_patterns = map(re.compile, horizontal_patterns)
    for horiz_pattern in map(re.compile, horizontal_patterns):
        successes = []
        for line in map(''.join, itertools.product(alphabet, repeat=width)):
            if horiz_pattern.fullmatch(line):  # Don't worry about full-match - widths are same
                successes.append(line)
        horizontal_possibilities.append(successes)

    vertical_patterns = [re.compile(pattern) for pattern in vertical_patterns]
    for horizontal_choices in itertools.product(*horizontal_possibilities):
        success = True
        for vert_line, vert_pattern in zip(map(''.join, zip(*horizontal_choices)), vertical_patterns):
            if not vert_pattern.fullmatch(vert_line):
                success = False
        if success:
            yield horizontal_choices



def test_regex_crossword_solve():
    horiz = [r'HE|LL|O+', r'[PLEASE]+']
    vert = [r'[^SPEAK]+', r'EP|IP|EF']
    for solution in regex_crossword_solve(horiz, vert, 2, 2):
        print(''.join(solution))

    horiz = [r'(Y|F)(.)\2[DAF]\1', r'(U|O|I)*T[FRO]+', r'[KANE]*[GIN]*']
    vert = [r'(FI|A)+', r'(YE|OT)K', r'(.)[IF]+', r'[NODE]+', r'(FY|F|RG)+']
    for solution in regex_crossword_solve(horiz, vert, 5, 3):
        print(''.join(solution))


def multidirectional(horizontal_patterns, vertical_patterns, width, height, alphabet=string.ascii_uppercase):
    """As a super challenge, we don't implement the solution to this."""

def minimal_regex(positives, negatives):
    """As a super challenge, we don't implement the solution to this."""

def tabulate(f, start=0, step=1):
    return map(f, itertools.count(start, step))

if __name__ == '__main__':
    print(most_common_words())
    test_largest_families()
    test_regex_crossword_check()
    test_regex_crossword_solve()
