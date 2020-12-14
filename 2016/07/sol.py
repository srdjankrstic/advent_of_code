import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

def abba(s):
    if len(s) < 4:
        return False
    return s[-4] == s[-1] and s[-3] == s[-2] and s[-1] != s[-2]

def isaba(s):
    if len(s) < 3:
        return False
    return s[-3] == s[-1] and s[-1] != s[-2]

sol = 0
for line in lines.splitlines():
    if not line:
        continue
    if args.part == 1:
        p = 0
        b = False
        hasab = False
        bad = False
        for i, c in enumerate(line):
            if c in '[]':
                p = i + 1
                b = not b
                continue
            if abba(line[p:i+1]):
                if b:
                    bad = True
                    break
                else:
                    hasab = True
        if hasab and not bad:
            sol += 1
    elif args.part == 2:
        p = 0
        b = False
        abas = []
        babs = []
        for i, c in enumerate(line):
            if c in "[]":
                p = i + 1
                b = not b
                continue
            if isaba(line[p:i+1]):
                if b:
                    babs.append(line[i-2:i+1])
                else:
                    abas.append(line[i-2:i+1])
        for aba in abas:
            bab = "".join([aba[1], aba[0], aba[1]])
            if bab in babs:
                sol += 1
                break
print(sol)
