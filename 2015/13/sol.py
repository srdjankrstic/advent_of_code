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

ppl = set()
wt = defaultdict(int)
for li, line in enumerate(lines):
    line = line.rstrip(".")
    w = line.split(" ")
    ppl.add(w[0]); ppl.add(w[-1])
    v = int(w[3]) * (1 if w[2] == "gain" else -1)
    wt[(w[0], w[-1])] += v
    wt[(w[-1], w[0])] += v

if args.part == 2:
    for p in ppl:
        wt[(p, "Srdjan")] = 0; wt[("Srdjan", p)] = 0
    ppl.add("Srdjan")

b = 0
n = len(ppl)
for p in it.permutations(ppl):
    t = 0
    for i in range(n):
        t += wt[(p[i], p[(i + 1) % n])]
    b = max(b, t)


print(b)
