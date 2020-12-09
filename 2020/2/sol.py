import re

LINE_RE = re.compile(r"^(\d+)-(\d+) (.): (.*)$")

valid = 0
with open("input.txt", "r") as fin:
    for line in fin:
        m = LINE_RE.match(line)
        if not m:
            print(f"wtf: {line}")
            continue
        min = int(m.group(1))
        max = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        if min <= password.count(char) <= max:
            valid += 1
print(valid)
