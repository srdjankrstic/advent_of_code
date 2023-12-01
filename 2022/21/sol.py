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

    yells = defaultdict(int)
    formula = defaultdict(tuple)
    monks = set()
    for li, line in enumerate(lines):
        w = line.split(' ')
        monk = w[0][:-1]
        monks.add(monk)
        if len(w) == 2:
            yells[monk] = int(w[1])
        else:
            formula[monk] = w[1:4]

    while True:
        if 'root' in yells:
            return yells['root']
        for monk in monks:
            if monk in yells:
                continue
            if formula[monk][0] in yells and formula[monk][2] in yells:
                if formula[monk][1] == '+':
                    yells[monk] = yells[formula[monk][0]] + yells[formula[monk][2]]
                if formula[monk][1] == '-':
                    yells[monk] = yells[formula[monk][0]] - yells[formula[monk][2]]
                if formula[monk][1] == '*':
                    yells[monk] = yells[formula[monk][0]] * yells[formula[monk][2]]
                if formula[monk][1] == '/':
                    yells[monk] = yells[formula[monk][0]] // yells[formula[monk][2]]


def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0

    oyells = defaultdict(int)
    formula = defaultdict(tuple)
    monks = set()
    for li, line in enumerate(lines):
        w = line.split(' ')
        monk = w[0][:-1]
        monks.add(monk)
        if len(w) == 2:
            oyells[monk] = int(w[1])
        else:
            formula[monk] = w[1:4]

    lo = 0
    hi = 100000000000000
    while True:
        mid = (lo + hi) // 2
        for humn in range(mid - 2, mid):
            yells = deepcopy(oyells)
            yells['humn'] = humn
            done = False
            while not done:
                for monk in monks:
                    if monk in yells:
                        continue
                    if formula[monk][0] in yells and formula[monk][2] in yells:
                        if monk == 'root':
                            if yells[formula[monk][0]] == yells[formula[monk][2]]:
                                return humn
                            elif yells[formula[monk][0]] > yells[formula[monk][2]]:
                                lo = humn
                            elif yells[formula[monk][0]] < yells[formula[monk][2]]:
                                hi = humn
                            done = True
                            continue
                        if formula[monk][1] == '+':
                            yells[monk] = yells[formula[monk][0]] + yells[formula[monk][2]]
                        if formula[monk][1] == '-':
                            yells[monk] = yells[formula[monk][0]] - yells[formula[monk][2]]
                        if formula[monk][1] == '*':
                            yells[monk] = yells[formula[monk][0]] * yells[formula[monk][2]]
                        if formula[monk][1] == '/':
                            yells[monk] = yells[formula[monk][0]] // yells[formula[monk][2]]
    return sol

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
