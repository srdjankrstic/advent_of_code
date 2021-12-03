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

whatiknow = {
    "children:": 3,
    "cats:": 7,
    "samoyeds:": 2,
    "pomeranians:": 3,
    "akitas:": 0,
    "vizslas:": 0,
    "goldfish:": 5,
    "trees:": 3,
    "cars:": 2,
    "perfumes:": 1,
}

for li, line in enumerate(lines):
    w = line.split(" ")
    ns = lib.rints(line)
    facts = [(w[2], ns[1]), (w[4], ns[2]), (w[6], ns[3])]
    yes = True
    for f in facts:
        if args.part == 1:
            if whatiknow[f[0]] != f[1]:
                yes = False
        else:
            if f[0] in ["cats:", "trees:"]:
                if whatiknow[f[0]] >= f[1]:
                    yes = False
            elif f[0] in ["pomeranians:", "goldfish:"]:
                if whatiknow[f[0]] <= f[1]:
                    yes = False
            elif whatiknow[f[0]] != f[1]:
                yes = False
    if yes:
        print(ns[0])

