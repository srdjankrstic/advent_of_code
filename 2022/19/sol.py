import argparse
import re
from collections import defaultdict
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

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    ore_robots = []
    clay_robots = []
    obs_robots = []
    geo_robots = []
    for li, line in enumerate(lines):
        x = lib.rints(line)
        ore_robots.append({'ore': x[1]})
        clay_robots.append({'ore': x[2]})
        obs_robots.append({'ore': x[3], 'clay': x[4]})
        geo_robots.append({'ore': x[5], 'obs': x[6]})

    M = 24
    bps = len(ore_robots)
    for b in range(bps):
        print(f"------ {b} ------")
        visited = set()
        q = [(0, (1, 0, 0, 0), (0, 0, 0, 0))]
        visited.add((0, (1, 0, 0, 0), (0, 0, 0, 0)))
        best = 0

        while q:
            state = q.pop(0)
            if state[0] == M:
                if state[2][3] > best:
                    print(state)
                    beststate = state
                best = max(best, state[2][3])
                continue

            if state[1][0] > 4:# or state[1][1] > 6 or state[1][2] > 6:
                continue

            # if state[1][3] > 0:
            #     print(state)

            canbuyall = True
            if state[2][0] >= geo_robots[b]['ore'] and state[2][2] >= geo_robots[b]['obs']:
                newstate = (
                    state[0] + 1,
                    (
                        state[1][0],
                        state[1][1],
                        state[1][2],
                        state[1][3] + 1
                    ),
                    (
                        state[2][0] + state[1][0] - geo_robots[b]['ore'],
                        state[2][1] + state[1][1],
                        state[2][2] + state[1][2] - geo_robots[b]['obs'],
                        state[2][3] + state[1][3]
                    )
                )
                if newstate not in visited:
                    visited.add(newstate)
                    q.append(newstate)
            else:
                canbuyall = False

            if state[2][0] >= obs_robots[b]['ore'] and state[2][1] >= obs_robots[b]['clay']:
                newstate = (
                    state[0] + 1,
                    (
                        state[1][0],
                        state[1][1],
                        state[1][2] + 1,
                        state[1][3]
                    ),
                    (
                        state[2][0] + state[1][0] - obs_robots[b]['ore'],
                        state[2][1] + state[1][1] - obs_robots[b]['clay'],
                        state[2][2] + state[1][2],
                        state[2][3] + state[1][3]
                    )
                )
                if newstate not in visited:
                    visited.add(newstate)
                    q.append(newstate)
            else:
                canbuyall = False

            if state[2][0] >= clay_robots[b]['ore']:
                newstate = (
                    state[0] + 1,
                    (
                        state[1][0],
                        state[1][1] + 1,
                        state[1][2],
                        state[1][3]
                    ),
                    (
                        state[2][0] + state[1][0] - clay_robots[b]['ore'],
                        state[2][1] + state[1][1],
                        state[2][2] + state[1][2],
                        state[2][3] + state[1][3]
                    )
                )
                if newstate not in visited:
                    visited.add(newstate)
                    q.append(newstate)
            else:
                canbuyall = False

            if state[2][0] >= ore_robots[b]['ore']:
                newstate = (
                    state[0] + 1,
                    (
                        state[1][0] + 1,
                        state[1][1],
                        state[1][2],
                        state[1][3]
                    ),
                    (
                        state[2][0] + state[1][0] - ore_robots[b]['ore'],
                        state[2][1] + state[1][1],
                        state[2][2] + state[1][2],
                        state[2][3] + state[1][3]
                    )
                )
                if newstate not in visited:
                    visited.add(newstate)
                    q.append(newstate)
            else:
                canbuyall = False

            if not canbuyall:
                newstate = (
                    state[0] + 1,
                    state[1],
                    (
                        state[2][0] + state[1][0],
                        state[2][1] + state[1][1],
                        state[2][2] + state[1][2],
                        state[2][3] + state[1][3]
                    )
                )
                if newstate not in visited:
                    visited.add(newstate)
                    q.append(newstate)


        print(f"BEST FOR {b + 1}: {best}")
        sol += best * (b + 1)

    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        pass
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
