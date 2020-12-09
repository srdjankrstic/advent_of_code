import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def good(seen_dict, valid):
    if not valid:
        return False
    if len(seen) != len(KEYS):
        return False

    if args.part == 1:
        return True

    # part 2:
    if not re.match(r"^\d{4}$", seen["byr"]):
        return False
    if not 1920 <= int(seen["byr"]) <= 2002:
        return False

    if not re.match(r"^\d{4}$", seen["iyr"]):
        return False
    if not 2010 <= int(seen["iyr"]) <= 2020:
        return False

    if not re.match(r"^\d{4}$", seen["eyr"]):
        return False
    if not 2020 <= int(seen["eyr"]) <= 2030:
        return False

    hgt = re.match(r"^(\d+)(cm|in)$", seen["hgt"])
    if not hgt:
        return False
    if hgt.group(2) == "cm" and not 150 <= int(hgt.group(1)) <= 193:
        return False
    if hgt.group(2) == "in" and not 59 <= int(hgt.group(1)) <= 76:
        return False

    if not re.match(r"^#[0-9a-f]{6}$", seen["hcl"]):
        return False

    if not re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", seen["ecl"]):
        return False

    if not re.match(r"^\d{9}$", seen["pid"]):
        return False
    return True


f = open(args.input, "r")
contents = f.read()
valids = 0

seen = dict()
valid = True
for line in contents.splitlines():
    if not line:
        if good(seen, valid):
            valids += 1
        seen = dict()
        valid = True
        continue
    for item in line.split():
        k, v = item.split(":")
        if k not in KEYS:
            continue
        if seen.get(k):
            valid = False  # double keys invalid?
        seen[k] = v
if good(seen, valid):
    valids += 1

print(valids)
