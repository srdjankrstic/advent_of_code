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

BASE_SCORES = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
TO_BEAT = {'A': 'B', 'B': 'C', 'C': 'A'}
TO_LOSE = {'A': 'C', 'B': 'A', 'C': 'B'}
OUTCOMES = {
    'X': {'A': 3, 'B': 0, 'C': 6},
    'Y': {'B': 3, 'C': 0, 'A': 6},
    'Z': {'C': 3, 'A': 0, 'B': 6},
}

def score(q, w):
    return BASE_SCORES[w] + OUTCOMES[w][q]

def f1():
    sol = 0
    for li, line in enumerate(lines):
        sol += score(line[0], line[2])
    return sol

def f2():
    sol = 0
    for li, line in enumerate(lines):
        if line[2] == 'X':
            sol += BASE_SCORES[TO_LOSE[line[0]]]
        elif line[2] == 'Y':
            sol += BASE_SCORES[line[0]] + 3
        else:
            sol += BASE_SCORES[TO_BEAT[line[0]]] + 6
    return sol


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
