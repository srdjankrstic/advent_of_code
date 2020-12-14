import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
contents = f.read()

maxseat = 0
seen = {}
for line in contents.splitlines():
    row = 0
    for c in line[0:7]:
        row *= 2
        if c == "B":
            row += 1

    column = 0
    for c in line[7:10]:
        column *= 2
        if c == "R":
            column += 1

    seat = 8 * row + column
    seen[seat] = True
    if seat > maxseat:
        maxseat = seat

if args.part == 1:
    print(maxseat)
else:
    for seat in range(1, maxseat - 1):
        if not seen.get(seat) and seen.get(seat - 1) and seen.get(seat + 1):
            print(seat)
