"""
Solutions for Lab 3

@parthsarin 11-11-19 Created file
"""

"""
PART 1
"""
def lattice_paths(m, n):
    if m == 0 or n == 0:
        return 1
    
    return lattice_paths(m-1, n) + lattice_paths(m, n-1)

memoization_dict = {}

def lattice_paths_memoized(m, n):
    if m == 0 or n == 0:
        return 1
    elif (m, n) in memoization_dict:
        return memoization_dict[(m, n)]
    
    output = lattice_paths_memoized(m-1, n) + lattice_paths_memoized(m, n-1)
    memoization_dict[(m, n)] = output
    return output

lattice_paths_memoized(2, 2)   # => 6
lattice_paths_memoized(6, 6)   # => 924
lattice_paths_memoized(20, 20) # => 137846528820
lattice_paths_memoized(40, 40) # => 107507208733336176461620

"""
PART 2
"""