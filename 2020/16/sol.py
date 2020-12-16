import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

rules = []
YT = False
NT = False
totalinv = 0
allns = []
myt = []
for li, line in enumerate(lines):
    if ":" in line:
        r = lib.rints(line)
        rules.append((r[0], r[1], r[2], r[3]))
    elif line.startswith("aa"):
        myt = lib.rints(line)
    elif line.startswith("bb"):
        ns = lib.rints(line)
        allns.append(ns)

if args.part == 1:
    for i, ns in enumerate(allns):
        for n in ns:
            valid = False
            for r in rules:
                if r[0] <= n <= r[1] or r[2] <= n <= r[3]:
                    valid = True
            if not valid:
                totalinv += n
    print(totalinv)
else:
    Z = len(rules)
    nscpy = deepcopy(allns)
    for ns in allns:
        for n in ns:
            valid = False
            for r in rules:
                if r[0] <= n <= r[1] or r[2] <= n <= r[3]:
                    valid = True
            if not valid:
                nscpy.remove(ns)
                break
    allns = nscpy

    possible = defaultdict(lambda: True)
    for i, r in enumerate(rules):
        for ns in allns:
            for j in range(len(ns)):
                if not(r[0] <= ns[j] <= r[1] or r[2] <= ns[j] <= r[3]):
                    possible[(i, j)] = False
    # for i in range(Z):
    #     for j in range(Z):
    #         print(f"{'X' if possible[(i, j)] else 'O'}\t", end="")
    #     print("")

    def findr(sofar):
        global Z
        global possible
        s = len(sofar)
        if s == Z:
            print(np.prod([myt[i] for i in range(Z) if sofar[i] < 6]))
            exit(0)
        for i in range(Z):
            if i not in sofar and possible[(i, s)]:
                sofar.append(i)
                findr(sofar)
                sofar.pop()
    findr([])
