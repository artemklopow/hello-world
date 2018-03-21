import json, sys


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
data = json.loads(sys.stdin.read())
names_list = []
for row_node in data:
    names_list.append(row_node['name'])
    tree[row_node['name']] = row_node['parents']

names_list.sort()
for name in names_list:
    counter = 0
    for again in names_list:
        result = 'No'
        is_it_ancestor(name, again)
        if result == 'Yes':
            counter += 1
    print(name, ':', counter)

