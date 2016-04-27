# Lab 5.2: Classes and Inheritance

This lab is going to delve into some practical features of classes in Python. Please submit any work you have at the end of lab to [our submission portal](http://stanfordpython.com/submit)

## Class Definition

Let’s create a class to represent courses at Stanford! Copy the following into a file and save it as `courses.py`.

```
class Course:
    def __init__(self, department, number, title):
        self.department = department
        self.number = number
        self.title = title
```

We can import this class definition and create an instance of the class in the sandbox, by running:
```
>>> from courses import Course
>>> python_course = Course("CS", "92SI", "hap.py coder: The python programming language")
```

Now we can play around with this instance of the class in our console:
```
>>> from courses import Course
>>> python_course = Course("CS", "92SI", "hap.py coder: the python programming language")
>>> python_course.title
'hap.py coder: the python programming language'
>>>
```

What happens when you pass in conflicting types of data into this different instances of this class?
```
>>> python_course = Course("CS", "92SI", "hap.py coder: the python programming language")
>>> python_course.number
“92SI”
>>> javascript_course = Course("CS", 42, "hap.py coder: the python programming language")
>>> javascript_course.number
```

**1.**Why does Python do this? (Please answer in a comment at the top of your file)

## Inheritance
Let’s add inheritance by creating a “CS_Course” class that takes an additional parameter `recorded` that defaults to `False`

Write the following code snippet in the `courses.py` file:
```
class CS_Course(Course):
    def __init__(self, department, number, title):
        Course.__init__(self, department, number, title)
        self.is_recorded = False
```

Assess the following equalities in your Python interpreter. You can import both classes by running either one of the following lines in your terminal
```
>>> from courses import Course, CS_Course
>>> from courses import *
```

After creating the following course instances, consider the statements below:
```
>>> a = Course(“CS”, “106A”, “Programming Methodology”)
>>> b = CS_Course(“CS”, “106B”, “Programming Abstractions”)
```

```
1. type(a)
2. isinstance(a, Course)
3. isinstance(b, Course)
4. type(a) == type(b)
5. a == b
```

**2.** Note any inconsistences that you noticed in a comment at the top of your `courses.py` file. (You can annotate your comments with `2.1` if you noticed an inconsistency with the first statement above)


## More properties and methods
Let's add more functionality to the `Course` class!

* Add a property `students` to the `Course` class that tracks whether students are here or not.

* Create a method `mark_attendance(*students)` that takes a splat operator `students` to mark students as present or absent.

* Create a method `is_present(student)` that takes a student’s name as a parameter and returns `True` if the student is present and `False` otherwise.

## Implementing Prerequesites
Now we want to implement functionality to determine if a course is a prerequsite of another. In our implementation, we will assume that each subsequent course that is instantiated requires all of the previous course listings as a prerequesite. For example, after implementing:
```
>>> cs106a = Course(“CS”, “106A”, “Programming Methodology”)
>>> cs106b = CS_Course(“CS”, “106B”, “Programming Abstractions”)
>>> cs107 = CS_Course(“CS”, “107”, “Computer Organzation and Systems”)
>>> cs110 = CS_Course(“CS”, “110”, “Principles of Computer Systems”)
>>> cs110 > cs106b
True
>>> cs107 > cs110
False
```

To accomplish this, we'd like you to implement a magic method `__le__` that will add functionality to determine if a course is a prerequisite for another course. Read up on [total ordering](https://docs.python.org/3.4/library/functools.html#functools.total_ordering) to figure out what `__le__` should return based on the argument you pass in.

To give a few hints on how to add this piece of functionality might be implemented, we would encourage you to think about using a class variable to represent some sort of ordering amongs the classes that get initialized. Every call to the `Course` `__init` method might want to order the class variable in a way that `__le__` knows exactly how to compare the two courses it is given. Check out the slides or this [awesome blog post](http://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide) for a refresher on Python namespacing and class variables.

We encourage you to think about the most space and time-efficient way to accomplish this bit of functionality - perhaps you might investigate creating another class just to store the relations between the instances of `Course`

## Bonus
Try out the following two tasks if there's more than `30` minutes left in lab!

Allow the class to take a splat argument `instructors` that will take any number of strings and store them as a list of instructors.

Modify the way you track attendance in the `Course` class to map a Python date object (you can use the `datetime` module) to a data structure tracking what students are there on that day.

## Timed key-value store
We’ll be building a really interesting problem straight out of an interview programming challenge from [Stripe](https://stripe.com/).

In a sentence, we’ll be building a key-value store (think Dictionary or HashMap) that has a `get` method that takes an optional second parameter as a `time` object in Python to return the most recent value before that period in time. If no key-value pair was added to the map before that period in time, return `None`.

For consistency’s sake, let’s call this class `TimedKVStore` and put it into a file called `kv_store.py`

You’ll need some sort of `time` object to track when key-value pairs are getting added to this map. Consider using the `time` module from Python [Docs](https://docs.python.org/2/library/time.html)

To give you an idea of how this class works, this is what should happen after you implement `TimedKVStore`.

```
>>> from kv_store import *
>>> d = TimedKVStore()
>>> t0 = time.time()
>>> d.put(“1”, 1)
>>> t1 = time.time()
>>> d.put(“1”, 1.1)
>>> d.get(“1”)
1.1
>>> d.get(“1”, t1)
1
>>> d.get(“1”, t0)
None
```

### Bonus
Implement a method called `remove(key)` that takes a key and removes that entire key from the key-value store.

Write another `remove(key, time)` method that takes a key and removes all memory of values before that time method.
