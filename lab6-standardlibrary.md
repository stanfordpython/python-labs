# Lab 6: Standard Library

## Overview

The goal of this lab is to familiarize yourself with the tools of the standard library. We want you to gain practice with the common utilities of the standard library, and be aware of the rest of the tools, in case you ever need them.

We expect you to spend most of the time in this lab reading over the modules in the standard library that you find intriguing or applicable to your interests. If you have any questions about any standard library features, please ask us!

## Read

We get it. Reading documentation doesn't sound like a fun way to spend an afternoon. However, this is one of a rare few times when you will have dedicated class time to take a deep dive into a library tool. Python's standard library is huge, and your interests may not span all of it. However, I would bet that you can find something you enjoy in the library.

Remember that you can follow along with the documentation's examples in the interactive interpreter - we recommend this approach, so that you're both reading about and using the modules you like.

Several of the documentation pages have links to the source code - if you're interested in seeing examples of well-crafted Python modules, there's no better place to look than the standard library!

Ask questions! You should spend at least half of lab time reading over the standard library.

If you don't know which modules to look at, we've put together a list of some of our favorite modules that *weren't* covered in lecture, based on some common general interests. Come talk to us about what you'd like to learn more about, and we'll point in the right general direction.

### [Standard Library - Click Me!](https://docs.python.org/3.4/library/)

## Write

In this section, you'll practice using some of the more common modules in the Python standard library.

### Using `sys` for command-line tools.

#### Addition

Write a Python script `add.py` that can be run on the command line with any number of additional arguments representing numbers that you want to add up. Your script should print their sum! If there are arguments that can't be converted to floats, ignore them. If there are no additional arguments to your script, you should print an error message and exit.

Recall you can use `sys.argv` to access the command-line arguments.

```
$ python3 add.py 4 1
Sum: 5.0
$ python3 add.py 17 38 "Hey wassup" "hello"
55.0
$ python3 add.py 8 6 7 5 3 0 9
38.0
$ python3 add.py
Usage: python3 add.py <nums>
	
	Add some numbers together
```

#### `tree` (challenge)

Write a program that emulates the command-line utility `tree`, which pretty-prints the directory structure rooted by an argument name. If there is no argument, use the current working directory. For example,

```
$ python3 tree.py python-labs/
python-labs/
├── LICENSE
├── README.md
├── archive
│   └── aut15
│       ├── lab1-gettingstarted.md
│       ├── lab2-datastructures.md
│       ├── lab3-functions.md
│       ├── lab4-functionalprogramming.md
│       ├── lab5-classes.md
│       └── lab6-wallscraper.md
├── ideas.md
├── lab1-warmup.md
├── lab2-datastructures.md
├── lab3-functions.md
├── lab4-fp.md
├── lab5-oop.md
├── lab6-standardlibrary.md
└── solutions
    ├── lab2solutions.py
    ├── lab3solutions.py
    ├── lab4solutions.py
    ├── lab5solutions.py
    └── lab6solutions.py
```

The above is just an example - don't worry if your actual `python-labs/` directory doesn't look like this.

Use the `pathlib` library for filesystem navigation. For implementation details, check out `tree`'s [man page](http://linux.die.net/man/1/tree) or this [more helpful description](http://www.computerhope.com/unix/tree.htm). You don't need to implement any command-line flags for this part.

#### Improving `tree` (challenge)

Update your `tree` program to handle more advanced use cases, listed in the man page above. Can you handle symbolic links, maximum depth recursion, or pattern matching?

You can make this tool as powerful as you'd like.

### Extracting data with `re`

If you're new to regular expressions, we recommend you read through [the official Python HOWTO](https://docs.python.org/3.4/howto/regex.html)

