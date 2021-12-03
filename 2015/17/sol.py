import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

#MAX = 25
MAX = 150

ns = []
for li, line in enumerate(lines):
    ns.append(int(line))

tot = 0
ways = defaultdict(int)
for i in range(1, len(ns)+1):
    for p in it.combinations(ns, i):
        if sum(p) == MAX:
            ways[i] += 1
            tot += 1

print(tot)
print(ways[min(ways.keys())])
