from anytree import Node, RenderTree

A = Node("A")
B = Node("B", parent =A)
C = Node("C", parent =A)
D = Node("D", parent = B)
E = Node("E", parent = C, minh = 'deptrai')
F = Node("F", parent = C)
G = Node("G", parent = E)

for pre , fill, node in RenderTree(A):
	print(pre, node.name)
print(G.parent)
print(B.parent.name)
print(A.is_root)