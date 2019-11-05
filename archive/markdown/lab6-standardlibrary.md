# Lab 6: Standard Library

## Overview

The goal of this lab is to familiarize yourself with the tools of the standard library. We want you to gain practice with the common utilities of the standard library, and be aware of the rest of the tools, in case you ever need them.

**We expect you to spend most of the time in this lab reading over the modules in the standard library that you find intriguing or applicable to your interests.** If you have any questions about any standard library features, please ask us!

## Read

We get it. Reading documentation doesn't sound like a fun way to spend an afternoon. However, this is one of a rare few times when you will have dedicated class time to take a deep dive into a library tool. Python's standard library is huge, and your interests may not span all of it. However, I would bet that you can find something you enjoy in the library.

Remember that you can follow along with the documentation's examples in the interactive interpreter - we recommend this approach, so that you're both reading about and using the modules you like.

Several of the documentation pages have links to the source code - if you're interested in seeing examples of well-crafted Python modules, there's no better place to look than the standard library!

Ask questions! You should spend at least half of lab time reading over the standard library.

If you don't know which modules to look at, we've put together a list of some of our favorite modules that *weren't* covered in lecture, based on some common general interests. Come talk to us about what you'd like to learn more about, and we'll point in the right general direction.

### [Standard Library - Click Me!](https://docs.python.org/3.4/library/)

## Write

In this section, you'll practice using some of the more common modules in the Python standard library.

### Manipulating `collections`

