f = open("input.txt", "r")
contents = f.read()

encountered = 0
tree = []
for i, line in enumerate(contents.splitlines()):
    tree.append([])
    for j, c in enumerate(line):
        tree[i].append((c == '#'))

n = len(tree[0])
y = 0
for x in range(len(tree)):
    if tree[x][y]:
        encountered += 1
    y += 3
    y %= n

print(encountered)
