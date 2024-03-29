import argparse
import re
from collections import defaultdict
from functools import reduce
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json
import sympy.ntheory.factor_

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

sol = 0

def f(x):
    g = max(x // 3 - 2, 0)
    if args.part == 1:
        return g
    else:
        return g + f(g) if g > 0 else g

for li, line in enumerate(lines):
    n = lib.rints(line)[0]
    sol += f(n)

print(sol)
