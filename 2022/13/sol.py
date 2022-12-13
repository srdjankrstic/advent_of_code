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

def right(l, r):
    if lib.isint(l) and lib.isint(r):
        z = 1 if l < r else -1 if l > r else 0
        return z
    if lib.isint(l) and not lib.isint(r):
        l = [l]
    if lib.isint(r) and not lib.isint(l):
        r = [r]
    n = min(len(l), len(r))
    for i in range(n):
        x = right(l[i], r[i]) 
        if x == 1 or x == -1:
            return x
    if len(l) < len(r):
        return 1
    elif len(l) > len(r):
        return -1
    return 0

def f1(lines):
    sol = 0
    groups = []
    for i in lines.split("\n\n"):
        groups.append((eval(i.split("\n")[0]), eval(i.split("\n")[1])))
    for i, g in enumerate(groups):
        if right(g[0], g[1]) == 1:
            sol += i + 1
    return sol

def f2(lines):
    sol = 0
    groups = [[[2]], [[6]]]
    for i in lines.split("\n\n"):
        for j in i.split("\n"):
            groups.append(eval(j))

    n = len(groups)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if right(groups[i], groups[j]) == -1:
                tmp = groups[i]
                groups[i] = groups[j]
                groups[j] = tmp

    i1 = 0; i2 = 0
    for i, g in enumerate(groups):
        if g == [[2]]:
            i1 = i + 1
        elif g == [[6]]:
            i2 = i + 1
    sol = i1 * i2
    return sol

f = open(args.input, "r")
# lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
