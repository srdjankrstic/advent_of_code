import argparse
import re
from collections import defaultdict
from functools import reduce
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json
import sympy.ntheory.factor_

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def solve1(line):
    parens = []
    match = dict()
    for i, c in enumerate(line):
        if c == "(":
            parens.append(i)
        elif c == ")":
            match[parens[-1]] = i
            parens.pop()
    op = None
    val = None
    i = 0
    while i < len(line):
        newval = None
        c = line[i]
        if c in " )":
            i += 1
        elif c in "+*":
            op = c
            i += 1
        elif c == "(":
            newval = solve(line[i+1:match[i]])
            i = match[i] + 1
        elif lib.isint(c):
            newval = int(c)
            i += 1
        if newval is not None:
            if val is None:
                val = newval
            elif op == "+":
                val += newval
            elif op == "*":
                val *= newval
    return val

def solve2(line):
#    print(line)
    parens = []
    match = dict()
    for i, c in enumerate(line):
        if c == "(":
            parens.append(i)
        elif c == ")":
            match[parens[-1]] = i
            parens.pop()

    if len(match) > 0:
        mini = min(match.keys())
        return solve2(line[:mini] + str(solve2(line[mini+1:match[mini]])) + line[match[mini]+1:])
    else:
        m = re.search(r"(\d+) \+ (\d+)", line)
        if not m:
            return reduce(lambda a, b: a*b, lib.rints(line))
        else:
            skip = len(m.group(0))
            start = line.index(m.group(0))
            thissum = int(m.group(1)) + int(m.group(2))
            return solve2(line[:start] + str(thissum) + line[start+skip:])

if args.part == 1:
    print(sum([solve1(line) for line in lines]))
else:
    print(sum([solve2(line) for line in lines]))
