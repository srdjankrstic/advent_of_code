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
import sympy.ntheory.factor_ as sf

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def f1():
    sol = 0
    count = []
    for li, line in enumerate(lines):
        l = len(line)
        for i, c in enumerate(line):
            count.append(defaultdict(int))
            count[i][c] += 1
        gamma = int("".join(["1" if count[i]["1"] > count[i]["0"] else "0" for i in range(l)]), 2)
        eps = int("".join(["1" if count[i]["1"] < count[i]["0"] else "0" for i in range(l)]), 2)
        sol = gamma * eps
    return sol

def f2():
    def oxygen(lines, cur = 0):
        if len(lines) == 1:
            return int(lines[0], 2)
        ones = sum([1 if l[cur] == "1" else 0 for l in lines])
        zeroes = len(lines) - ones
        if ones >= zeroes:
            return oxygen([l for l in lines if l[cur] == "1"], cur + 1)
        else:
            return oxygen([l for l in lines if l[cur] == "0"], cur + 1)

    def co2(lines, cur = 0):
        if len(lines) == 1:
            return int(lines[0], 2)
        ones = sum([1 if l[cur] == "1" else 0 for l in lines])
        zeroes = len(lines) - ones
        if ones < zeroes:
            return co2([l for l in lines if l[cur] == "1"], cur + 1)
        else:
            return co2([l for l in lines if l[cur] == "0"], cur + 1)

    return oxygen(deepcopy(lines)) * co2(deepcopy(lines))

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
