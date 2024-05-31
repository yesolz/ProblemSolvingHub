import sys

input = sys.stdin.readline

n = int(input().strip())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

root = 'A'


def preorder(tree, node):
    if node == '.':
        return ""
    return node + preorder(tree, tree[node][0]) + preorder(tree, tree[node][1])


def inorder(tree, node):
    if node == '.':
        return ""
    return inorder(tree, tree[node][0]) + node + inorder(tree, tree[node][1])


def postorder(tree, node):
    if node == ".":
        return ""
    return postorder(tree, tree[node][0]) + postorder(tree, tree[node][1]) + node


print(preorder(tree, root))
print(inorder(tree, root))
print(postorder(tree, root))
