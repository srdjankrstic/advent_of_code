import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def looknsay(x):
    o = ""
    i = 0
    n = len(x)
    while i < n:
        st = 1
        i += 1
        while i < n and x[i - 1] == x[i]:
            st += 1
            i += 1
        o += str(st) + str(x[i - 1])
    return o

s = lines[0]
for _ in range(40 if args.part == 1 else 50):
    s = looknsay(s)
print(len(s))
