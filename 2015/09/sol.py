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

c = set()
d = defaultdict(int)

for li, line in enumerate(lines):
    w = line.split(" ")
    c.add(w[0])
    c.add(w[2])
    d[(w[0], w[2])] = int(w[-1])
    d[(w[2], w[0])] = int(w[-1])

shortest = 100000000000
longest = 0

c = list(c)
for p in it.permutations(c):
    t = 0
    for z in range(1, len(p)):
        t += d[(p[z-1], p[z])]
    shortest = min(shortest, t)
    longest = max(longest, t)
print(shortest)
print(longest)