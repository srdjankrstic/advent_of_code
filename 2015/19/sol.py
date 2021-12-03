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

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

final = None
rules = []
for li, line in enumerate(lines):
    x = line.split(" ")
    if len(x) == 1:
        final = x[0]
    else:
        rules.append((x[0], x[2]))

possible = set()

if args.part == 1:
    for r in rules:
        for x in range(len(final) - len(r[0]) + 1):
            if final[x:x+len(r[0])] == r[0]:
                possible.add(final[:x] + r[1] + final[x+len(r[0]):])

    print(len(possible))
else:
    i = 0
    seen = set()
    q = [('e', 0)]
    while True:
        cur = q.pop(0)
        if i % 100000 == 0:
            print(f"round {i}, depth {cur[1]}")
        i += 1
        fin = cur[0]
        for r in rules:
            for x in range(len(fin) - len(r[0]) + 1):
                if fin[x:x+len(r[0])] == r[0]:
                    newm = fin[:x] + r[1] + fin[x+len(r[0]):]
                    if len(newm) > len(final):
                        break
                    if newm == final:
                        print(cur[1] + 1)
                        exit(0)
                    if newm not in seen:
                        seen.add(newm)
                        q.append((newm, cur[1] + 1))
