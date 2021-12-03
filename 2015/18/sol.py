import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json

di = lib.di8
dj = lib.dj8

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

g = []
for li, line in enumerate(lines):
    g.append([])
    for c in line:
        g[-1].append(True if c == '#' else False)

n = len(g); m = len(g[0])

#STEPS = 5
STEPS = 100

for s in range(STEPS):
    newg = deepcopy(g)
    for i in range(n):
        for j in range(m):
            if args.part == 2 and ((i==0 and j==0) or (i==0 and j==m-1) or (i==n-1 and j==0) or (i==n-1 and j==m-1)):
                newg[i][j] = True
                continue
            num = 0
            for d in range(8):
                pi = i + di[d]; pj = j + dj[d]
                l = False if pi < 0 or pj < 0 or pi >= n or pj >= m else g[pi][pj]
                if l:
                    num +=1
            newg[i][j] = True if (g[i][j] and num in [2, 3]) or (~g[i][j] and num == 3) else False
    g = newg

tot = 0
for i in range(n):
    tot += g[i].count(True)
print(tot)
