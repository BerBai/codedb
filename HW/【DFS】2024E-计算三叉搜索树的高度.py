#
# @hw id=2024E lang=python3
#
# 【DFS】2024E-计算三叉搜索树的高度
#

# @hw code=start
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.mid = None
        self.right = None

def insert(root, value):
    if root == None:
        return Node(value)
    if root.value - 500 > value:
        root.left = insert(root.left, value)
    elif root.value + 500 < value:
        root.right = insert(root.right, value)
    else:
        root.mid = insert(root.mid, value)
    return root

def cal_height(root):
    if root == None:
        return 0
    left = cal_height(root.left)
    mid = cal_height(root.mid)
    right = cal_height(root.right)
    return 1 + max(left, mid, right)

def build_tree(arr):
    root = None
    for i in arr:
        root = insert(root, i)
    height = cal_height(root)
    print(height)


n = int(input())
arr = list(map(int, input().split()))

build_tree(arr)
# @hw code=end