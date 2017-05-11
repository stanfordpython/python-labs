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

def wordplay():
    with open('/usr/share/dict/words', 'r') as f:
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
    # if width > height:
    #     for transposed_solution in regex_crossword_solve(vertical_patterns, horizontal_patterns, height, width, alphabet):
    #         yield tuple(''.join(horiz_letters) for horiz_letters in zip(*transposed_solution))
    #     return

    horizontal_possibilities = []
    horizontal_patterns = map(re.compile, horizontal_patterns)
    for horiz_pattern in map(re.compile, horizontal_patterns):
        successes = []
        for line in map(''.join, itertools.product(alphabet, repeat=width)):
            if horiz_pattern.match(line):  # Don't worry about full-match - widths are same
                successes.append(line)
        horizontal_possibilities.append(successes)

    print(horizontal_possibilities)

    vertical_patterns = [re.compile(pattern) for pattern in vertical_patterns]
    for horizontal_choices in itertools.product(*horizontal_possibilities):
        success = True
        for vert_line, vert_pattern in zip(map(''.join, zip(*horizontal_choices)), vertical_patterns):
            if not vert_pattern.match(vert_line):
                success = False
        if success:
            yield horizontal_choices



def test_regex_crossword_solve():
    horiz = [r'^HE|LL|O+$', r'^[PLEASE]+$']
    vert = [r'^[^SPEAK]+$', r'^EP|IP|EF$']
    for solution in regex_crossword_solve(horiz, vert, 2, 2):
        print(solution)


# def multidirectional(horizontal_patterns, vertical_patterns, width, height, alphabet=string.ascii_uppercase):
#     """As a super challenge, we don't implement the solution to this."""

def tabulate(f, start=0, step=1):
    return map(f, itertools.count(start, step))


test_regex_crossword_check()
test_regex_crossword_solve()
