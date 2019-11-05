#!/usr/bin/env python3 -tt
"""(Incomplete) reference solutions to Lab 5 for CS41: Hap.py Code.

Revision history:
@sredmond 05-18-2016 Created
"""

class Course:
    def __init__(self, department, number, title):
        self.department = department
        self.number = number
        self.title = title

class CSCourse(Course):
    def __init__(self, number, title, recorded=False):
        super().__init__("CS", number, title)
        self.recorded = recorded

"""
cs106a = Course("CS", "106A", "Programming Methodology")
cs106b = CSCourse("106B", "Programming Abstractions")

1. type(cs106a)  # => Course
2. isinstance(cs106a, Course)  # => True
3. isinstance(cs106b, CSCourse)  # => True
4. type(cs106a) == type(cs106b)  # => False
5. cs106a == cs106b  # => False
"""
