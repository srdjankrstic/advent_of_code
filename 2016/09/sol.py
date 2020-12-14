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
lines = f.read()

def totlen(s):
    i = 0
    inp = False
    last = 0
    totalen = 0
    while(i < len(s)):
        if s[i] == '(' and not inp:
            inp = True
            last = i
        elif s[i] == ')' and inp:
            inp = False
            m = lib.rints(s[last:i])
            if args.part == 1:
                totalen += m[0] * m[1]
            else:
                totalen += m[1] * totlen(s[i+1 : i + m[0] + 1])
            i += m[0]
        elif not inp:
            totalen += 1
        i += 1
    return totalen

for line in lines.splitlines():
    if not line:
        continue
    print(totlen(line))
