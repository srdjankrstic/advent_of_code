import re

LINE_RE = re.compile(r"^(\d+)-(\d+) (.): (.*)$")

valid = 0
with open("input.txt", "r") as fin:
    for line in fin:
        m = LINE_RE.match(line)
        if not m:
            print(f"wtf: {line}")
            continue
        pos1 = int(m.group(1)) - 1
        pos2 = int(m.group(2)) - 1
        char = m.group(3)
        password = m.group(4)
        if (password[pos1] == char) ^ (password[pos2] == char):
            valid += 1
print(valid)
