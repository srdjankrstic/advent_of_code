import argparse
import re
from collections import defaultdict
import itertools as it
import math


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
d = 0
xx = 0 
yy = 0

if args.part == 1:
    for line in lines.splitlines():
        if not line:
            continue
        m = re.match("^(.)(.*)$", line)
        c = m.group(1)
        v = int(m.group(2))
        if c == 'N':
            yy += v
        elif c == 'S':
            yy -= v
        elif c == 'E':
            xx += v
        elif c == 'W':
            xx -= v
        elif c == 'L':
            d = int((d + v/90 + 4) % 4)
        elif c == 'R':
            d = int((d - v/90 + 4) % 4)
        elif c == 'F':
            xx += di[d] * v
            yy += dj[d] * v
        print(abs(xx) + abs(yy))

if args.part == 2:
    wx = 10
    wy = 1
    for line in lines.splitlines():
        if not line:
            continue
        m = re.match("^(.)(.*)$", line)
        c = m.group(1)
        v = int(m.group(2))
        if c == 'N':
            wy += v
        elif c == 'S':
            wy -= v
        elif c == 'E':
            wx += v
        elif c == 'W':
            wx -= v
        elif c == 'L':
            if v == 90:
                t = wx
                wx = -wy
                wy = t
            elif v == 180:
                wx *= -1
                wy *= -1
            elif v == 270:
                t = wx
                wx = wy
                wy = -t
        elif c == 'R':
            if v == 90:
                t = wx
                wx = wy
                wy = -t
            elif v == 180:
                wx *= -1
                wy *= -1
            elif v == 270:
                t = wx
                wx = -wy
                wy = t
        elif c == 'F':
            xx += wx * v
            yy += wy * v
#        print(f"{xx}, {yy}, {wx}, {wy}")
    print(abs(xx) + abs(yy))
