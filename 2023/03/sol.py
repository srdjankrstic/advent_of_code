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

def isdigit(c):
    return c >= '0' and c <= '9'

def issymbol(c):
    return c != '.' and not isdigit(c)

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        n = len(line)
        i = 0
        while i < n:
            if isdigit(line[i]):
                good = False
                if i > 0:
                    if issymbol(line[i - 1]):
                        good = True
                    if li > 0 and issymbol(lines[li-1][i-1]):
                        good = True
                    if li < len(lines) - 1 and issymbol(lines[li+1][i-1]):
                        good = True
                j = i
                while j < n and isdigit(line[j]):
                    if li > 0 and issymbol(lines[li-1][j]):
                        good = True
                    if li < len(lines) - 1 and issymbol(lines[li+1][j]):
                        good = True
                    j += 1
                if j < n:
                    if issymbol(line[j]):
                        good = True
                    if li > 0 and issymbol(lines[li-1][j]):
                        good = True
                    if li < len(lines) - 1 and issymbol(lines[li+1][j]):
                        good = True
                number = lib.rints(line[i:j])[0]
                i = j
                if good:
                    sol += number
            else:
                i += 1
    return sol


def isgear(c):
    return c == '*'

gears = defaultdict(list)

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        n = len(line)
        i = 0
        while i < n:
            if isdigit(line[i]):
                gears_to_add = []
                if i > 0:
                    if isgear(line[i - 1]):
                        gears_to_add.append(lib.Point(li, i-1))
                    if li > 0 and isgear(lines[li-1][i-1]):
                        gears_to_add.append(lib.Point(li-1, i-1))
                    if li < len(lines) - 1 and isgear(lines[li+1][i-1]):
                        gears_to_add.append(lib.Point(li+1, i-1))
                j = i
                while j < n and isdigit(line[j]):
                    if li > 0 and isgear(lines[li-1][j]):
                        gears_to_add.append(lib.Point(li-1, j))
                    if li < len(lines) - 1 and isgear(lines[li+1][j]):
                        gears_to_add.append(lib.Point(li+1, j))
                    j += 1
                if j < n:
                    if isgear(line[j]):
                        gears_to_add.append(lib.Point(li, j))
                    if li > 0 and isgear(lines[li-1][j]):
                        gears_to_add.append(lib.Point(li-1, j))
                    if li < len(lines) - 1 and isgear(lines[li+1][j]):
                        gears_to_add.append(lib.Point(li+1, j))
                number = lib.rints(line[i:j])[0]
                i = j
                for gear in gears_to_add:
                    gears[gear].append(number)
            else:
                i += 1
    for gear in gears:
        if len(gears[gear]) == 2:
            sol += gears[gear][0] * gears[gear][1]
    return sol

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
