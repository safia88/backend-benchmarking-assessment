#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function find_anagrams which can be used to do the same
for an arbitrary list of strings.
"""

import sys
from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "Safia Ali"


def alphabetize(string):
    """Returns alphabetized version of the string"""
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    anagrams = defaultdict(list)

    for word in words:
        anagrams[alphabetize(word)].append(word)
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
        for k, v in find_anagrams(words).items():
            if len(v) > 1:
                print('{}:{}'.format(k, v))


if __name__ == "__main__":
    main(sys.argv[1:])
