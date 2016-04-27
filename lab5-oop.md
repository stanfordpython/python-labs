# Lab 5: Object-Oriented Python

*Note: there may be some typos in this lab, so periodically refresh GitHub to make sure you're always working on the latest version*

## Overview

After Monday's lecture on mostly rules, definitions, and semantics, we'll be playing around with actual classes today, writing a lot of code and building several classes to solve a variety of problems.

## Stanford Prereqs

### Basic Class

Let’s create a class to represent courses at Stanford! Copy the following into a file and save it as `courses.py`.

```
class Course:
    def __init__(self, department, number, title):
        self.department = department
        self.number = number
        self.title = title
```

We can import this class definition and create an instance of the class in the interacitve interpreter, by running:

```
$ python3
>>> from courses import Course
>>> stanford_python = Course("CS", "41", "hap.py code: The python programming language")
```

We can access attributes of `stanford_python`, our instance object:

```
>>> from courses import Course
>>> stanford_python = Course("CS", "41", "hap.py code: the python programming language")
>>> stanford_python.title
'hap.py coder: the python programming language'
>>> stanford_python.number
41
>>>
```

### Inheritance

Let’s add inheritance by creating a `CSCourse` class that takes an additional parameter `recorded` that defaults to `False`

Write the following code snippet in the `courses.py` file:

```
class CSCourse(Course):
    def __init__(self, department, number, title, recorded=False):
        super().__init__(department, number, title)
        self.is_recorded = recorded
```

The `super()` call is a little bit of magic to us at this point - it builds an object described by the superclass, allowing us to call the `__init__` method on that object.

Assess the following equalities in your Python interpreter. You can import both classes by running either one of the following lines in your terminal

```
>>> from courses import Course, CSCourse
>>> a = Course("CS", "106A", "Programming Methodology")
>>> b = CSCourse("CS", "106B", "Programming Abstractions")
```

What is the output of the statements below?

```
1. type(a)
2. isinstance(a, Course)
3. isinstance(b, Course)
4. type(a) == type(b)
5. a == b
```

### Additional Attributes

Let's add more functionality to the `Course` class!

* Add a property `students` to the `Course` class that tracks whether students are here or not.
* Create a method `mark_attendance(*students)` that takes a splat operator `students` to mark students as present or absent.
* Create a method `is_present(student)` that takes a student’s name as a parameter and returns `True` if the student is present and `False` otherwise.

### Implementing Prerequesites

Now we want to implement functionality to determine if one course is a prerequisite of another. In our implementation, we will assume that each one course is a prerequisite for another if it is in the same department and the numeric part of the course number is less. For example, after implementing:

```
>>> cs106a = Course("CS", "106A", "Programming Methodology")
>>> cs106b = CSCourse("CS", "106B", "Programming Abstractions")
>>> cs107 = CSCourse("CS", "107", "Computer Organzation and Systems")
>>> cs110 = CSCourse("CS", "110", "Principles of Computer Systems")
>>> cs110 > cs106b
True
>>> cs107 > cs110
False
```

