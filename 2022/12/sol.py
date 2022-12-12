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
    h = []
    sx = sy = fx = fy = 0
    for li, line in enumerate(lines):
        h.append([])
        for i, c in enumerate(line):
            cc = 'a' if c == 'S' else 'z' if c == 'E' else c
            cc = ord(cc) - ord('a')
            h[-1].append(cc)
            if c == 'S':
                sx = li; sy = i
            elif c == 'E':
                fx = li; fy = i
    I = len(h)
    J = len(h[0])
    q = [((sx, sy), 0)]
    visited = set()
    visited.add((sx, sy))

    while True:
        ((qx, qy), s) = q.pop(0)
        if qx == fx and qy == fy:
            return s
        for d in range(4):
            px = qx + di[d]; py = qy + dj[d]
            if 0 <= px < I and 0 <= py < J and (px, py) not in visited and h[px][py] - h[qx][qy] <= 1:
                visited.add((px, py))
                q.append(((px, py), s + 1))
    return 0

def f2():
    sol = 0
    h = []
    sx = sy = fx = fy = 0
    for li, line in enumerate(lines):
        h.append([])
        for i, c in enumerate(line):
            cc = 'a' if c == 'S' else 'z' if c == 'E' else c
            cc = ord(cc) - ord('a')
            h[-1].append(cc)
            if c == 'S':
                sx = li; sy = i
            elif c == 'E':
                fx = li; fy = i
    I = len(h)
    J = len(h[0])
    q = []
    visited = set()
    for i in range(I):
        for j in range(J):
            if h[i][j] == 0:
                q.append(((i, j), 0))
                visited.add((i, j))

    while True:
        ((qx, qy), s) = q.pop(0)
        if qx == fx and qy == fy:
            return s
        for d in range(4):
            px = qx + di[d]; py = qy + dj[d]
            if 0 <= px < I and 0 <= py < J and (px, py) not in visited and h[px][py] - h[qx][qy] <= 1:
                visited.add((px, py))
                q.append(((px, py), s + 1))


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
