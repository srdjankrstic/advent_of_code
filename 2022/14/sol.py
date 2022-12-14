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
    maxy = 0
    grid = lib.zarray(600)
    for li, line in enumerate(lines):
        coords = lib.rints(line)
        for i in range(0, len(coords) - 2, 2):
            x1 = coords[i]; y1 = coords[i+1]
            x2 = coords[i+2]; y2 = coords[i+3]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[x1, y] = 1
            else:
                maxy = max(maxy, y1)
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[x, y1] = 1
    grid[500, 0] = 2
    sand = 0
    while True:
        x = 500
        y = 0
        while True:
            if y > maxy:
                break
            if grid[x, y + 1] == 0:
                y += 1
                continue
            if grid[x - 1, y + 1] == 0:
                x -= 1; y += 1
                continue
            if grid[x + 1, y + 1] == 0:
                x += 1; y += 1
                continue
            break
        if y > maxy:
            break
        grid[x, y] = 2
        sand += 1
    return sand

def f2(data):
    MAX = 800
    lines = [line for line in data.splitlines() if line.strip()]
    maxy = 0
    grid = lib.zarray(MAX)
    for li, line in enumerate(lines):
        coords = lib.rints(line)
        for i in range(0, len(coords) - 2, 2):
            x1 = coords[i]; y1 = coords[i+1]
            x2 = coords[i+2]; y2 = coords[i+3]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[x1, y] = 1
            else:
                maxy = max(maxy, y1)
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[x, y1] = 1
    for x in range(0, MAX):
        grid[x, maxy + 2] = 1

    grid[500, 0] = 2
    sand = 0
    while True:
        x = 500
        y = 0
        while True:
            if grid[x, y + 1] == 0:
                y += 1
                continue
            if grid[x - 1, y + 1] == 0:
                x -= 1; y += 1
                continue
            if grid[x + 1, y + 1] == 0:
                x += 1; y += 1
                continue
            break
        if x == 500 and y == 0:
            break
        grid[x, y] = 2
        sand += 1
    return sand + 1


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
