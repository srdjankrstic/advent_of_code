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
    sol = 1
    times = lib.rints(lines[0])
    distances = lib.rints(lines[1])
    n = len(times)
    for i in range(n):
        time = times[i]
        dist = distances[i]
        mysol = 0
        for stop in range(time):
            if (time - stop) * (stop) > dist:
                mysol += 1
        print(mysol)
        sol *= mysol
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 1
    times = lib.rints(lines[0].replace(" ", ""))
    distances = lib.rints(lines[1].replace(" ", ""))
    n = len(times)
    for i in range(n):
        time = times[i]
        dist = distances[i]
        mysol = 0
        for stop in range(time):
            if (time - stop) * (stop) > dist:
                mysol += 1
        print(mysol)
        sol *= mysol
    return sol

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
