from functools import reduce

sequence = [ 2, 2, 2, 2, 2]
totally_sequence = reduce(lambda a, b: a * b , sequence)
print(totally_sequence)