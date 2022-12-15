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

# Y = 10
Y = 2000000

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    minx = 1000000000
    maxx = -1
    sensors = []
    beacons = []
    bset = set()
    n = len(lines)
    for li, line in enumerate(lines):
        [x1, y1, x2, y2] = lib.rnints(line)
        sensors.append(lib.Point(x1, y1))
        beacons.append(lib.Point(x2, y2))
        bset.add((x2, y2))
        minx = min(minx, x1, x2)
        maxx = max(maxx, x1, x2)
    
    minx -= 1000000
    maxx += 1000000
    distances = [sensors[i].distance(beacons[i], norm=1) for i in range(n)]
    for x in range(minx, maxx):
        p = lib.Point(x, Y)
        for i in range(n):
            if sensors[i].distance(p, norm=1) <= distances[i] and (x, Y) not in bset:
                sol += 1
                break
    return sol

# F = 20
F = 4000000
M = 4000000

def atdist(p, dist):
    for c1 in range(-dist, dist + 1):
        y = dist - abs(c1)
        yield lib.Point(p[0] + c1, p[1] - y)
        yield lib.Point(p[0] + c1, p[1] + y)

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    sensors = []
    beacons = []
    bset = set()
    n = len(lines)
    for li, line in enumerate(lines):
        [x1, y1, x2, y2] = lib.rnints(line)
        sensors.append(lib.Point(x1, y1))
        beacons.append(lib.Point(x2, y2))
        bset.add((x2, y2))

    distances = [int(sensors[i].distance(beacons[i], norm=1)) for i in range(n)]

    for i in range(n):
        for p in atdist(sensors[i], distances[i] + 1):
            if not (0 <= p[0] <= F and 0 <= p[1] <= F):
                continue
            bad = False
            for j in range(n):
                if i == j:
                    continue
                if p.distance(sensors[j]) <= distances[j]:
                    bad = True
                    break
            if not bad:
                sol = p[0] * M + p[1]
                return sol

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
