import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def nice(s):
    if sum([1 for v in s if v in "aeiou"]) < 3:
        return False
    if any([x in s for x in ["ab", "cd", "pq", "xy"]]):
        return False
    return any([s[i] == s[i-1] for i in range(1, len(s))])

def nice2(s):
    if not any([s[i:i+2] in s[i+2:] for i in range(0, len(s) - 2)]):
        return False
    if not any([s[i] == s[i+2] for i in range(0, len(s) - 2)]):
        return False
    return True

if args.part == 1:
    print(sum([1 for x in lines if nice(x)]))
else:
    print(sum([1 for x in lines if nice2(x)]))
