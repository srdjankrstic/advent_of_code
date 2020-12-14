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

m = dict(zip("RDLU", range(4)))
di = lib.di4
dj = lib.dj4
if args.part == 1:
    np = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    x = y = 1
else:
    np = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None]
    ]
    x = 2
    y = 0

sol = ""
for line in lines.splitlines():
    if not line:
        continue
    for c in line:
        d = m[c]
        if args.part == 1:
            x += di[d]
            y += dj[d]
            x = max(0, min(2, x))
            y = max(0, min(2, y))
        else:
            if 0 <= x + di[d] < 5 and np[x + di[d]][y]:
                x += di[d]
            if 0 <= y + dj[d] < 5 and np[x][y + dj[d]]:
                y += dj[d]
    sol += str(np[x][y])
print(sol)