**Before continuing, make sure you have read the [`collections` documentation](https://docs.python.org/3.4/library/collections.html) through 8.3.6.1.**

##### Mechanics

**`collections.namedtuple`**

Rewrite the following code to be more Pythonic. Use `collections.namedtuple` to add readable attribute references.

```
lassie = ('Lassie', 'dog', 'black', 12)
astro = ('Astro', 'dog', 'grey', 15)
mrpb = ('Mr. Peanutbutter', 'dog', 'golden', 35)
bojack = ('BoJack Horseman', 'horse', 'brown', 52)
pc = ('Princess Carolyn', 'cat', 'pink', 34)
tinkles = ('Mr. Tinkles', 'cat', 'white', 7)
pupper = ('Bella', 'pupper', 'brown', 0.5)
doggo = ('Max', 'doggo', 'brown', 5)
seuss = ('The Cat in the Hat', 'cat', 'stripey', 27)
pluto = ('Pluto (Disney)', 'dog', 'orange', 3)
yertle = ('Yertle', 'turtle', 'green', 130)

for animal in [lassie, astro, mrpb, bojack, pc, tinkles, pupper, doggo, seuss, pluto, yertle]:
    if animal[1] == 'dog' or animal[1] == 'doggo' or animal[1] == 'pupper':
        if animal[3] > 5:
            print(animal[0] + ' is an old ' + animal[2] + ' ' + animal[1] + ' who is ' + str(animal[3]) + ' years old.')
        else:
            print(animal[0] + ' is a young ' + animal[2] + ' ' + animal[1] + ' who is ' + str(animal[3]) + ' years old.')
    else:
        print(animal[0] + ' is a non-canine ' + animal[2] + ' ' + animal[1] + '.')
```

#### `collections.defaultdict` and `collections.Counter`

Using `/usr/share/dict/words` (alternatively, `http://stanfordpython.com/res/misc/words`) as a data source, what are the three most common word lengths in the English language? Remember to strip off trailing whitespace.

##### Evil Hangman Redux (optional)

Feel free to skip this section if you aren't familiar with Keith's CS106B/L assignment: "Evil Hangman."

Suppose you are provided with the function `mask(word, letter)` which replaces each character in `word` with a dash if that character is different than `letter` - for example, `mask('banana', 'a')  # => '-a-a-a'`.

```
def mask(word, letter):
    return ''.join('-' if letter != ch else letter for ch in word)
```

Write a function called

```
def largest_families(words, letter, num_families):
    pass
```
which returns the top `num_families` largest collections of words which share a mask, given a source collection of words and a chosen letter. Specifically, given a chosen letter, a family of words is one in which every word yields the same mask when applied with that letter. For example, if the chosen letter is `'s'`, then `'sees'`, and `'says'` would be in the same family (`'s--s'`), but `'sass'` would be in a different family (`'s-ss'`).

#### Working Together

Use tools from the `collections` module to implement an `Employee` database. You should read in a file of

```
employee_name    employee_manager    salary    department    title
employee_name    employee_manager    salary    department    title
...
employee_name    employee_manager    salary    department    title
```

If you'd like sample data to work with, you can use the following
```
sredmond	poohbear	41	CS	Instructor
poohbear	sahami	500	CS	Lecturer
tigger	poohbear	500	CS	Tiger
htiek	sahami	500	CS	Lecturer
sahami	mtl	5000	CS	Professor
guido	guido	50000	PSF	BDFL
```
You can assume that lines in the file are tab-separated. If you're saving the above text to a file, make sure that your text editor didn't automatically replace tabs with spaces!

You should implement the following functions:

```
def directly_reports_to(employee, manager):
    """Return whether or not employee directly reports to manager"""
    pass

def indirectly_reports_to(employee, manager):
    """Return whether or not employee indirectly reports to manager"""
    pass
    
def in_department(dept):
    """Return a collection of all employees of a given department"""
    pass
    
def cost_of(dept):
    """Return the sum total of salaries for all employees of a given department""""
    pass
```

The primary portion of this section is parsing the file and storing the employees in a your choice of data structure keyed by some of the employees' information.

### Extracting data with `re`

If you're new to regular expressions, we recommend you read through [the official Python HOWTO](https://docs.python.org/3.4/howto/regex.html)

Otherwise, **read through the official [`re` documentation](https://docs.python.org/3.4/library/re.html) through 6.2.4** (although 6.2.5 is neat).

#### Wordplay

Using the list of words found at `/usr/share/dict/words`, or alternatively `http://stanfordpython.com/res/misc/words` if you're running Windows, determine all words that have the five vowels in order. That is, words that contain an `'a'`, `'e'`, `'i'`, `'o'`, and `'u'` in order, with any number (including 0) of word characters before the 'a', between the vowels, and after the 'u'.

#### Regex Crossword Checker

Take a moment to play one round of [Regex Crossword](https://regexcrossword.com/) (a highly entertaining site, if you've got hours to spare).

In the spirit of Regex Crossword, write a function that checks arbitrary regex crosswords. Your function should take in two lists, one representing horizontal clues and one representing vertical clues, as well as the potential solution to crossword in the form a list-of-lists in row-major order (i.e. the elements are lists representing rows of the crossword. Return whether or not the potential solution is in fact valid.

```
import string
def regex_crossword_check(horizontal_patterns, vertical_patterns, candidate):
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

* You may want to use `re.fullmatch` instead of `re.match` or `re.search`. The former matches a pattern string against an entire string, whereas the latter methods check to see if any prefix string or any substring, respectively, match the pattern.
* You can get the width and height of the crossword from the length of the vertical and horizontal clue lists, respectively.
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
regex_crossword_solve(horiz, vert, 2, 2)
```

and would return the final answer `['HELP']` derived from the (unique, in this case) solution `[['H', 'E'], ['L', 'P']]`. If there are multiple answers, return them all.

#### Multidirectional (super challenge)

If you look though the Regex Crossword site linked above, you'll see that some puzzles (starting from "Double Cross" onwards), support multiple directions. Update your function above to work first with bidirection clues (as in "Double Cross", "Cities", "Volapük", and "Hamlet"). If that's too easy, see if you can solve the types of puzzles shown in "Hexagonal."

#### Minimal Regex (super challenge)

Given a finite set of positive samples and a finite set of negative examples, can we build a regular expression that matches the positives but rejects the negatives? Of course! We can just explicitly include the positives and explicitly reject the negatives. However, this approach leads to regexes that are quite long. For this part, write an algorithm that approximately generates the smallest regular expression that matches a list of positive samples and rejects a list of negative samples. Our metric for smallest will default to shortest, but feel free to come up with your own metric.

```
def minimal_regex(positives, negatives):
    pass
```

*Note: this problem is NP-hard, and is tied to some deep results in complexity theory. For more information, check out [this CSTheory.SE post](http://cstheory.stackexchange.com/questions/1854/is-finding-the-minimum-regular-expression-an-np-complete-problem)*

### Working with `itertools`

**Before continuing, make sure you read the [`itertools` documentation](https://docs.python.org/3.4/library/itertools.html) through 10.1.1** (although 10.1.2 is neat).

#### Tabulation

Write a `tabulate` function to generate a computation lookup table. `tabulate` should takes in three arguments, a function, a start number (default 0), and a step size (default 1)

```
def tabulate(f, start=0, step=1):
	pass
```

This function can be used as follows:

```
sqgen = tabulate(lambda x: x ** 2)
next(sqgen)  # => 0 = f(0)
next(sqgen)  # => 1 = f(1)
next(sqgen)  # => 4 = f(2)
next(sqgen)  # => 9 = f(3)
```

For reference, our implmentation is one line and 43 characters.

Hint: take a look at the `itertools.count` function!

### JSON

**Before continuing, make sure you read the [`json` documentation](https://docs.python.org/3.4/library/json.html) through 19.2.1.**

Think of a broad topic you're interested in. Then, spend a few minutes trying to find a JSON file on the internet related to your interest.

### `random`

**Before continuing, make sure you read the [`random` documentation](https://docs.python.org/3.4/library/random.html) through 19.2.1.**

There's no code in this section - just read the documentation! It's rather short.

### Using `sys` for command-line tools.

#### Addition

Write a Python script `add.py` that can be run on the command line with any number of additional arguments representing numbers that you want to add up. Your script should print their sum! If there are arguments that can't be converted to floats, ignore them. If there are no additional arguments to your script, you should print an error message and exit.

Recall you can use `sys.argv` to access the command-line arguments.

```
$ python3 add.py 4 1
5.0
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

#### Improving `tree` (super challenge)

Update your `tree` program to handle more advanced use cases, listed in the man page above. Can you handle symbolic links, maximum depth recursion, or pattern matching?

You can make this tool as powerful as you'd like.

### All Together

This final problem will incorporate all of the modules we've seen so far. We'll build a tool to determine the shortest airport journey between any two airports.

First, the data:

* [Airlines](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat)
* [Airports](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat)
* [Routes](https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat)

For information about the data itself, [DataHub](https://datahub.io/dataset/open-flights) has a good writeup.

The information [here](https://openflights.org/data.html) is also quite good.

Write a script that, when given two airport codes (like SFO and JFK) and a maximum segment count, prints all possible ways to get from the source airport to the destination airport in at most that many segments. For example,

```
$ python3 flights.py SFO JFK 2
SFO -> JFK
SFO -> LAX -> JFK
SFO -> ORD -> JFK
SFO -> DFW -> JFK
...
SFO -> PDX -> JFK
```

> With <3 by @sredmond
