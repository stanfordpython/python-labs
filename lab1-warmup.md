# Lab 1: Welcome to Python!

## Goals
Welcome to your first lab day! Labs in CS41 are designed to be your opportunity to experiment with Python and gain hands-on experience with the language.

The primary goal of this lab is to ensure that your Python installation process went smoothly, and that there are no lingering Python 2/3 bugs floating around.

This lab also gives you the chance to write what might be your first programs in Python, and allows you to experiment with both scripts and with the interactive interpreter!

These problems are not intended to be algorithmically challenging - just ways to flex your new Python 3 muscles. Even if the problems seem simple, work through them quickly, and then you're free to go.

As always, have fun, and enjoy the (remainder of the) class period!

## Warming Up

### Hello World

If you haven’t already, write a Hello World program which consists of getting Python to print `"Hello, World!"` to the console. First, write this program using the interactive interpreter. Next, put the body of the program into a file named `hello.py`, and run the Hello World program as a Python script.

### Printing

Write a program using `print()` that, when run, prints out a tic-tac-toe board.

```
  |  |
--------
  |  |
--------
  |  |  
```

*Hint: you may find the optional arguments to `print` useful. You can read about them [here](https://docs.python.org/3.4/library/functions.html#print)*

### Printing #2 (challenge)

Write a program that, when run, prints out a SUPER tic-tac-toe board.

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

You'll find that there may be many ways to solve this problem. Which do you think is the most 'pythonic?' Talk to someone next to you about your approach to this problem. Remember the Zen of Python!

### Fizz, Buzz, FizzBuzz!
If we list all of the natural numbers under 41 that are a multiple of 3 or 5, we get

```
 3,  5,  6,  9, 10, 12, 15,
18, 20, 21, 24, 25, 27, 30,
33, 35, 36, 39, 40
```

The sum of these numbers is 408.

Find the sum of all the multiples of 3 or 5 below 1001.

### Collatz Sequence
Depending on who you took CS106A from, you may have seen this problem before.

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

What is the length of the longest chain which has a starting number under 1000?

*NOTE: Once the chain starts the terms are allowed to go above one thousand.*

Challenge: Same question, but for any starting number under 1,000,000 (you may need to implement a cleverer-than-naive algorithm)

### Fahrenheit-to-Celsius converter
Write a program to convert degrees Fahrenheit to degrees Celcius by (1) asking the user for a number (not necessarily integral) representing the current temperature in degrees Fahrenheit, (2) converting that value into the equivalent degrees Celsius, and (3) printing the final equivalent value.

For example, your program should be able to emulate the following sample run:

```
Temperature F? 212
It is 100.0 degrees Celsius.

Temperature F? 98.6
It is 37.0 degrees Celsius.

Temperature F? 10
It is -12.222222222222221 degrees Celsius.
```

Want to be fancy (challenge)? Try to print the final temperature to two decimal places. *Hint: Take a look at the [`round()`](https://docs.python.org/3.4/library/functions.html#round) function. Isn't Python great?*

## Done Early?

Skim [Python’s Style Guide](https://www.python.org/dev/peps/pep-0008/), keeping the Zen of Python in mind. Feel free to skip portions of the style guide that cover material we haven't yet touched on in this class, but it's always good to start with an overview of good style.

## Submitting Labs

Alright, you did it! There's nothing to submit for this lab. You're free to leave as soon as you've finished this lab.

*Credit to ProjectEuler and InterviewCake for some of the above problem ideas.*

> With <3 by @sredmond