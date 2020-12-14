import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

#inp = list("abcde")
inp = list("abcdefgh")

def do(inp, line):
    w = line.split(" ")
    if w[0] == "swap":
        if w[1] == "position":
            x = int(w[2])
            y = int(w[-1])
        elif w[1] == "letter":
            x = inp.index(w[2])
            y = inp.index(w[-1])
        t = inp[x]
        inp[x] = inp[y]
        inp[y] = t
    elif w[0] == "reverse":
        [lo, hi] = lib.rints(line)
        s = inp[:lo] + inp[lo:hi+1][::-1] + inp[hi+1:]
        inp = s
    elif w[0] == "rotate":
        if "step" in line:
            n = lib.rints(line)[0]
            if w[1] == "left":
                s = inp[n:] + inp[:n]
            else:
                s = inp[-n:] + inp[:-n]
        else:
            n = inp.index(w[-1])
            if n >= 4:
                n += 2
            else:
                n += 1
            n %= len(inp)
            s = inp[-n:] + inp[:-n]
        inp = s
    elif w[0] == "move":
        [x, y] = lib.rints(line)
        c = inp.pop(x)
        inp.insert(y, c)
    return inp

if args.part == 1:
    for li, line in enumerate(lines):
        inp = do(inp, line)
    print("".join(inp))
elif args.part == 2:
    for z in it.permutations(inp):
        z = list(z)
        save = deepcopy(z)
        for line in lines:
            z = do(z, line)
        if "".join(z) == "fbgdceah":
            print("".join(save))
            break
