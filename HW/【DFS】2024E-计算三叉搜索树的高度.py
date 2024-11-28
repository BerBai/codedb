#
# @hw id=2024E lang=python3
#
# 【DFS】2024E-计算三叉搜索树的高度
#

# @hw code=start
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __lt__(self, other):
        if self.value == other.value:
            return self.height < other.height
        return self.value < other.value

def build_tree(arr):
    node_arr = [Node(i) for i in arr]
    heapq.heapify(node_arr)
    
    while len(node_arr) > 1:
        left = heapq.heappop(node_arr)
        right = heapq.heappop(node_arr)
        parent = Node(left.value + right.value)
        parent.left = left
        parent.right = right
        parent.height = max(left.height, right.height) + 1
        heapq.heappush(node_arr, parent)
    return node_arr[0]

def dfs(root, arr):
    if not root:
        return
    dfs(root.left, ans)
    arr.append(root.value)
    dfs(root.right, ans)

n = int(input())
arr = list(map(int, input().split()))

root = build_tree(arr)
ans = []
dfs(root, ans)
print(" ".join(map(str, ans)))

# @hw code=end