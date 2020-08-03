# Lab 2: Welcome to Python + Data Structures

## Overview

Welcome to your first lab! Labs in CS41 are designed to be your opportunity to experiment with Python and gain hands-on experience with the language.

The primary goal of the first half is to ensure that your Python installation process went smoothly, and that there are no lingering Python installation bugs floating around.

The second half focuses more on using data structures to solve some interesting problems.

You're welcome to work in groups or individually. Remember to have some fun! Make friends and maybe relax a little too. If you want to cue up any songs to the CS41 playlist, let us know or add them yourself at [this link](https://open.spotify.com/playlist/1pn8cUoKsLlOfX7WEEARz4?si=jKogUQTsSDmqu6RbSBGfGA)!

**Note: These labs are *designed* to be long! You shouldn't be able to finish all the problems in one class period. Work through as much as you can in the time allotted, but also feel free to skip from question to question freely. Part II is intended to be extra practice, if you want to hone your Python skills even more.**

Above all, have fun playing with Python! Enjoy.

### Running this lab

In this lab, you should make changes to `data-structures.py`! We've provided a file called `harness.py` which will allow you to run the functions in `data-structures.py` individually.

Execute `python3 harness.py` to open up our coding harness and select specific functions to run from the data structures file.

## Hello World

Edit `say_hello` so that it prints `"Hello, world!"` when executed.

## Warmup Problems! 🦄

### Fizz, Buzz, FizzBuzz!
If we list all of the natural numbers under 41 that are a multiple of 3 or 5, we get

```
 3,  5,  6,  9, 10, 12, 15,
18, 20, 21, 24, 25, 27, 30,
33, 35, 36, 39, 40
```

The sum of these numbers is 408.

Edit `fizzbuzz(n)` to find the sum of all the multiples of 3 or 5 below 1001. As a sanity check, the last two digits of the sum should be `68`.

### Collatz Sequence
Depending on from whom you took CS106A, you may have seen this problem before.

The *Collatz sequence* is an iterative sequence defined on the positive integers by:

```
n -> n / 2    if n is even
n -> 3n + 1   if n is odd
```

For example, using the rule above and starting with 13 yields the sequence:

```
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
```

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although unproven, it it hypothesized that all starting numbers finish at 1.

Edit `max_collatz_len(n)` so that it computes the the length of the longest chain which has a starting number under `n` and use it to find the longest chain that has a starting number under 1000.

**Challenge**: Same question, but for any starting number under 1,000,000. What about for any starting number under 10,000,000? You may need to implement a cleverer-than-naive algorithm.

<details>
    <summary><b>Hints</b> (click to expand):</summary>
    <ol>
        <li>You can implement <code>collatz_len</code> really elegantly using recursion, but you don't need that! You can also use a <code>while</code> loop.</li>
        <li>(for the challenge) You don't need to do any complicated math to get the cleverer-than-naive algorithm! Just try to improve efficiency when your code encounters a Collatz sequence that it's already encountered.</li>
    </ol>
</details>

*NOTE: Once the chain starts the terms are allowed to go above one thousand.*

### Zen Printing

Implement `print_tictactoe` using `print()` so that, when run, it prints out a tic-tac-toe board.

```
 X | . | . 
-----------
 . | O | . 
-----------
 . | O | X 
```

