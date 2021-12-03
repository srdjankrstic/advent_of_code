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

def rsum(j):
    if type(j) == int:
        return j
    elif type(j) == dict:
        if "red" in j.values():
            return 0
        else:
            return sum([rsum(x) for x in j.values()])
    elif type(j) == list:
        return sum([rsum(x) for x in j])
    else:
        return 0

for li, line in enumerate(lines):
    if args.part == 1:
        print(sum(lib.rnints(line)))
    else:
        j = json.loads(line)
        print(rsum(j))
