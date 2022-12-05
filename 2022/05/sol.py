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

# N = 3
N = 9

def f1():
    sol = 0
    stacks = []
    for i in range(N):
        stacks.append([])
    phase = 0
    for li, line in enumerate(lines):
        if not line:
            phase = 1
            continue
        if not phase:
            for i in range(N):
                z = line[4*i : min(len(line), 4*i+4)]
                if z.strip() and z[0] == '[':
                    stacks[i].append(z[1])
        else:
            [x, y, z] = lib.rints(line)
            y -= 1; z -= 1
            for i in range(x):
                stacks[z] = [stacks[y][0], *stacks[z]]
                stacks[y] = stacks[y][1:]
    sol = "".join([s[0] for s in stacks])
    return sol

def f2():
    sol = 0
    stacks = []
    for i in range(N):
        stacks.append([])
    phase = 0
    for li, line in enumerate(lines):
        if not line:
            phase = 1
            continue
        if not phase:
            for i in range(N):
                z = line[4*i : min(len(line), 4*i+4)]
                if z.strip() and z[0] == '[':
                    stacks[i].append(z[1])
        else:
            [x, y, z] = lib.rints(line)
            y -= 1; z -= 1
            stacks[z] = [*stacks[y][0:x], *stacks[z]]
            stacks[y] = stacks[y][x:]
    sol = "".join([s[0] for s in stacks])
    return sol


f = open(args.input, "r")
lines = [line for line in f.read().splitlines()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
