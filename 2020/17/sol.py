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

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

STEPS = 6
n = len(lines)

if args.part == 1:
    p = defaultdict(bool)
    for li, line in enumerate(lines):
        for i, c in enumerate(line):
            p[(li, i, 0)] = True if c == '#' else False

    for s in range(1, STEPS + 1):
        newp = deepcopy(p)
        for k in range(-s, s+1):
            for i in range(-s, n+s):
                for j in range(-s, n+s):
                    neigh = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            for dk in [-1, 0, 1]:
                                if di == 0 and dj == 0 and dk == 0:
                                    continue
                                pi = i + di
                                pj = j + dj
                                pk = k + dk
                                if p[(pi, pj, pk)]:
                                    neigh += 1
                    newp[(i, j, k)] = True if (p[(i, j, k)] and neigh in [2, 3]) or (~p[(i, j, k)] and neigh == 3) else False
        p = newp
        # print(f"AFTER {s} cycles:")
        # for k in range(-s, s+1):
        #     print(f"z: {k}")
        #     for i in range(-s, n+s):
        #         for j in range(-s, n+s):
        #             if p[(i, j, k)]:
        #                 print("#", end="")
        #             else:
        #                 print(".", end="")
        #         print("")
        #     print("")

    print(sum([1 for x in p.values() if x]))
else:
    p = defaultdict(bool)
    for li, line in enumerate(lines):
        for i, c in enumerate(line):
            p[(li, i, 0, 0)] = True if c == '#' else False

    for s in range(1, STEPS + 1):
        newp = deepcopy(p)
        for k in range(-s, s+1):
            for w in range(-s, s+1):
                for i in range(-s, n+s):
                    for j in range(-s, n+s):
                        neigh = 0
                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                for dk in [-1, 0, 1]:
                                    for dw in [-1, 0, 1]:
                                        if di == 0 and dj == 0 and dk == 0 and dw == 0:
                                            continue
                                        pi = i + di
                                        pj = j + dj
                                        pk = k + dk
                                        pw = w + dw
                                        if p[(pi, pj, pk, pw)]:
                                            neigh += 1
                        newp[(i, j, k, w)] = True if (p[(i, j, k, w)] and neigh in [2, 3]) or (~p[(i, j, k, w)] and neigh == 3) else False
        p = newp

    print(sum([1 for x in p.values() if x]))
