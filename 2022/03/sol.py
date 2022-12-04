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

def priority(c):
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

def f1():
    sol = 0
    for li, line in enumerate(lines):
        n = len(line) // 2
        l1 = line[0:n]
        l2 = line[n:2*n]
        ls1 = set()
        for c in l1:
            ls1.add(c)
        for c in l2:
            if c in ls1:
                sol += priority(c)
                break
    return sol

def f2():
    sol = 0
    c = 0
    rucks = []
    for li, line in enumerate(lines):
        c += 1
        rucks.append(set([c for c in line]))
        if c % 3 == 0:
            for i in rucks[0]:
                if i in rucks[1] and i in rucks[2]:
                    sol += priority(i)
                    break
            rucks = []

    return sol


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
