# Lab 1: Welcome to Python!

## Goals
The primary goal is to ensure that your Python installation process went smoothly, and that there are no lingering Python 2/3 bugs floating around.

This lab also gives you the chance to write what might be your first programs in Python, and allows you to experiment with both scripts and with the interactive interpreter.

These problems are not intended to be algorithmically challenging - just ways to flex your new Python 3 muscles. Even if the problems seem simple, work through them quickly, and then you're free to go.

## Warming Up

### Hello World

If you haven’t already, write a Hello World program which consists of getting Python to print "Hello, World!" to the console. First, write this program using the interactive interpreter. Next, put the body of the program into a file named `hello.py`, and run the Hello World program as a Python script.

### Printing

Write a program using `print()` that, when run, prints out a tic-tac-toe board.

```
  |  |
--------
  |  |
--------
  |  |  
```

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

*Hint: you may find the optional arguments to `print` very useful. You can read about them [here](https://docs.python.org/3.4/library/functions.html#print)*

### Fahrenheit-to-Celsius converter
Write a program to convert degrees Fahrenheit to degrees Celcius by (1) asking the user for a number (not necessarily integral) representing the current temperature in degrees Fahrenheit, (2) converting that value into the equivalent degrees Celsius, and (3) printing the final equivalent value.

For example, your program should be able to emulate the following sample run:

```
Temperature F? 212
It is 100.0 degrees Celsius

Temperature F? 98.6
It is 37.0 degrees Celsius

Temperature F? 10
It is -12.222222222222221 degrees Celsius
```

Want to be fancy (challenge)? Try to print the final temperature to two decimal places. *Hint: Take a look at the [`round()`](https://docs.python.org/3.4/library/functions.html#round) function. Isn't Python great?*

### Efficient Phrases

The following phrases are all 'efficient'

```
UNCONSCIOUS OMISSION
COLD WINDOWSILL
INSIDIOUS DOMINION
VOLUMINOUS PILLOWS
VIVID DISILLUSIONS
```

but none of the following phrases are 'efficient':

```
INSENSIBLE EXCLUSION
UNUSUAL OBLIGATION
CHILLY WINDOW LEDGE
ANCIENT APARTMENT
CAPACIOUS CUSHIONS
```

What makes a phrase efficient or inefficient? Only scroll down once you have a guess.

---

Efficient phrases are those for which every letter is drawn from `BCDGIJLMNOPSUVWZ` - that is, every letter can be drawn with a single stroke.

Your task is to write a function, `is_efficient_phrase`, to determine if a given phrase is efficient. For example,

```
is_efficient_phrase("UNCONSCIOUS OMISSION")  # => True
is_efficient_phrase("ANCIENT APARTMENT")     # => False
```

What approaches are there to this problem? Again, chat with a neighbor about the most 'pythonic' way you can think of.

*Credit to [Puzzling.SE](http://puzzling.stackexchange.com/questions/17079/what-is-an-efficient-phrase/17081)*

## Done Early?

Skim [Python’s Style Guide](https://www.python.org/dev/peps/pep-0008/), keeping the Zen of Python in mind. Feel free to skip portions of the style guide that cover material we haven’t yet touched on in this class. Nevertheless, itcan't hurt to start with an overview of good style.

## Still Done Early?

Alright, you did it! You're free to leave as soon as you've finished this lab.

