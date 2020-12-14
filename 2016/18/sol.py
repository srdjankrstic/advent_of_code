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

STEPS = 40 if args.part == 1 else 400000
traps = [False] + [c == "^" for c in lines[0]] + [False]
n = len(traps)
tot = traps.count(False) - 2
prev = deepcopy(traps)

for s in range(STEPS-1):
    traps[0] = False; traps[-1] = False
    for i in range(1, n-1):
        l = prev[i-1]; c = prev[i]; r = prev[i+1]
        traps[i] = (l and c and not r) or (c and r and not l) or (l and not c and not r) or (r and not l and not c)
    tot += traps.count(False) - 2
    prev = deepcopy(traps)

print(tot)
