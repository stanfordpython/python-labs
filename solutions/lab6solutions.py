#!/usr/bin/env python3 -tt
"""
File: lab6solutions.py
----------------------
Incomplete solutions to Lab 6 for CS41: Hap.py Code.

Honestly, there wasn't much code for this lab, so this file is relatively small.

Revision history:
@sredmond 05-02-2016 Created
"""
import re
import collections
import string
import itertools


def regex_crossword_check(horizontal_patterns, vertical_patterns, candidate, alphabet=string.ascii_uppercase):
    # Check horizontal clues
    for pattern, horiz_line in zip(horizontal_patterns, candidate):
        line = ''.join(horiz_line)
        if re.match(pattern, line) is None:
            return False

    # Check vertical clues
    for pattern, vert_line in zip(vertical_patterns, zip(*candidate)):
        line = ''.join(vert_line)
        if re.match(pattern, line) is None:
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
    # Possible widths
    for letters in itertools:
        pass

def tabulate(f):
    return map(f, count())


test_regex_crossword_check()
