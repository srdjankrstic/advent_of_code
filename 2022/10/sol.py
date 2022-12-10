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
    X = 1
    cycle = 0
    for li, line in enumerate(lines):
        cycle += 1
        if cycle % 40 == 20:
            sol += X * (cycle)
        w = line.split(' ')
        if len(w) != 2:
            continue
        cycle += 1
        if cycle % 40 == 20:
            sol += X * (cycle)
        X += int(w[1])
    return sol

def f2():
    sol = 0
    X = 1
    cycle = 0
    for li, line in enumerate(lines):
        cycle += 1
        crtx = cycle % 40
        if crtx == 0:
            print()
        if X <= crtx < X + 3:
            print('#', end='')
        else:
            print('.', end='')

        w = line.split(' ')
        if len(w) != 2:
            continue
        cycle += 1
        crtx = cycle % 40
        if crtx == 0:
            print()
        if X <= crtx < X + 3:
            print('#', end='')
        else:
            print('.', end='')

        X += int(w[1])
    return sol


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
