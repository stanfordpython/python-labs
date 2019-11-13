"""
Solutions for Lab 3

@parthsarin 11-11-19 Created file
"""

"""
PART 1
"""
# Lattice Paths
def lattice_paths(m, n):
	"""
	When m == 0 or n == 0, the grid is actually one-dimensional,
	so there's only one way to get to the end: just walk down the line.

	Otherwise, you have to compute the number of paths if you go down,
	and the number of paths if you go right, and add them together.
	"""
    if m == 0 or n == 0:
        return 1
    
    return lattice_paths(m-1, n) + lattice_paths(m, n-1)

# Lattice Paths Memoized
memoization_dict = {}

def lattice_paths_memoized(m, n):
	"""
	The base case is the same as the last function but now, we add
	tuples to the memoization dict if they aren't already in the dict.

	Then, at the end, we can just return the value stored in the dict.
	"""
    if m == 0 or n == 0:
        return 1

    if (m, n) not in memoization_dict:
		memoization_dict[(m, n)] = lattice_paths_memoized(m-1, n) + lattice_paths_memoized(m, n-1)

    return memoization_dict[(m, n)]

lattice_paths_memoized(2, 2)   # => 6
lattice_paths_memoized(6, 6)   # => 924
lattice_paths_memoized(20, 20) # => 137846528820
lattice_paths_memoized(40, 40) # => 107507208733336176461620

"""
PART 2
"""