You may find the optional arguments to `print()` useful, which you can read about [here](https://docs.python.org/3/library/functions.html#print). In no more than five minutes, try to use these optional arguments to print out this particular tic-tac-toe board.

Maybe you were able to print out the tic-tac-toe board. Maybe not. In the five minutes you've been working on that, I've gotten bored with normal tic-tac-toe (too many ties!) so now, I want to play SUPER tic-tac-toe.

Write a program that prints out a SUPER tic-tac-toe board.

```
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
  |  |  H  |  |  H  |  |  
```

You'll find that there might be many ways to solve this problem. Which do you think is the most 'pythonic?' Talk to someone next to you about your approach to this problem. Remember the Zen of Python!

**Hint:** To find the most Pythonic way to do this, think about what you'd do if I said you have 10 seconds to write code that prints out the list.

## Data Structures, whooo!
If you've gotten this far, you're already above and beyond! Our recommendation at this point is to pick out the most interesting of the following problems and solve those!

[Optional Reading on Standard Types - check out Sequence types and Mapping types](https://docs.python.org/3/library/stdtypes.html)

### Comprehensions
#### Read

Predict the output of each of the following list comprehensions. After you have written down your hypothesis, uncomment the appropriate line in `comprehension_read` and run it. If you were incorrect, discuss with a partner why Python returns what it does.

```Python
[x for x in [1, 2, 3, 4]]
[n - 2 for n in range(10)]
[k % 10 for k in range(41) if k % 3 == 0]
[s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]]

# Something is fishy here. Can you spot it?
arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
print([el.append(el[0] * 4) for el in arr])  # What is printed?
print(arr)  # What is the content of `arr` at this point?

[letter for letter in "pYthON" if letter.isupper()]
{len(w) for w in ["its", "the", "remix", "to", "ignition"]}
```

#### Write

Write comprehensions in `comprehension_write` to transform the input data structure into the output data structure:

```python
[0, 1, 2, 3] -> [1, 3, 5, 7]  # Double and add one
['apple', 'orange', 'pear'] -> ['A', 'O', 'P']  # Capitalize first letter
['apple', 'orange', 'pear'] -> ['apple', 'pear']  # Contains a 'p'

["TA_parth", "student_poohbear", "TA_michael", "TA_guido", "student_htiek"] -> ["parth", "michael", "guido"]
['apple', 'orange', 'pear'] -> [('apple', 5), ('orange', 6), ('pear', 4)]

['apple', 'orange', 'pear'] -> {'apple': 5, 'orange': 6, 'pear': 4}
```

### Tuples and Dicts: Caching
In this problem, we'll use tuples and dicts to memoize a recursive function.

*Note*: In general, we try to keep this class as self-contained as possible and don't ask that you know too much computer science outside of CS41. For this problem, though, you will use recursion. If you aren't super comfortable with recursion or caching, feel free to skip ahead!

This problem is called **lattice paths**. Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

![2x2 paths](https://projecteuler.net/project/images/p015.png)

Implement `lattice_paths(m, n)` to be a recursive function that, when run, calculates the number of paths from the top left of an $m \times n$ grid ($m$ rows and $n$ columns) to the bottom right corner.

Notice that the problem seems very similar to itself... At every point in the grid, you only have two moves: down and left.

<details>
    <summary><b>Hints</b> (click to expand):</summary>
    <ol>
        <li>The recursive base case is a grid where <i>either</i> the number of rows is zero or the number of columns is zero. How many paths are there in this case? Notice that programming it this way also prevents $m$ or $n$ from being negative.</li>
        <li>Suppose you move down. Then, the remaining problem is <i>still</i> to count the number of paths from the top left of a grid to the bottom right, but now the grid is a different size.</li>
        <li>If you move down, the problem becomes counting the number of paths from the top left of a grid of size $(m-1) \times n$ to the bottom right of that grid.</li>
    </ol>
</details>

Notice that the way that our code is constructed results in a lot of repeated calls to the same functions. For example, if you start at the top of a $20 \times 20$ grid and go down, then right, you'll make a function call for a $19 \times 19$ grid. But you'll also make that call if you go right and *then* down. This is where caching comes in. We'll store the output of `lattice_paths` in a dictionary the first time that we call it and then the second time, we'll just immediately return the value from the dictionary so that we won't make calls twice.

In `lattice_paths_cached`, let's cache `lattice_paths` by adding its output to a dictionary. This dictionary should have keys that are tuples $(m,n)$ and values that are the output `lattice_paths(m,n)`. Make sure to check if the tuple `(m,n)` is in the cache dictionary at the beginning of the function execution.

### Lists
Predict what the following lines of Python will do. Then, run `object_reference` to see if they match what you expect:

```Python
s = [0] * 3
print(s)
s[0] += 1
print(s)

s = [''] * 3
print(s)
s[0] += 'a'
print(s)

s = [[]] * 3
print(s)
s[0] += [1]
print(s)
```

Why does this happen? Talk with your neighbor.

### Tuples

Write a function to compute the [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) of two positive integers. You can freely use the fact that `gcd(a, b)` is mathematically equal to `gcd(b, a % b)`, and that `gcd(a, 0) == a`.

You can assume that `a >= b` if you'd like.

It is possible to accomplish this in three lines of Python code (or with extra cleverness, even fewer!). Consider exploiting tuple packing and unpacking!

Implement your solution in the `gcd` function.

*Note: The standard library has a `gcd` function. Avoid simply importing that function and using it here - the goal is to practice with tuple packing and unpacking!*

### Flipping Dictionaries
I asked our course staff what their favorite animal is and they gave me these answers:
```python
fav_animals = {
    'parth': 'unicorn',
    'michael': 'elephant',
    'sam': 'ox',
    'zheng': 'tree',
    'theo': 'puppy',
    'alex': 'dog',
    'nick': 'daisy'
}
```

I know that, realistically, they're lying to themselves. In fact, the dict probably looks more like this:
```python
fav_animals = {
    'parth': 'unicorn',
    'michael': 'unicorn',
    'sam': 'unicorn',
    'zheng': 'tree',
    'theo': 'unicorn',
    'alex': 'dog',
    'nick': 'daisy'
}
```

In this problem, we'll reverse the `fav_animals` dictionary to create a new dictionary which associates animals to a list of people for whom that animal is their favorite. 

More precisely, write a function that properly reverses the keys and values of a dictionary - each key (originally a value) should map to a collection of values (originally keys) that mapped to it. For example,

```python
flip_dict({"CA": "US", "NY": "US", "ON": "CA"})
# => {"US": ["CA", "NY"], "CA": ["ON"]}
```

Note: there is a data structure in the `collections` module from the standard library called `defaultdict` which provides exactly this sort of functionality. You provide it a factory method for creating default values in the dictionary (in this case, a list.) You can read more about `defaultdict` and other `collections` data structures [here](https://docs.python.org/3/library/collections.html).

# Bonus Problems
Don't worry about doing these bonus problems. In most cases, bonus questions ask you to think more critically or use more advanced algorithms.

In this case, we'll use list comprehensions to solve some interesting problems.

### Pascal's Triangle
Write a function that generates the next level of [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) given a list that represents a row of Pascal’s triangle.

```
generate_pascal_row([1, 2, 1]) -> [1, 3, 3, 1]
generate_pascal_row([1, 4, 6, 4, 1]) -> [1, 5, 10, 10, 5, 1]
generate_pascal_row([]) -> [1]
```

As a reminder, each element in a row of Pascal's triangle is formed by summing the two elements in the previous row directly above (to the left and right) that elements. If there is only one element directly above, we only add that one. For example, the first 5 rows of Pascal's triangle look like:

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

You could solve this problem with `enumerate` or look up the `zip` function for an even more Pythonic solution (use iPython, perhaps?)! Avoid using a loop of the form `for i in len(range(row)):`.

*Hint: Check out the diagram below. How could you use this insight to help complete this problem?*

```
  0 1 3 3 1
+ 1 3 3 1 0
-----------
  1 4 6 4 1
```

## Pretty Pascal
Implement `pretty_pascal_triangle` so that given a number `n`, it prints out the first `n` rows of Pascal's triangle, *centering* each line. You should use the `generate_pascal_row` function you wrote previously. The Pascal's triangle with 1 row just contains the number `1`.

To center a string in Python, you can use use string format specifiers. `'{:^10}'.format(var)` will produce a string of length 10 or `len(var)` (whichever is longer), with `str(var)` centered.

```python
'{:^10}'.format('CS41') # => '   CS41   '
```

You can even specify an optional `fillchar` to fill with characters other than spaces!

For example, for `n = 10`:
```python
print_pascal_triangle(10)
#              1             
#             1 1            
#            1 2 1           
#           1 3 3 1          
#          1 4 6 4 1         
#        1 5 10 10 5 1       
#      1 6 15 20 15 6 1      
#     1 7 21 35 35 21 7 1    
#   1 8 28 56 70 56 28 8 1   
# 1 9 36 84 126 126 84 36 9 1
```

## Special Phrases
For the next few problems, we'll describe a criterion that makes a word or phrase special (like the "Efficient Words" example from lecture) and ask you to write a function that determines whether the input fits that criterion.

Before that, though, we need to load up a list of all of the words in the English language to see which words fit the criterion.

If you are using macOS or Linux, you should have a dictionary file available at `/usr/share/dict/words`, a 2.5M text file containing over 200 thousand English words, one per line. However, we've also mirrored this file at `https://stanfordpython.com/res/misc/words`, so you can download the dictionary from there if your computer doesn't have this dictionary file readily available.

Write a function called `load_english` that loads the words from this file and returns them. What would be an appropriate data structure in which to store these words?

## Cyclone Phrases (challenge)

Cyclone words are English words that have a sequence of characters in alphabetical order when following a cyclic pattern. 

For example:

![Cyclone Phrases](http://i.stack.imgur.com/4XBV3.png)

Write the function `is_cyclone_phrase` to determine whether an entire phrase passed into a function is made of cyclone words. You can assume that all words are made of only alphabetic characters, and are separated by whitespace.

```
is_cyclone_phrase("adjourned") # => True
is_cyclone_phrase("settled") # => False
is_cyclone_phrase("all alone at noon") # => True
is_cyclone_phrase("by myself at twelve pm") # => False
is_cyclone_phrase("acb") # => True
is_cyclone_phrase("") # => True
```

Using the `load_english` function, write `all_cyclone_words` to generate a list of all cyclone words. How many are there? As a sanity check, we found 769 distinct cyclone words.

### Triad Phrases

Triad words are English words for which the two smaller strings you make by extracting alternating letters both form valid words.

For example:

![Triad Phrases](http://i.imgur.com/jGEXJWi.png)

Write the function `is_triad_phrase` to determine whether an entire phrase passed into a function is made of triad words. You can assume that all words are made of only alphabetic characters, and are separated by whitespace. We will consider the empty string to be an invalid English word.

```python
is_triad_phrase("learned theorem") # => True
is_triad_phrase("studied theories") # => False
is_triad_phrase("wooded agrarians") # => True
is_triad_phrase("forrested farmers") # => False
is_triad_phrase("schooled oriole") # => True
is_triad_phrase("educated small bird") # => False
is_triad_phrase("a") # => False
is_triad_phrase("") # => False
```

Write `all_triad_words` to generate a list of all triad words. How many are there? We found 2770 distinct triad words (case-insensitive).

### Surpassing Phrases (challenge)

Surpassing words are English words for which the gap between each adjacent pair of letters strictly increases. These gaps are computed without "wrapping around" from Z to A.

For example:

![Surpassing Phrases](http://i.imgur.com/XKiCnUc.png)

Write the function `is_surpassing_phrase(phrase)` to determine whether an entire phrase passed in is made of surpassing words. You can assume that all words are made of only alphabetic characters, and are separated by whitespace. We will consider the empty string and a 1-character string to be valid surpassing phrases.

```python
is_surpassing_phrase("superb subway") # => True
is_surpassing_phrase("excellent train") # => False
is_surpassing_phrase("porky hogs") # => True
is_surpassing_phrase("plump pigs") # => False
is_surpassing_phrase("turnip fields") # => True
is_surpassing_phrase("root vegetable lands") # => False
is_surpassing_phrase("a") # => True
is_surpassing_phrase("") # => True
```

We've provided a `character_gap` function that returns the gap between two characters. To understand how it works, you should first learn about the Python functions `ord` (one-character string to integer ordinal) and `chr` (integer ordinal to one-character string). For example:

```python
ord('a') # => 97
chr(97) # => 'a'
```

So, in order to find the gap between `G` and `E`, we compute `abs(ord('G') - ord('E'))`, where `abs` returns the absolute value of its argument.

Write `all_surpassing_words` to generate a list of all surpassing words. How many are there? We found 1931 distinct surpassing words.

### Triangle Words
The nth term of the sequence of triangle numbers is given by $1 + 2 + ... + n = \frac{n(n+1)}{2}$. For example, the first ten triangle numbers are: `1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...`

By converting each letter in a word to a number corresponding to its alphabetical position (`A=1`, `B=2`, etc) and adding these values we form a word value. For example, the word value for SKY is `19 + 11 + 25 = 55` and 55 is a triangle number. If the word value is a triangle number then we shall call the word a triangle word.

Write `all_triangle_words` to generate a list of all triangle words. How many are there? As a sanity check, we found 16303 distinct triangle words.

*Hint: you can use `ord(ch)` to get the integer ASCII value of a character. You can also use a dictionary to accomplish this!*

## Polygon Collision

Given two polygons in the form of lists of 2-tuples, determine whether the two polygons intersect.

Formally, a polygon is represented by a list of (x, y) tuples, where each (x, y) tuple is a vertex of the polygon. Edges are assumed to be between adjacent vertices in the list, and the last vertex is connected to the first. For example, the unit square would be represented by

```
square = [(0,0), (0,1), (1,1), (1,0)]
```

You can assume that the polygon described by the provided list of tuples is not self-intersecting, but do not assume that it is convex.

**Note: this is a *hard* problem. Quite hard.**

## Done Early?
Skim [Python’s Style Guide](https://www.python.org/dev/peps/pep-0008/), keeping the Zen of Python in mind. Feel free to skip portions of the style guide that cover material we haven't yet touched on in this class, but it's always good to start with an overview of good style.

*Credit to Sam Redmond, Puzzling.SE (specifically [JLee](https://puzzling.stackexchange.com/users/463/jlee)), ProjectEuler and InterviewCake for several problem ideas*

> With 🦄 by @psarin and @coopermj[]([]([]([]([]()))))