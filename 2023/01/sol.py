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
    for li, line in enumerate(lines):
        x = []
        for c in line:
            if c >= "0" and c <= "9":
                x.append(int(c))
        sol += 10*x[0] + x[-1]
    return sol


def f2(data):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        x = []
        for i, c in enumerate(line):
            if c >= "0" and c <= "9":
                x.append(int(c))
                continue
            for j, n in enumerate(nums):
                if line[i:i+len(n)] == n:
                    x.append(j + 1)
                    break
        sol += 10*x[0] + x[-1]
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
