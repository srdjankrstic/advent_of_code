import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

g = []
for line in lines.splitlines():
    g.append([])
    gg = g[-1]
    for c in line:
        gg.append(c)

n = len(g)
m = len(g[0])

sol = ""
for j in range(m):
    t = defaultdict(int)
    for i in range(n):
        t[g[i][j]] += 1
    if args.part == 1:
        t = sorted(t.items(), key=lambda x: (-x[1], x[0]))
    else:
        t = sorted(t.items(), key=lambda x: (x[1], x[0]))
    sol += t[0][0]
print(sol)
