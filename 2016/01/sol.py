import argparse
import re
from collections import defaultdict
import itertools as it
import math
from advent_of_code import lib


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

di = lib.di4
dj = lib.dj4

for line in lines.splitlines():
    d = x = y = c = 0
    seen = set()
    w = [x.strip() for x in line.split(',')]
    ops = [(x[0], int(x[1:])) for x in w]
    for (o, n) in ops:
        if o == 'R':
            d += 1
        elif o == 'L':
            d -= 1
        d %= 4
        if args.part == 1:
            x += di[d] * n
            y += dj[d] * n
        elif args.part == 2:
            if di[d]:
                for pi in range(n):
                    if (x, y) in seen:
                        break
                    seen.add((x, y))
                    x += di[d]
            elif dj[d]:
                for pj in range(n):
                    if (x, y) in seen:
                        break
                    seen.add((x, y))
                    y += dj[d]
            if (x, y) in seen:
                break
    print(abs(x) + abs(y))
