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
        [winning, mine] = line.split('|')
        winning = winning.split(':')[1]
        wnums = set(lib.rints(winning))
        mysol = 0
        for num in lib.rints(mine):
            if num in wnums:
                if mysol == 0:
                    mysol = 1
                else:
                    mysol *= 2
        sol += mysol
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    copies = defaultdict(int)
    for li, line in enumerate(lines):
        mult = copies[li] + 1
        sol += mult
        [winning, mine] = line.split('|')
        winning = winning.split(':')[1]
        wnums = set(lib.rints(winning))
        i = 0
        for num in lib.rints(mine):
            if num in wnums:
                i += 1
                copies[li+i] += mult
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
