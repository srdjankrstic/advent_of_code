import re
import math
from functools import reduce
import numpy
from hashlib import md5
import itertools as it

# I/O
def rints(line):
    return [int(x) for x in (re.findall(r'\d+', line) or [])]

def rnints(line):
    return [int(x) for x in (re.findall(r'-?\d+', line) or [])]

def rem(ptr, line):
    return re.match(f"^{ptr}$", line)

def isint(s):
    try:
        int(s)
    except:
        return False
    return True

# MATH
def gcd(*x):
    return math.gcd(*x)

def lcm(*x):
    return math.lcm(*x)

def isprime(num):
    x = int(math.sqrt(num))
    for i in range(2, x + 1):
      if not num % i:
        return False
    return True

def crt(n, a):
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q*x0, x0
        if x1 < 0:
            x1 += b0
        return x1
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# Grid stuff, start north clockwise (N E S W), bottom left is 0, 0
di4 = [0, 1, 0, -1]
dj4 = [1, 0, -1, 0]
di8 = [0, 1, 1, 1, 0, -1, -1, -1]
dj8 = [1, 1, 0, -1, -1, -1, 0, 1]

# Bit stuff
def bin1(x):
    return bin(x)[2:]
def oct1(x):
    return oct(x)[2:]
def hex1(x):
    return hex(x)[2:]

def popcnt(x):
    return bin(x).count('1')

def sumpow2(x):
    r = []
    while x:
        z = x & (x - 1)
        r.append(x - z)
        x = z
    return r

# grid/matrix stuff
def zarray(n, val=0, dtype=int):
    if isint(n):
        n = [n, n]
    return numpy.full(n, val, dtype)

# Random
def hmd5(*c):
    s = "".join([str(x) for x in c])
    return md5(s.encode("utf-8")).hexdigest()

def isiterable(obj):
    try:
        iterator = iter(obj)
    except TypeError:
        return False
    return True  

class Point:
    def __init__(self, *coords):
        if len(coords) > 1:
            self.coords = tuple(coords)
        elif not isiterable(coords[0]):
            raise TypeError
        else:
            self.coords = tuple(coords[0])
        self.dim = len(self.coords)

    def norm(self, _norm=1):
        if _norm == 0:  # Chebyshev, NB different than what normally people think of as L0
            return max([abs(c) for c in self.coords])
        else:
            return sum([abs(c)**_norm for c in self.coords])**(1/_norm)

    def distance(self, other, norm=1):
        if norm == 0:  # Chebyshev, NB different than what normally people think of as L0
            return max([abs(c1 - c2) for c1, c2 in zip(self.coords, other.coords)])
        else:
            return sum([abs(c1 - c2)**norm for c1, c2 in zip(self.coords, other.coords)])**(1/norm)

    def at_l1_dist(self, dist):
        if len(self.coords) != 2:
            for p in self.neigh_l1(dist):
                if self.distance(p) == dist:
                    yield p
        else:
            for x in range(-dist, dist + 1):
                y = dist - abs(x)
                yield Point(self.coords[0] + x, self.coords[1] - y)
                if y:
                    yield Point(self.coords[0] + x, self.coords[1] + y)

    def neigh_hinorm(self, *, norm=2, dist=1, include_self=False):
        deltas = it.product(range(-dist, dist+1), repeat=self.dim)
        for delta in deltas:
            if not include_self and not any(delta):
                continue
            other = Point([c1 + c2 for c1, c2 in zip(self.coords, delta)])
            if 0 <= self.distance(other) <= dist:
                yield other

    # Faster methods for neighbor iterators for norms 0 and 1 without
    # needing to instantiate other point as classes to calculate distance.
    def neigh_cheb(self, dist=1, include_self=False):
        """Chebyshev norm, i.e. max coord diff"""
        deltas = it.product(range(-dist, dist+1), repeat=self.dim)
        for delta in deltas:
            if not include_self and not any(delta):
                continue
            if 0 <= max(abs(axis) for axis in delta) <= dist:
                yield Point([c1 + c2 for c1, c2 in zip(self.coords, delta)])

    def neigh_l1(self, dist=1, include_self=False):
        """L1 norm, i.e. Manhattan"""
        deltas = it.product(range(-dist, dist+1), repeat=self.dim)
        for delta in deltas:
            if not include_self and not any(delta):
                continue
            if 0 <= sum(abs(axis) for axis in delta) <= dist:
                yield Point([c1 + c2 for c1, c2 in zip(self.coords, delta)])

    def __hash__(self):
        return hash(self.coords)

    def __getitem__(self, index):
        return self.coords[index]

    def __repr__(self):
        return repr(self.coords)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("dimension mismatch")
        return Point([c1 + c2 for c1, c2 in zip(self.coords, other.coords)])

    def __sub__(self, other):
        if self.dim != other.dim:
            raise ValueError("dimension mismatch")
        return Point([c1 - c2 for c1, c2 in zip(self.coords, other.coords)])
