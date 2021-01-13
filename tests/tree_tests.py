import sys
sys.path.append('src')
from tree import *

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

tree = Tree(edges)

tree.build_from_edges()

print("Testing that Tree class works...")
assert tree.root.data == 'e'
assert [node.data for node in tree.root.children]==['g', 'i', 'a'], [node.data for node in tree.root.children]

assert [node.data for node in tree.root.children[0].children]==['b']

assert [node.data for node in tree.root.children[1].children]==[]

assert [node.data for node in tree.root.children[2].children]==['c', 'd']

assert [node.data for node in tree.root.children[0].children[0].children]==[]

assert [node.data for node in tree.root.children[2].children[0].children]==['k']

assert [node.data for node in tree.root.children[2].children[1].children]==['f', 'j']

assert [node.data for node in tree.root.children[2].children[0].children[0].children]==[]

assert [node.data for node in tree.root.children[2].children[1].children[0].children]==['h']

assert [node.data for node in tree.root.children[2].children[1].children[1].children]==[]

assert [node.data for node in tree.root.children[2].children[1].children[0].children[0].children]==[]
print("Passed")

print("Testing breadth_first_search... ")
breadth_first_search = tree.breadth_first_search()
assert [node.data for node in breadth_first_search] == ['e', 'g', 'i', 'a', 'c', 'd', 'b', 'f', 'j', 'k', 'h']
print("Passed")

print("Testing depth_first_search...")
depth_first_search = tree.depth_first_search()
assert [node.data for node in depth_first_search] == ['e', 'a', 'd', 'k', 'j', 'f', 'h', 'b', 'c', 'i', 'g']
print("Passed")