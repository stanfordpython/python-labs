#!/usr/bin/env python3 -tt
"""
File: lab1solutions.py
----------------------
Reference solutions to Lab 1 for CS41: Hap.py Code.

"""
import math
DICTIONARY_PATH = '/usr/share/dict/words'  # Feel free to change this to your dictionary


def say_hello():
		"""Prints "Hello, world!" """
		print("Hello, World!")


def print_tictactoe():
		"""Print out a tic tac toe board using print's `sep` keyword argument

		Note: this is just one of many ways to solve this problem, chosen to
		illustrate .join, list multiplication, .format, string multiplication,
		and, of course, `sep`.
		"""
		row = '|'.join(['  '] * 3)      # row = '  |  |  '
		div = '\n{}\n'.format('-' * 9)  # div = '--------'
		print(div.join([row] * 3))


def print_super_tictactoe():
		"""Prints a super tic-tac-toe board using print's `sep` keyword.

		Note: As above, this is just one of many ways to accomplish this program, and
		it isn't very readable, or very fast! But, it does illustrate using the `sep`
		keyword.
		"""
		row = 'H'.join(['  |  |  '] * 3)  # row = '  |  |  H  |  |  H  |  |  '
		div = '\n'+ 'H'.join(['--+--+--'] * 3) + '\n'  # div = '\n--+--+--H--+--+--H--+--+--\n'
		superdiv = '\n' + '+'.join(['=' * 8] * 3) + '\n'  # superdiv = '\n========+========+========\n'
		block = div.join([row] * 3)
		print(superdiv.join([block] * 3))


def fizzbuzz(n):
		"""Returns the sum of all numbers < n divisible by 3 or 5.

		This iterative approach will work really well, and if it gets the job done
		reasonably quickly, that's all we should ask for.

		If you want to write this in one line, the following will work:

				return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

		However, that line isn't particularly Pythonic, since we're basically just
		compressing the syntax of an iterative for loop into one line - no big changes
		except for the use of `sum`.

		Another approach, as we'll learn about soon, is to use `filter`:

				return sum(filter(lambda i: i % 3 == 0 and i % 5 == 0, range(n)))

		However, in many ways, this isn't much different, since we're still specifying a
		function (admittedly, a `lambda` or anonymous function - which we'll learn about Week 4)
		over our range of numbers.

		For a job this simple, the iterative approach will suffice.
		"""
		count = 0
		for i in range(n):
				if i % 3 == 0 or i % 5 == 0:
						count += i
		print(count)
		return count


def collatz_len(n):
		"""Computes the length of the Collatz sequence starting at `n`.

		While this iterative approach might look "unpythonic" at first,
		the Collatz sequence is a very iterative algorithm, and there aren't
		very many easy functional ways to solve this problem.

		One benefit of this approach is that we do not store the entire
		sequence in memory - since we're only interested in the length, that
		would be wasteful.
		"""
		length = 1
		while n > 1:
				if n % 2 == 0:
						n //= 2  # We want to explicitly use integer division here, even though n is even.
				else:
						n = 3 * n + 1
				length += 1  # Note: Python has no increment operator (like ++), so we use += 1
		return length


def max_collatz_len(n):
		"""Computes the longest Collatz sequence length for starting numbers < n

		In Python, the `max` function returns the largest element of some collection.
		Since "finding the max element" isn't naturally iterative (although it can be
		solved iteratively), we can use this functional-looking code to compute the
		maximal collatz length. Note, however, that this approach buffers the list of
		lengths in memory (due to the list comprehension). In general, we can mitigate
		this problem using a generator comprehension (look it up!) rather than a list
		comprehension, but we'll cover that later in the course.

		An even more Pythonic way to solve this problem is to use `map`, which applies a
		function to all elements of a sequence.

				return max(map(collatz_len, range(1, n)))

		"""
		return max([collatz_len(i) for i in range(1, n)])


