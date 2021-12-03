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

def f1():
    f = 0
    d = 0
    for li, line in enumerate(lines):
        if line[0] == 'f':
            f += lib.rints(line)[0]
        if line[0] == 'd':
            d += lib.rints(line)[0]
        if line[0] == 'u':
            d -= lib.rints(line)[0]
    return f * d

def f2():
    a = 0
    f = 0
    d = 0
    for li, line in enumerate(lines):
        if line[0] == 'f':
            x = lib.rints(line)[0]
            f += x
            d += a * x
        if line[0] == 'd':
            a += lib.rints(line)[0]
        if line[0] == 'u':
            a -= lib.rints(line)[0]
    return f * d
if args.part == 1:
    print(f1())
elif args.part == 2:
    print(f2())
        