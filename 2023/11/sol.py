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
    cgrid = []
    galaxies = set()

    n = len(lines)
    m = len(lines[0])
    for li, line in enumerate(lines):
        cgrid.append([])
        empty = True
        for i, c in enumerate(line):
            cgrid[-1].append(c)
            if c == "#":
                empty = False
        if empty:
            cgrid.append(deepcopy(cgrid[-1]))
            n += 1

    j = 0
    while j < m:
        if all(cgrid[i][j] == "." for i in range(n)):
            for i in range(n):
                cgrid[i] = [*cgrid[i][:j], '.', *cgrid[i][j:]]
            m += 1
            j += 1
        j += 1

    for i in range(n):
        for j in range(m):
            if cgrid[i][j] == "#":
                galaxies.add(lib.Point(i, j))

    sol = 0
    for g1 in galaxies:
        for g2 in galaxies:
            sol += g1.distance(g2)
    return int(sol / 2)


def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    cgrid = []
    galaxies = set()

    n = len(lines)
    m = len(lines[0])
    emptyrows = []
    emptycols = []
    for li, line in enumerate(lines):
        cgrid.append([])
        empty = True
        for i, c in enumerate(line):
            cgrid[-1].append(c)
            if c == "#":
                empty = False
                galaxies.add(lib.Point(li, i))
        if empty:
            emptyrows.append(li)
    for j in range(m):
        if all(cgrid[i][j] == "." for i in range(n)):
            emptycols.append(j)

    MULT = 1000000
    sol = 0
    for g1 in galaxies:
        for g2 in galaxies:
            sol += g1.distance(g2)
            extrarows = [r for r in emptyrows if ((r > g1.coords[0] and r < g2.coords[0]) or (r > g2.coords[0] and r < g1.coords[0]))]
            extracols = [c for c in emptycols if ((c > g1.coords[1] and c < g2.coords[1]) or (c > g2.coords[1] and c < g1.coords[1]))]
            sol += (len(extrarows) + len(extracols)) * (MULT-1)
    return int(sol / 2)

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
