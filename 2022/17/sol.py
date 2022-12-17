import argparse
import re
from collections import defaultdict, deque
from functools import reduce, cmp_to_key
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json
import sympy.ntheory.factor_ as sf

di = lib.di4
dj = lib.dj4

"""

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

"""

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

class Rock:
    def __init__(self, rtype):
        self.rtype = rtype
        if rtype == 0:
            self.points = {(3, 2), (3, 3), (3, 4), (3, 5)}
        elif rtype == 1:
            self.points = {(3, 3), (4, 2), (4, 3), (4, 4), (5, 3)}
        elif rtype == 2:
            self.points = {(3, 2), (3, 3), (3, 4), (4, 4), (5, 4)}
        elif rtype == 3:
            self.points = {(3, 2), (4, 2), (5, 2), (6, 2)}
        elif rtype == 4:
            self.points = {(3, 2), (3, 3), (4, 2), (4, 3)}


    def translate(self, x, y):
        newp = set()
        for p in self.points:
            newp.add((p[0] + x, p[1] + y))
        self.points = newp


def f1(data, N):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    dirs = []
    for c in lines[0]:
        dirs.append(1 if c == '>' else -1)
    ndirs = len(dirs)

    h = 0
    t = 0
    rstopped = 0
    map = [[0 for _ in range(7)] for __ in range(10000)]
    currock = Rock(0)

    while True:
        if t < 10:
            print(f"time: {t}")
            for i in range(12):
                print("".join(['#' if map[11-i][j] else '@' if (11-i, j) in currock.points else '.' for j in range(7)]))
            print()
        jet = dirs[t % ndirs]
        currock.translate(0, jet)
        for p in currock.points:
            if (not 0 <= p[1] < 7) or map[p[0]][p[1]]:
                currock.translate(0, -jet)
                break

        stopped = False
        currock.translate(-1, 0)
        for p in currock.points:
            if p[0] == -1 or map[p[0]][p[1]]:
                stopped = True
                break
        if stopped:
            currock.translate(1, 0)
            for p in currock.points:
                map[p[0]][p[1]] = 1
                h = max(h, p[0])
            currock = Rock((currock.rtype + 1) % 5)
            currock.translate(h+1, 0)
            rstopped += 1
            if rstopped == N:
                return h + 1
        t += 1
    return sol


def f2(data, N):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    dirs = []
    for c in lines[0]:
        dirs.append(1 if c == '>' else -1)
    ndirs = len(dirs)

    MSIZE = 100000
    scroll = 0
    h = 0
    t = 0
    rstopped = 0
    map = dict()
    for i in range(MSIZE):
        map[i] = [0 for _ in range(7)]
    mset = set(range(MSIZE))
    currock = Rock(0)
    lasth = 0
    diffs = []

    while True:
        # if t < 10:
        #     print(f"time: {t}")
        #     for i in range(12):
        #         print("".join(['#' if map[11-i][j] else '@' if (11-i, j) in currock.points else '.' for j in range(7)]))
        #     print()

        jet = dirs[t % ndirs]
        currock.translate(0, jet)

        for p in currock.points:
            if p[0] not in mset:
                olds = sorted(mset)
                jump = MSIZE//2
                for i in range(jump):
                    del map[olds[i]]
                    map[olds[-1] + i + 1] = [0 for _ in range(7)]
                    mset.remove(olds[i])
                    mset.add(olds[-1] + i + 1)

        for p in currock.points:
            if (not 0 <= p[1] < 7) or map[p[0]][p[1]]:
                currock.translate(0, -jet)
                break

        stopped = False
        currock.translate(-1, 0)
        for p in currock.points:
            if p[0] == -1 or map[p[0]][p[1]]:
                stopped = True
                break
        if stopped:
            currock.translate(1, 0)
            for p in currock.points:
                map[p[0]][p[1]] = p[0] + 1
                h = max(h, p[0] + 1)
            currock = Rock((currock.rtype + 1) % 5)
            currock.translate(h, 0)
            rstopped += 1
            if rstopped == N:
                return h

            diffs.append(h - lasth)
            lasth = h
            if rstopped % 500000 == 0:
                print("testing")
                for chunk_size in range(10, rstopped // 20):
                    repeats = 0
                    chunk_start = len(diffs) - chunk_size
                    while True:
                        new_chunk_start = chunk_start - chunk_size
                        if new_chunk_start < 0:
                            break
                        if any([diffs[new_chunk_start + i] != diffs[chunk_start + i] for i in range(chunk_size)]):
                            break
                        repeats += 1
                        chunk_start = new_chunk_start
                        if repeats > 100:
                            break
                    if repeats > 100:
                        print(f"{repeats}: {chunk_size}")
                        (dd, mm) = divmod((N - rstopped), chunk_size)
                        print(f"{h}, {dd}, {mm}, {sum(diffs[-chunk_size:])}")
                        sol = h + dd * sum(diffs[-chunk_size:])
                        sol += sum(diffs[-chunk_size:]) - sum(diffs[-(chunk_size-mm):])
                        return sol

        t += 1

    return sol

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read(), 2022)}")
elif args.part == 2:
    print(f"solution: {f2(f.read(), 1000000000000)}")
