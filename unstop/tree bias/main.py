# Enter your code here. Read input from STDIN. Print output to STDOUT
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def to_string(self):
        return f"{self.left} <- {self.data} -> {self.right} | "

n = int(input())

all_nodes = []
nodes_created = []
for i in range(n-1):
    l = list(map(int, input().split()))
    if l[0] not in nodes_created:
        nodes_created.append(l[0])
        tree_obj = TreeNode(l[0], l[1])
        all_nodes.append(tree_obj)
    else:
        nodes_created.append(l[0])
        for nodes in all_nodes:
            if nodes.data == l[0]:
                nodes.right = l[1]

depth = {}
for node in all_nodes:
    if node.data not in depth:
        depth[node.data] = 0
        depth[node.left] = 1
        depth[node.right] = 1
    else:
        depth[node.left] = depth[node.data] + 1
        depth[node.right] = depth[node.data] + 1

s = 0
for k,v in depth.items():
    if k != None:
        s += v
print(s)