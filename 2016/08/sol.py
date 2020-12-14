import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

def pgr(gr):
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            if gr[i][j]:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")

nn = 6
mm = 50
g = []
for _ in range(nn):
    g.append([False] * mm)
for line in lines.splitlines():
    if not line:
        continue
#    pgr(g)
    gg = deepcopy(g)
    x = line.split(" ")
    if len(x) == 2:
        m, n = x[1].split("x")
        n = int(n); m = int(m)
        for i in range(n):
            for j in range(m):
                gg[i][j] = True
    else:
        if x[1] == "row":
            i = lib.rints(x[-3])[0]
            dj = int(x[-1])
            for j in range(mm):
                pj = (j + dj) % mm
                gg[i][pj] = g[i][j]
        else:
            j = lib.rints(x[-3])[0]
            di = int(x[-1])
            for i in range(nn):
                pi = (i + di) % nn
                gg[pi][j] = g[i][j]
    g = gg
#pgr(g)

sol = 0
for i in range(nn):
    for j in range(mm):
        if g[i][j]:
            sol += 1
print(sol)
pgr(g)
