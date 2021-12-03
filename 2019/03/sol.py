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
import sympy.ntheory.factor_

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __init__(self, x1, y1, x2, y2):
        self.p1 = lib.Point(x1, y1)
        self.p2 = lib.Point(x2, y2)

    def vertical(self):
        return self.p1[0] == self.p2[0]

    def horizontal(self):
        return self.p1[1] == self.p2[1]

    def length(self):
        return self.p1.distance(self.p2)

    def intersect(self, other):
        if self.vertical():
            if other.vertical():
                return None
            if (
                min(self.p1[1], self.p2[1]) < other.p1[1] < max(self.p1[1], self.p2[1]) and
                min(other.p1[0], other.p2[0]) < self.p1[0] < max(other.p1[0], other.p2[0])
            ):
                return lib.Point(self.p1[0], other.p1[1])
            else:
                return None
        if self.horizontal():
            if other.horizontal():
                return None
            return other.intersect(self)


best = 99999999

segments = [[], []]
for li, line in enumerate(lines):
    x = 0
    y = 0
    for i in line.split(','):
        l = int(i[1:])
        if i[0] == 'U':
            segments[li].append(Line(x, y, x, y + l))
            y = y + l
        elif i[0] == 'R':
            segments[li].append(Line(x, y, x + l, y))
            x = x + l
        elif i[0] == 'D':
            segments[li].append(Line(x, y, x, y - l))
            y = y - l
        elif i[0] == 'L':
            segments[li].append(Line(x, y, x - l, y))
            x = x - l

totali = 0
for i in range(len(segments[0])):
    if i > 0:
        totali += segments[0][i-1].length()
    totalj = 0
    for j in range(len(segments[1])):
        if j > 0:
            totalj += segments[1][j-1].length()
        cand = segments[0][i].intersect(segments[1][j])
        if cand:
            if args.part == 1:
                if cand.norm() < best:
                    best = cand.norm()
            else:
                maybe = totali + totalj + segments[0][i].p1.distance(cand) + segments[1][j].p1.distance(cand)
                if maybe < best:
                    best = maybe
print(best)
