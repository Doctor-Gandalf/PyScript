#!/usr/local/bin/python3
from sys import argv
from re import sub
from itertools import permutations


def anagrams(word, width):
    word_anagrams = [''.join(i) for i in permutations(argv[1])]
    anagram_string = sub(r'[\[|\]|\']', r'', str(word_anagrams))

    original = r'([^,]+, )'*width
    replacement = ''.join(
        [r'\{}'.format(i) for i in range(1, width+1)]) + r'\n'

    return sub(original, replacement, anagram_string)

if __name__ == "__main__":
    if len(argv) > 2:
        print(anagrams(argv[1], int(argv[2])))
    elif len(argv) == 2:
        print(anagrams(argv[1], 10))
    else:
        print("""    Usage:
            arg[1] - String to list anagrams
            arg[2] - Number of anagrams per line""")