Otherwise, read through the official [`re` documentation](https://docs.python.org/3.4/library/re.html) in its entirety.

#### Wordplay

Using the list of words found at `/usr/share/dict/words`, or alternatively `http://stanfordpython.com/words` if you're running Windows, determine all words that have the five vowels in order. That is, words that contain an `'a'`, `'e'`, `'i'`, `'o'`, and `'u'` in order.

#### Regex Crossword Checker

In the spirit of [Regex Crossword](https://regexcrossword.com/) (a highly entertaining site, if you've got hours to spare), write a function that checks arbitrary regex crosswords. Your function should take in two lists, one representing horizontal clues and one representing vertical clues, two integers representing the width and height of the crossword, as well as the potential solution to crossword in the form a list-of-lists in row-major order (i.e. the elements are lists representing rows of the crossword. Return true if and only if the potential solution is in fact valid.

```
import string
def regex_crossword_check(horizontal_patterns, vertical_patterns, width, height, candidate, alphabet=string.ascii_uppercase):
    pass  # Your implementation here
```

For example, the call corresponding to the first "Beginner" puzzle (it's called "Beatles") would look like:

```
horiz = [r'HE|LL|O+', r'[PLEASE]+']
vert = [r'[^SPEAK]+', r'EP|IP|EF']
candidate = [
	['H', 'E'],
	['L', 'P']
]
regex_crossword_check(horiz, vert, candidate)  # => True
```

and the call corresponding to the second "Experiences" puzzle (it's called "Royal Dinner") would look like:

```
horiz = [r'(Y|F)(.)\2[DAF]\1', r'(U|O|I)*T[FRO]+', r'[KANE]*[GIN]*']
vert = [r'(FI|A)+', r'(YE|OT)K', r'(.)[IF]+', r'[NODE]+', r'(FY|F|RG)+']
candidate = [
	['F', 'O', 'O', 'D', 'F'],
	['I', 'T', 'F', 'O', 'R'],
	['A', 'K', 'I', 'N', 'G']
]
regex_crossword_check(horiz, vert, candidate)  # => True
```

Some implementation notes:

* Make sure you're using `re.match` instead of `re.search`. The former matches an pattern string against an entire piece of text, whereas the latter checks to see if the pattern matches any substring of the text.
* You can get the width and height of the cr2ossword from the length of the vertical and horizontal clue lists, respectively.
* Remember your friend, `zip`!


#### Regex Crossword Solver (challenge)

Write a function to solve arbitrary regular expression crosswords.

Your function should take in two lists, one representing horizontal clues and one representing vertical clues, two integers representing the width and height of the crossword, as well as a keyword argument representing the possible alphabet. Return the characters read in row-major order (consistent with the site).

```
import re
import string
def regex_crossword_solve(horizontal_patterns, vertical_patterns, width, height, alphabet=string.ascii_uppercase):
    pass
```

For example, the call corresponding to the first "Beginner" puzzle (it's called "Beatles") would look like:

```
horiz = [r'HE|LL|O+', r'[PLEASE]+']
vert = [r'[^SPEAK]+', r'EP|IP|EF']
regex_crossword_solve(horiz, vert)
```

and would return the final answer `['HELP']` derived from the (unique, in this case) solution `[['H', 'E'], ['L', 'P']]`. If there are multiple answers, return them all.

#### Multidirectional (super challenge)

If you look though the Regex Crossword site linked above, you'll see that some puzzles (starting from "Double Cross" onwards), support multiple directions. Update your function above to work first with bidirection clues (as in "Double Cross", "Cities", "Volapük", and "Hamlet"). If that's too easy, see if you can solve the types of puzzles shown in "Hexagonal."

#### Minimal Regex (challenge)

Given a finite set of positive samples and a finite set of negative examples, can we build a regular expression that matches the positives but rejects the negatives? Of course! We can just explicitly include the positives and explicitly reject the negatives. However, this approach leads to regexes that are quite long. For this part, write an algorithm that approximately generates the smallest regular expression that matches a list of positive samples and rejects a list of negative samples. Our metric for smallest will default to shortest, but feel free to come up with your own metric.

```
def minimal_regex(positives, negatives):
    pass
```

*Note: this problem is NP-hard, and is tied to some deep results in complexity theory. For more information, check out [this CSTheory.SE post](http://cstheory.stackexchange.com/questions/1854/is-finding-the-minimum-regular-expression-an-np-complete-problem)

### Manipulating `collections`

**Before continuing, make sure you read the [`collections` documentation](https://docs.python.org/3.4/library/collections.html) in its entirety.**

Use `collections.namedtuple` and `collections.defaultdict` to implement an Employee database. You should read in a file of

```
employee_name employee_manager salary department title
employee_name employee_manager salary department title
...
employee_name employee_manager salary department title
```

and answer queries about all employees in a given department, with a given title, underneath a given manager, etc. You can also answer any other graph-related queries you'd like.

The primary part of this component is parsing the file and storing the employees in a data structure keyed by some of that employee's information.

### Working with `itertools`

**Before continuing, make sure you read the [`itertools` documentation](https://docs.python.org/3.4/library/itertools.html) in its entirety.**

#### Tabulation

Write a `tabulate` function to generate a computation lookup table. `tabulate` should takes in three arguments, a function, a start number, and a step size (the latter two default to 0).

```
def tabulate(f, start=0, step=0):
	pass
```

This function can be used as follows:

```
sqgen = tabulate(lambda x: x ** 2)
next(sqgen)  # => 0
next(sqgen)  # => 1
next(sqgen)  # => 2
next(sqgen)  # => 4
next(sqgen)  # => 9
```

For reference, our solution has one line and 32 characters.

### All Together

This final challenge will incorporate all of the modules we've seen so far. We'll build a tool to determine the shortest airport journey between any two airports.

First, the data:

* [Airlines](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat)
* [Airports](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat)
* [Routes](https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat)

For information about the data itself, [DataHub](https://datahub.io/dataset/open-flights) has a good writeup.

Write a script that, when given two airport codes (like SFO and JFK) and a maximum segment count, prints all possible ways to get from the source airport to the destination airport in at most that many segments. For example,

```
$ python3 flights.py SFO JFK
SFO -> JFK (nonstop)
SFO -> ORD -> JFK (1 stop)
...
```

> With <3 by @sredmond