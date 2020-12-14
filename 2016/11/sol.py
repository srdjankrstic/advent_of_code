import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
from functools import lru_cache


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

allcomps = []
allnames = []

class Component:
    def __init__(self, name, generator):
        self.name = name
        self.gen = generator

    def hash(self):
        return f"{self.name[:3]}{'G' if self.gen else 'M'}"

    def pair(self):
        return Component(name=self.name, generator=not self.gen)

    def __lt__(self, other):
        return self.hash() < other.hash()

    def __eq__(self, other):
        return self.hash() == other.hash()


class State:
    def __init__(self, *, f1 = None, f2 = None, f3 = None, f4 = None, ele=0):
        self.floors = [f1 or [], f2 or [], f3 or [], f4 or []]
        self.ele = ele

    def add(self, floor, comp):
        self.floors[floor].append(comp)

    def move(self, comps, after):
        news = State(
            f1 = deepcopy(self.floors[0]),
            f2 = deepcopy(self.floors[1]),
            f3 = deepcopy(self.floors[2]),
            f4 = deepcopy(self.floors[3]),
            ele = after
        )
        news.floors[self.ele] = [c for c in self.floors[self.ele] if c not in comps]
        for comp in comps:
            if comp not in self.floors[self.ele]:
                raise ValueError("can't do this move")
            news.add(after, comp)
        return news

    def hash(self):
        h = f"E{str(self.ele)}"
        for i in range(4):
            h += " " + str(i) + ": "
            if self.floors[i]:
                h += ",".join([c.hash() for c in sorted(self.floors[i])])
        return h

    def remapped(self, mapping):
        news = State(ele=self.ele)
        for floor in range(4):
            for c in self.floors[floor]:
                newc = Component(mapping[c.name], c.gen)
                news.floors[floor].append(newc)
        return news

    def minhash(self):
        mh = None
        for p in it.permutations(allnames):
            remap = {}
            for i in range(len(p)):
                remap[allnames[i]] = p[i]
            news = self.remapped(remap)
            h = news.hash()
            if not mh or mh > h:
                mh = h
        return mh

    def valid(self):
        for i in range(4):
            if len(self.floors[i]) > 1:
                gens = [x for x in self.floors[i] if x.gen]
                chips = [x for x in self.floors[i] if not x.gen]
                for c in chips:
                    if c.pair() not in gens and len(gens) > 0:
                        return False
        return True

    def reachables(self):
        if self.ele > 0:
            for c in self.floors[self.ele]:
                news = self.move([c], self.ele - 1)
                if news.valid():
                    yield news
            for (c1, c2) in it.combinations(self.floors[self.ele], 2):
                news = self.move([c1, c2], self.ele - 1)
                if news.valid():
                    yield news
        if self.ele < 3:
            for c in self.floors[self.ele]:
                news = self.move([c], self.ele + 1)
                if news.valid():
                    yield news
            for (c1, c2) in it.combinations(self.floors[self.ele], 2):
                news = self.move([c1, c2], self.ele + 1)
                if news.valid():
                    yield news

s = State()
for li, line in enumerate(lines):
    fl = 0
    if "first" in line:
        fl = 0
    elif "second" in line:
        fl = 1
    elif "third" in line:
        fl = 2
    elif "fourth" in line:
        fl = 3
    if "nothing relevant" in line:
        continue

    line = line.replace(", and", " and")
    line = line.replace(" and", ",")
    contents = line.split(",")
    for item in contents:
        w = item.split(" ")
        w[-2] = w[-2].replace("-compatible", "")
        w[-1] = w[-1].replace(".", "")
        comp = Component(w[-2], w[-1] == "generator")
        allcomps.append(comp)
        if comp.name not in allnames:
            allnames.append(comp.name)
        s.add(fl, comp)

final = State(f4=deepcopy(allcomps), ele=3).minhash()

q = [(s, 0)]
seen = set([s.minhash()])

count = 0
while(True):
    if count % 100 == 0:
        print(f"steps: {count}, queue: {len(q)}, depth: {q[0][1]}")
    count += 1
    (cur, n) = q.pop(0)
#    print(cur.hash())
    if cur.minhash() == final:
        print(n)
        break
    for reachable in cur.reachables():
        h = reachable.minhash()
        if h not in seen:
            seen.add(h)
            q.append((reachable, n + 1))
