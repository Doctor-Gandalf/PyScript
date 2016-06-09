#!/usr/local/bin/python3
from sys import argv
from itertools import permutations

if __name__ == "__main__":
    if len(argv) > 1:
        print([''.join(i) for i in permutations(argv[1])])
    else:
        print("Usage: arg[1] - String to list permutations")