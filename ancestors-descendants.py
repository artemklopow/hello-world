import sys


def is_it_ancestor(ancestor, descendant):
    global result
    if ancestor == descendant or ancestor in tree[descendant]:
        result = 'Yes'
        return
    if len(tree[descendant]) > 0:
        for i in tree[descendant]:
            is_it_ancestor(ancestor, i)
    return


tree = {}
for _ in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().split(' : ')
    childs = data[0].split()
    if len(data) == 1:
        for child in childs:
            if child not in tree:
                tree[child] = set()
    else:
        parents = data[1].split()
        for child in childs:
            if child not in tree:
                tree[child] = set(parents)
            else:
                tree[child].update(set(parents))


for _ in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().split()
    result = 'No'
    is_it_ancestor(data[0], data[1])
    print(result)
