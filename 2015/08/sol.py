import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

Q = False
E = False
sol = 0
sol2 = 0
for li, line in enumerate(lines):
    n = len(line)
    i = 0
    sol2 += 2
    while i < n:
        c = line[i]
        if c == '"':
            sol += 1
            sol2 += 1
        elif c == '\\':
            if line[i+1] == '\\':
                sol += 1
                sol2 += 2
                i += 1
            elif line[i+1] == '"':
                sol += 1
                sol2 += 2
                i += 1
            elif line[i+1] == 'x':
                sol += 3
                sol2 += 1
                i += 3
        i += 1

print(sol)
print(sol2)
