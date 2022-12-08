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
    trees = []
    for li, line in enumerate(lines):
        trees.append([int(c) for c in line])
    n = len(trees)
    for i in range(n):
        for j in range(n):
            if (
                all(trees[i][p] < trees[i][j] for p in range(j)) or
                all(trees[i][p] < trees[i][j] for p in range(j+1, n)) or
                all(trees[p][j] < trees[i][j] for p in range(i)) or
                all(trees[p][j] < trees[i][j] for p in range(i+1,n))
            ):
                sol += 1
    return sol

def f2():
    sol = 0
    trees = []
    for li, line in enumerate(lines):
        trees.append([int(c) for c in line])
    n = len(trees)
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            score = 1
            for d in range(4):
                x = 0
                pi = i; pj = j
                while True:
                    pi += di[d]
                    pj += dj[d]
                    if 0 <= pi < n and 0 <= pj < n and trees[pi][pj] < trees[i][j]:
                        x += 1
                    else:
                        break
                if not(pi < 0 or pi == n or pj < 0 or pj == n):
                    x += 1
                score *= x
            if score > sol:
                sol = score
    return sol


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
