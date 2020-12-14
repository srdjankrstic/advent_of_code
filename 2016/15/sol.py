import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

n = []; a = []
for li, line in enumerate(lines):
    ns = lib.rints(line)
    n.append(ns[1])
    a.append((-ns[0] - ns[-1]) % ns[1])

print(lib.crt(n, a))
