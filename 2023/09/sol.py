import argparse
import re
from collections import defaultdict
from functools import reduce, cmp_to_key
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

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        allnums = []
        allnums.append(lib.rnints(line))
        n = 0
        while True:
            if all([x == 0 for x in allnums[n]]):
                break
            newnums = []
            for i in range(len(allnums[n]) - 1):
                newnums.append(allnums[n][i + 1] - allnums[n][i])
            allnums.append(newnums)
            n += 1
        sol += sum([allnums[i][-1] for i in range(len(allnums))])
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        allnums = []
        allnums.append(lib.rnints(line))
        n = 0
        while True:
            if all([x == 0 for x in allnums[n]]):
                break
            newnums = []
            for i in range(len(allnums[n]) - 1):
                newnums.append(allnums[n][i + 1] - allnums[n][i])
            allnums.append(newnums)
            n += 1
        newsol = 0
        for x in range(len(allnums) - 1, -1, -1):
            newsol = allnums[x][0] - newsol
        sol += newsol
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
