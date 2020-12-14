import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy

di = lib.di4
dj = lib.dj4

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
        g[-1].append(c)

def bfs(x, y):
    sh = []
    for _ in range(len(g)):
        sh.append([None] * len(g[0]))

    seen = set([(x, y)])
    q = [((x, y), 0)]
    while len(q):
        cur = q.pop(0)
        i = cur[0][0]
        j = cur[0][1]
        for d in range(4):
            pi = i + di[d]
            pj = j + dj[d]
            if g[pi][pj] != '#' and (pi, pj) not in seen:
                seen.add((pi, pj))
                sh[pi][pj] = cur[1] + 1
                q.append(((pi, pj), cur[1] + 1))
    return sh

shortest = {}
pos = {}
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j].isdigit():
            pos[g[i][j]] = (i, j)
            shortest[g[i][j]] = bfs(i, j)

best = 1000000000
for p in it.permutations(shortest.keys()):
    if p[0] != '0':
        continue
    total = 0
    for i in range(1, len(p)):
        (ti, tj) = pos[p[i]]
        total += shortest[p[i-1]][ti][tj]
    if args.part == 2:
        total += shortest[p[-1]][pos['0'][0]][pos['0'][1]]
    best = min(best, total)

print(best)
