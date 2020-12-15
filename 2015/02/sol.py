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

tot = 0
tot2 = 0
for li, line in enumerate(lines):
    [a, b, c] = lib.rints(line)
    tot += 2 * (a*b + a*c + b*c) + min(a*b, a*c, b*c)
    tot2 += 2 * (a + b + c - max([a, b, c])) + a*b*c
print(tot)
print(tot2)
