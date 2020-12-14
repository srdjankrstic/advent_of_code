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

ranges = []
alls = []
for li, line in enumerate(lines):
    x = lib.rints(line)
    ranges.append((x[0], x[1]))
    alls.append((x[0], '1s'))
    alls.append((x[1], '2e'))

MAX = 4294967295
#MAX = 9
alls = sorted(alls)
last = -1
o = 0
tot = 0
for i, e in enumerate(alls):
    if e[1] == '1s':
        o += 1
        if o == 1:
            if args.part == 1:
                if e[0] > last + 1:
                    print(last + 1)
                    break
            elif args.part == 2:
                tot += e[0] - last - 1
    else:
        o -= 1
        if o == 0:
            last = e[0]

if args.part == 2:
    tot += MAX - last
    print(tot)
