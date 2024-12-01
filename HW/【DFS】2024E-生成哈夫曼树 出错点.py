#
# @hw id=2024E lang=python3
#
# 【DFS】2024E-生成哈夫曼树
#

# @hw code=start
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
    
    # 出错点1：符号不要写错
    # __eq__：用于重写等号==。
    # __ne__：用于重写不等号!=。
    # __lt__：用于重写小于号<。
    # __le__：用于重写小于等于号<=。
    # __gt__：用于重写大于号>。
    # __ge__：用于重写大于等于号>=。
    def __lt__(self, other):
        if self.value == other.value:
            # 出错点二：注意细节，比较元素不要写错
            return self.height < other.height
        return self.value < other.value

def build_tree(arr):
    node_arr = [Node(i) for i in arr]
    heapq.heapify(node_arr)

    while len(node_arr) > 1:
        # 出错点三：熟悉下heapq的用法
        left = heapq.heappop(node_arr)
        right = heapq.heappop(node_arr)
        parent = Node(left.value + right.value)
        
        parent.left = left
        parent.right = right
        # 出错点四：注意细节，比较高度，不要写错成value
        parent.height = max(left.height, right.height) + 1

        heapq.heappush(node_arr, parent)
    # 返回根节点
    return node_arr[0]

def dfs(root, arr):
    if root == None:
        return
    # 出错点五：注意细节，参数个数
    dfs(root.left, arr)
    arr.append(root.value)
    dfs(root.right, arr)

n = int(input())
arr = list(map(int, input().split()))

root = build_tree(arr)

ans_arr = []
dfs(root, ans_arr)

# 出错点六：注意细节，不要写成arr
print(' '.join(map(str, ans_arr)))
# @hw code=end