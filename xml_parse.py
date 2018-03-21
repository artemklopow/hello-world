import sys
from xml.etree import ElementTree

def count(root, level=1):
    if root.tag == 'cube' and root.attrib['color'] in colours_dict:
        colours_dict[root.attrib['color']] += level
    level += 1
    for child in root:
        count(child, level)

colours_dict = {'red': 0, 'green': 0, 'blue': 0}
root = ElementTree.fromstring(sys.stdin.readline())
count(root, 1)
for i in ['red', 'green', 'blue']:
    print(colours_dict[i])
