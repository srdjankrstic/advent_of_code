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

#DL = 20
DL = 272 if args.part == 1 else 35651584

def flip(s):
    return "".join(["0" if x == "1" else "1" for x in s][::-1])

inp = lines[0]

while len(inp) < DL:
    inp += "0" + flip(inp)
inp = inp[:DL]

out = inp
while len(out) % 2 == 0:
    out = ""
    for i in range(0, len(inp), 2):
        if inp[i] == inp[i+1]:
            out += "1"
        else:
            out += "0"
    inp = out

print(out)
