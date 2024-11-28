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
n = int(input())
arr = list(map(int, input().split()))

# @hw code=end