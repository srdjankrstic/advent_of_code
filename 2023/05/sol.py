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
    maps = defaultdict(lambda: defaultdict(list))
    X = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

    lines = [line for line in data.splitlines() if line.strip()]
    seeds = lib.rints(lines[0])

    for li, chunk in enumerate(data.split("\n\n")):
        if li == 0:
            continue
        chunk = chunk.splitlines()
        [left, _, right] = chunk[0].split(' ')[0].split('-')
        chunk = chunk[1:]
        for l in chunk:
            [a, b, c] = lib.rints(l)
            maps[left][right].append((a, b, c))

    sol = 999999999999999
    for s in seeds:
        x = s
        for i in range(len(X) - 1):
            for arange in maps[X[i]][X[i + 1]]:
                if arange[1] <= x < arange[1] + arange[2]:
                    x = arange[0] + x - arange[1]
                    break
        sol = min(sol, x)
    return sol

def f2(data):
    range_queue = []
    maps = defaultdict(lambda: defaultdict(list))
    X = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

    lines = [line for line in data.splitlines() if line.strip()]
    seeds = lib.rints(lines[0])

    for li, chunk in enumerate(data.split("\n\n")):
        if li == 0:
            continue
        chunk = chunk.splitlines()
        [left, _, right] = chunk[0].split(' ')[0].split('-')
        chunk = chunk[1:]
        for l in chunk:
            [a, b, c] = lib.rints(l)
            maps[left][right].append((a, b, c))

    for ss in range(0, len(seeds), 2):
        range_queue.append((seeds[ss], seeds[ss] + seeds[ss+1]))

    for x in range(len(X) - 1):
        new_range_queue = []
        for arange in range_queue:
            found = False
            for new_range in maps[X[x]][X[x + 1]]:
                (dest, src, run) = new_range
                remap = (src, src + run)
                fixer = dest - src
                if remap[0] >= arange[1] or remap[1] <= arange[0]:
                    continue
                if arange[0] <= remap[0] and arange[1] >= remap[1]:
                    new_range_queue.append((remap[0] + fixer, remap[1] + fixer))
                    found = True
                    if arange[0] < remap[0]: range_queue.append((arange[0], remap[0]))
                    if remap[1] < arange[1]: range_queue.append((remap[1], arange[1]))
                    continue
                if remap[0] <= arange[0] and remap[1] >= arange[1]:
                    found = True
                    new_range_queue.append((arange[0] + fixer, arange[1] + fixer))
                    continue
                if arange[0] <= remap[0] <= arange[1] <= remap[1]:
                    found = True
                    if arange[0] < remap[0]: range_queue.append((arange[0], remap[0]))
                    if remap[0] < arange[1]: new_range_queue.append((remap[0] + fixer, arange[1] + fixer))
                    continue
                if remap[0] <= arange[0] <= remap[1] <= arange[1]:
                    found = True
                    if arange[0] < remap[1]: new_range_queue.append((arange[0] + fixer, remap[1] + fixer))
                    if remap[1] < arange[1]: range_queue.append((remap[1], arange[1]))
                    continue
            if not found:
                new_range_queue.append(arange)
        range_queue = deepcopy(new_range_queue)

    sol = 9999999999999
    for x in range_queue:
        if x[0]:
            sol = min(sol, x[0])
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
