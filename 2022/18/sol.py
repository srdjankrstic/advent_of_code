import argparse
import re
from collections import defaultdict
from functools import reduce, cmp_to_key, lru_cache
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
    points = set()
    for li, line in enumerate(lines):
        [x, y, z] = lib.rints(line)
        points.add(lib.Point(x, y, z))

    for p in points:
        for op in p.neigh_l1():
            if op not in points:
                sol += 1

    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    points = set()
    for li, line in enumerate(lines):
        [x, y, z] = lib.rints(line)
        points.add(lib.Point(x, y, z))

    minx = min(p[0] for p in points)
    maxx = max(p[0] for p in points)
    miny = min(p[1] for p in points)
    maxy = max(p[1] for p in points)
    minz = min(p[2] for p in points)
    maxz = max(p[2] for p in points)

    visited = set()
    q = []
    q.append(lib.Point(minx - 1, miny, minz))
    visited.add(lib.Point(minx - 1, miny, minz))

    while len(q):
        p = q.pop(0)
        for np in lib.Point(p).neigh_l1():
            if np in points or np in visited or np[0] < minx-1 or np[0] > maxx+1 or np[1] < miny-1 or np[1] > maxy+1 or np[2] < minz-1 or np[2] > maxz+1:
                continue
            q.append(np)
            visited.add(np)

    for p in points:
        for op in p.neigh_l1():
            if op not in points and op in visited:
                sol += 1

    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
