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

z = lib.zarray(1000)
for li, line in enumerate(lines):
    [x1, y1, x2, y2] = lib.rints(line)
    t = line.split(" ")
    if t[:2] == ["turn", "on"]:
        if args.part == 1:
            z[x1:x2+1,y1:y2+1] = lib.zarray([x2-x1+1, y2-y1+1], 1)
        else:
            z[x1:x2+1,y1:y2+1] = np.vectorize(lambda x: x+1)(z[x1:x2+1,y1:y2+1])
    elif t[:2] == ["turn", "off"]:
        if args.part == 1:
            z[x1:x2+1,y1:y2+1] = lib.zarray([x2-x1+1, y2-y1+1], 0)
        else:
            z[x1:x2+1,y1:y2+1] = np.vectorize(lambda x: max(0, x-1))(z[x1:x2+1,y1:y2+1])
    else:
        if args.part == 1:
            z[x1:x2+1,y1:y2+1] = np.vectorize(lambda x: 1-x)(z[x1:x2+1,y1:y2+1])
        else:
            z[x1:x2+1,y1:y2+1] = np.vectorize(lambda x: x+2)(z[x1:x2+1,y1:y2+1])

print(np.sum(z))
