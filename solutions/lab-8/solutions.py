#!/usr/bin/env python3
"""
File: lab-8.py
--------------

Solutions for CS 41 Lab 8.

Authors:
    Parth Sarin
    Sam Redmond
"""
import numpy as np
import re
import collections
import string
import itertools

DICTIONARY_FILENAME = '/usr/share/dict/words'


################################
# NETFLIX MOVIE RECOMMENDATION #
################################
def load_data():
    """
    Loads the movie data from `ratings.txt`.
    """
    """
    I don't particularly like hard-coding these values, but it's the most
    Pythonic way to do it given our problem. For robustness, you'd probably
    open `movies.txt` to extract the number of movies before you make this
    matrix.
    """
    out = np.zeros((671, 9125))

    with open('ratings.txt', 'r') as f:
        for line in f:
            user_id, movie_id, rating = line.strip().split('%')
            out[int(user_id), int(movie_id)] = float(rating)


    return out


def clean_data(ratings):
    """
    Cleans the data by normalizing each axis.

    Arguments
    ---------
    ratings (np.ndarray [m x n]) -- The matrix to normalize.

    Returns
    -------
    np.ndarray [m x n] -- The input matrix, with its columns normalized
    """
    norms = np.linalg.norm(ratings, axis=0)
    # To avoid division by zero:
    norms = np.array([v if v != 0 else 1 for v in norms])
    return ratings / norms


def suggest_movies(user_ratings, normalized_ratings, n=5):
    """
    Returns the top five movie suggestions for the user, given their ratings
    of other movies.

    Arguments
    ---------
    user_ratings (np.ndarray) -- A numpy array representing the user's ratings
        of the movies.

    normalized_ratings (np.ndarray) -- A numpy array representing all of the
        rating data for movies that we have.

    n (int) -- The number of recommended movies to return.

    Returns
    -------
    np.ndarray [n] -- The indices of the recommended movies for this user.
    """
    """
    Compute the movie_profile by multiplying user_ratings with the matrix,
    summing, and then normalizing.
    """
    movie_profile = np.sum(normalized_ratings * user_ratings, axis=1)
    movie_profile /= np.linalg.norm(movie_profile)

    """
    The scores are obtained using numpy broadcasting, and by transposing the
    normalized_ratings matrix.
    """
    scores = np.sum(normalized_ratings.T * movie_profile, axis=1)

    """
    Sort the scores and return the top n!
    """
    return np.argsort(scores)[-n:][::-1]


def run_recommendation():
    """
    Runs the recommendation algorithm on Parth's favorite movies.
    """
    parth_ratings = {
        8911: 5, # Inside Out
        8460: 4, # Frozen 1
        6294: 5  # Harry Potter and the Goblet of Fire
    }

    ratings = load_data()
    normalized_ratings = clean_data(ratings)
    
    full_parth_ratings = np.array([
        parth_ratings.get(i, 0) for i in range(ratings.shape[1])
    ])

    print(suggest_movies(full_parth_ratings, normalized_ratings))
    # [8911, 6294, 8460, 5399, 8434]


######################
# STANDARD LIBRARIES #
######################
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


def license_plate_words(letters):
    re_pattern = r'.*' + r'.*'.join(letters.lower()) + r'.*'
    print(re_pattern)
    with open(DICTIONARY_FILENAME, 'r') as f:
        for line in f:
            if not re.match(re_pattern, line.lower().strip()):
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
    run_recommendation()
    # print(most_common_words())
    # license_plate_words('btp')
    # test_largest_families()
    # test_regex_crossword_check()
    # test_regex_crossword_solve()