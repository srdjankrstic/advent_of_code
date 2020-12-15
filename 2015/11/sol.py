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

alphaf = "abcdefghijklmnopqrstuvwxyz"
alpha = "abcdefghjkmnpqrstuvwxyz"

def inc(x):
    for i in reversed(range(len(x))):
        if x[i] == 'z':
            x[i] = 'a'
        else:
            x[i] = alpha[alpha.index(x[i]) + 1]
            return

def v(x):
    sx = "".join(x)
    if not any([alphaf[i:i+3] in sx for i in range(len(alphaf) - 2)]):
        return False
    if not any([p1+p1 in sx and p2+p2 in sx for (p1, p2) in it.combinations(alpha, 2)]):
        return False
    return True

pw = list(lines[0])
while(True):
    inc(pw)
    if v(pw):
        print("".join(pw))
        break
