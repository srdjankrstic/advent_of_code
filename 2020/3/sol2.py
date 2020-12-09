f = open("input.txt", "r")
contents = f.read()

tree = []
for i, line in enumerate(contents.splitlines()):
    tree.append([])
    for j, c in enumerate(line):
        tree[i].append((c == '#'))

n = len(tree[0])

final = 1
for diff in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    encountered = 0
    y = 0
    for x in range(0, len(tree), diff[1]):
        if tree[x][y]:
            encountered += 1
        y += diff[0]
        y %= n
    final *= encountered

print(final)
