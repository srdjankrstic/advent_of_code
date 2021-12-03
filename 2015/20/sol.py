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
import sympy.ntheory.factor_ as nt

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

n = int(lines[0])
z = n/10 if args.part == 1 else math.ceil(n/11)

if args.part == 1:
    for i in it.count(1):
        if nt.divisor_sigma(i) >= z:
            print(i)
            exit(0)
else:
    totals = defaultdict(int)
    for i in range(1, 1000000):
        for x in range(1, 51):
            totals[x * i] += i
    for i in range(1, 10000000):
        if totals[i] >= z:
            print(i)
            exit(0)