def collatz_len_fast(n, cache):
		"""Slightly more clever way to find the collatz length.

		A dictionary is used as a cache of previous results, and since
		the dictionary passed in is mutable, our changes will reflect
		in the caller.
		"""
		if n == 1:
				return 1
		if n in cache:
				return cache[n]

		if n % 2 == 0:
				cache[n] = collatz_len_fast(n // 2, cache) + 1
		else:
				cache[n] = collatz_len_fast(3 * n + 1, cache) + 1
		return cache[n]


def max_collatz_len_fast(n):
		"""Slightly faster way to compute the longest Collatz sequence for numbers < n

		We use the exact same tactic as in `max_collatz_len` above, with the added
		optimization that we only look over the second half of the range, since everything
		in the first half has a x2 preimage.
		"""
		cache = {}
		return max(collatz_len_fast(i, cache) for i in range(n // 2, n))


def convert_fahr_to_cels(deg_fahr):
		"""Converts a temperature in degrees Fahrenheit to degrees Celsius."""
		cels = (fahr - 32) * 5 / 9


def converter():
		"""Converts user-specified temperatures from Fahrenheit to Celsius.

		This problem exists to check that you're running Python 3, where
		`input` returns a string and division is double division by default, in
		contrast to Python 2, where `input` quasi-evaluates it's input and division
		is integer (floored) division by default.

		Note: There's some extra code here (the try/except/else stuff) so that the
		solutions can continue to run after you break out of the converter. We'll
		talk about advanced exception handling Week 5.
		"""
		print("Convert from Fahrenheit to Celsius with this lovely tool!")
		print("For the purposes of the lab solutions, hit CTRL+C to quit.")
		while True:
				try:
						fahr = float(input("Temperature F? "))
				except KeyboardInterrupt:
						print("\nExiting converter...")
						break
				except ValueError as exc:
						print(exc)
				else:
						cels = (fahr - 32) * 5 / 9
						# cels = round(cels, 2)  # Round to two decimal places
						print("It is {} degrees Celsius".format(cels))
						
						
def get_english_words(dictionary_path):
	"""Returns a set of trimmed, capitalized English words from a path to a dictionary.

	The dictionary is assumed to have one English word per line.

	If dictionary_path can not be read or is formatted incorrectly, a default English word
	set is returned containing some fruits.

	Note that we keep the file open for as little time as possible, which is
	generally a good practice. One downside of this implementation is that it
	buffers all of the words in memory (first as a string, and later as a collection
	of lines, but the word list is a known finite size (and that size isn't *too*
	big), so this approach will work fine. Iterating through the lines in the file
	with a for loop could mitigate this downside.

	We then use a set comprehension to build an uppercased collection of all of
	the words in the dictionary.

	Note that we choose to represent the English words as a set, because we want fast
	membership testing (using `in`) and also want to be able to iterate over all words.
	"""
	try:
		with open(dictionary_path, 'r') as f:
			content = f.read()
		return {line.strip().upper() for line in content.split('\n') if line}
	except OSError:
		return {'APPLE', 'BANANA', 'PEAR', 'ORANGE'}


if __name__ == '__main__':
		"""Runs each of the lab solution functions and prints the attached docstring and source."""
		english = get_english_words(DICTIONARY_PATH)
		fns = [
				# Comment out any functions that you do not want to run
				(say_hello, (), {}),
				(print_tictactoe, (), {}),
				(print_super_tictactoe, (), {}),
				(fizzbuzz, (1001,), {}),
				(max_collatz_len, (1000,), {}),
				(max_collatz_len_fast, (1000000,), {}),
				(converter, (), {}),
		]
		for fn, args, kwargs in fns:
				name = fn.__name__
				print("*" * len(name))        # header
				print(name)                   # function name
				print(fn.__doc__)             # function docstring
				res = fn(*args, **kwargs)     # variadic argument unpacking - cool stuff!
				'''if res:
						print(res)
				input("Press [ENTER] to continue...")'''
		print("Done!")

