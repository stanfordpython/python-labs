#!/usr/bin/env python3 -tt
"""
File: lab3solutions.py
----------------------
Reference solutions to Lab 3 for CS41: Hap.py Code.

This lab incorporated a lot of exploration, so there's less
"code" per se.

These solutions are still a work in progress! More to come.

Revision history:
@sredmond 04-16-2016 Adds comments
@sredmond 04-12-2016 Created
"""

def print_two(a, b):
    """

    INVALID print_two()
      VALID print_two(4, 1)
    print_two(41)
    print_two(a=4, 1)
    print_two(4, a=1)
    print_two(4, 1, 1)
    print_two(b=4, 1)
    print_two(a=4, b=1)
    print_two(b=1, a=4)
    print_two(1, a=1)
    print_two(4, 1, b=1)
    """
    print("Arguments: {0} and {1}".format(a, b))



def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)


def speak_excitedly(message, num_exclamations=1, enthusiasm=False):
    message += '!' * num_exclamations
    if not enthusiasm:
        return message
    return message.upper()

def test_speak_excitedly():
    """ Sample function calls illustrating the `speak_excitedly` function. """
    # "I love Python!"
    print(speak_excitedly("I love Python"))

    # "Keyword arguments are great!!!!"
    print(speak_excitedly("Keyword arguments are great", num_exclamations=4))

    # "I guess Java is okay..."
    print(speak_excitedly("I guess Java is okay...", num_exclamations=0))

    # "LET'S GO STANFORD!!"
    print(speak_excitedly("Let's go Stanford", num_exclamations=2, enthusiasm=True))

def average(*nums):
    if not nums: return None
    return sum(nums) / len(nums)

def test_average():
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    avg = average(*nums)
    print("Average of first 10 primes is {}".format(avg))

def make_table(key_justify='left', value_justify='right', **kwargs):

    # Map from human-readable justifications to .format alignment specifiers
    justification = {
        'left': '<',
        'right': '>',
        'center': '^'
    }
    if key_justify not in justification or value_justify not in justification:
        print("Error! Invalid justification specifier.")
        return None

    key_alignment_specifier = justification[key_justify]
    value_alignment_specifier = justification[value_justify]

    max_key_length = max(map(len, kwargs.keys()))
    max_value_length = max(map(len, kwargs.values()))

    total_length = 2 + max_key_length + 3 + max_value_length + 2
    print('=' * total_length)
    for key, value in kwargs.items():
        print('| {:{key_align}{key_pad}} | {:{value_align}{value_pad}} |'.format(key, value,
            key_align=key_alignment_specifier, key_pad=max_key_length,
            value_align=value_alignment_specifier, value_pad=max_value_length
        ))
    print('=' * total_length)

def test_make_table():
    make_table(
        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink"
    )

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


###################
# DATA STRUCTURES #
###################


def function_objects():
    """

    """

if __name__ == '__main__':
    test_speak_excitedly()
    test_average()
    test_make_table()