To accomplish this, you will need to implement a magic method `__le__` that will add functionality to determine if a course is a prerequisite for another course. Read up on [total ordering](https://docs.python.org/3.4/library/functools.html#functools.total_ordering) to figure out what `__le__` should return based on the argument you pass in.

To give a few hints on how to add this piece of functionality might be implemented, consider how you might extract the actual `int` number from the course number attribute, which might be a string, or might be a number. 

We encourage you to think about the most space and time-efficient way to accomplish this bit of functionality - perhaps you might investigate creating another class just to store the relations between the instances of `Course`.

### Instructors (challenge)

Allow the class to take a splat argument `instructors` that will take any number of strings and store them as a list of instructors.

Modify the way you track attendance in the `Course` class to map a Python date object (you can use the `datetime` module) to a data structure tracking what students are there on that day.

## SimpleGraph

In this part, you'll build the implementation for a SimpleGraph class in Python whose functionality imitates that of the BasicGraph class in the Stanford CPP libraries.

In particular, you will need to define a `Vertex` class, an `Edge` class, and a `SimpleGraph` class. The specification is as follows:

A `Vertex` has attributes:

* `name`, a string representing the label of the vertex.
* `edges`, a set representing edges outbound from this vertex to its neighbors

A new Vertex should be initialized with an optional `name`, which defaults to `""`, and should be initialized with an empty edge set.

An `Edge` has attributes:

* `start`, a `Vertex` representing the start point of the edge.
* `end`, a `Vertex` representing the end point of the edge.
* `cost`, a `float` (used for graph algorithms) representing the weight of the edge.
* `visited`, a `bool` (used for graph algorithms) representing whether this edge has been visited before.

Note that for our purposes, an `Edge` is directed.

An `Edge` requires a `start` and `end` vertex in order to be instantiated. `cost` should default to 1, and `visited` should default to `False`, but both should be able to be set via an initializer.

A `SimpleGraph` has attributes

* `verts`, a collection of `Vertex`s (you need to decide the collection type)
* `edges`, a collection of `Edge`s (you need to decide the collection type)

as well as several methods:

* `graph.add_vertex(v)`
* `graph.add_edge(v_1, v_2)`
* `graph.contains_vertex(v)`
* `graph.contains_edge(e_1, e_2)`
* `graph.get_neighbors(v)`
* `graph.is_empty()`
* `graph.size()`
* `graph.remove_vertex(v)`
* `graph.remove_edge(v_1, v_2)`
* `graph.is_neighbor(v1, v2)`
* `graph.is_connected(v1, v2)  # Use any algorithm you like`
* `graph.clear_all()`

The actual implementation details are up to you.

*Note: debugging will significantly easier if you write `__str__` or `__repr__` methods on your custom classes.*

### Challenge: Graph Algorithms

If you're feeling up to the challenge, and you have sufficient time, implement other graph algorithms, including those covered in CS106B/X, using your SimpleGraph. The point isn't to check whether you still know your graph algorithms - rather, these algorithms will serve to test the correctness of your graph implementation. The particulars are up to you.

As some suggestions:

* Longest path
* D'ijkstras Algorithm
* A*
* Max Flow
* K-Clique
* Largest Connected Component
* is_bipartite

```
graph = SimpleGraph()
# Your extension code here
```

### Challenge: Using Magic Methods

See if you can rewrite the `SimpleGraph` class using magic methods to emulate the behavior and operators of standard Python. In particular,

```

```

## Timed Key-Value Store (challenge)
Let's build an interesting data structure straight out of an interview programming challenge from [Stripe](https://stripe.com/). This is more of an algorithms challenge than a Python challenge, but we hope you're still interested in tackling it.

At a high-level, we'll be building a key-value store (think Dictionary or HashMap) that has a `get` method that takes an optional second parameter as a `time` object in Python to return the most recent value before that period in time. If no key-value pair was added to the map before that period in time, return `None`.

For consistency’s sake, let’s call this class `TimedKVStore` and put it into a file called `kv_store.py`

You’ll need some sort of `time` object to track when key-value pairs are getting added to this map. Consider using the `time` module from Python [Docs](https://docs.python.org/2/library/time.html)

To give you an idea of how this class works, this is what should happen after you implement `TimedKVStore`.

```
>>> from kv_store import *
>>> d = TimedKVStore()
>>> t0 = time.time()
>>> d.put("1", 1)
>>> t1 = time.time()
>>> d.put("1", 1.1)
>>> d.get("1")
1.1
>>> d.get("1", t1)
1
>>> d.get("1", t0)
None
```

### Bonus
Implement a method called `remove(key)` that takes a key and removes that entire key from the key-value store.

Write another `remove(key, time)` method that takes a key and removes all memory of values before that time method.

## Inheritance

Consider the following code:

```
"""Examples of Single Inheritance"""
class Transportation:
    wheels = 0

    def __init__(self):
        self.wheels = -1

    def travel_one(self):
        print("Travelling on generic transportation")

    def travel(self, distance):
        for _ in range(distance):
            self.travel_one()

    def is_auto(self):
        return self.wheels == 4

class Bike(Transportation):

    def travel_one(self):
        print("Biking one mile")

class Car(Transportation):
    wheels = 4

    def travel_one(self):
        print("Driving one mile")

    def make_sound(self):
        print("VROOM")

class Ferrari(Car):
    pass

t = Transportation()
b = Bike()
c = Car()
f = Ferrari()
```

Predict the outcome of each of the following lines of code.

```
isinstance(t, Transportation)

isinstance(b, Bike)
isinstance(b, Transportation)
isinstance(b, Car)
isinstance(b, t)

isinstance(c, Car)
isinstance(c, Transportation)

isinstance(f, Ferrari)
isinstance(f, Car)
isinstance(f, Transportation)

issubclass(Bike, Transportation)
issubclass(Car, Transportation)
issubclass(Ferrari, Car)
issubclass(Ferrari, Transportation)
issubclass(Transportation, Transportation)

b.travel(5)
c.is_auto()
f.is_auto()
b.is_auto()
b.make_sound()
c.travel(10)
f.travel(4)
```

## Bloom Filter (challenge)
A bloom filter is a fascinating data structure that support insertion and probabilistic set membership. Read up on Wikipedia!

Write a class `BloomFilter` to implement a bloom filter data structure. Override the `__contains__` method so that membership can be tested with `x in bloom_filter`.

## Exceptions

### Reading

Skim over [Python's documentation on built-in exceptions](https://docs.python.org/3.4/library/exceptions.html).

### `try`/`except`/`else`/`finally`

Python provides `try` and `except` blocks , similar to other languages' `try` and `catch` blocks, for basic exceptional control flow.

#### `get_age`

Write a function `get_age` that asks a user for their age, which must be a positive integer between 0 and 123 (the oldest human recorded, Jeanna Clement, died at the age of 122). If the user enters something that's not an integer, you should reprompt them. However, if they enter an integer and it's out of range, you should raise an exception. That is, you should keep reprompting them until they enter something that can be converted into an integer, and then return that number if it's in range, and raise an exception otherwise. Two sample runs are shown below

```
# (Call 1)
How old are you? ABC
Invalid integer input.
How old are you? -4.5
Invalid integer input.
How old are you? 36
# returns 36

# (Call 2)
How old are you? XYZ
Invalid integer input.
How old are you? 128
# raises some exception
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Age 128 out of range
```

### Custom Exceptions

Write a custom exception class called `OutOfRangeError` that inherits from `ValueError` which indicates that a given value is outside of an acceptable range. What does this class definition look like? What is the body of the class?

``` 
# Implement OutOfRangeError
```

Rewrite your code in `get_age` to use this custom exception. Do you need to change any other code?

### Using `else` and `finally`

Rewrite your `get_age` function to use the `else` block, and optionally the `finally` block. As is consistent with general style guidelines, try to keep the `try` block as short as possible, containing just the code that might raise the exception you're trying to catch.

### Reraising

Consider the following code:

```
try:
	print("in try")
	# (A)
except Exception as exc:
	print("in except")
	# (B)
else:
	print("in else")
	# (C)
finally:
    print("in finally")
    # (D)
```

We're going to add some errors to this code block, which currently prints out

```
in try
in else
in finally
```

For each of the labelled locations, what happens if we `raise Exception()` at that position? Run the code to test your hypotheses.

> With <3 by @sredmond