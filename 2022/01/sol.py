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
import sympy.ntheory.factor_ as sf

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

def f1():
    sol = 0
    cur = 0
    for li, line in enumerate(lines):
        if line:
            cur += int(line)
        else:
            if cur > sol:
                sol = cur
            cur = 0
    return sol

def f2():
    sols = []
    cur = 0
    for li, line in enumerate(lines):
        if line:
            cur += int(line)
        else:
            sols.append(cur)
            cur = 0
    sols.append(cur)
    sols = sorted(sols)
    return sum(sols[-3:])


f = open(args.input, "r")
lines = [line for line in f.read().splitlines()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
