#
# @hw id=2024E lang=python3
#
# 【链表】2024E-寻找链表的中间节点
#

# @hw code=start
class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def build(head, nodes):
    for node in nodes:
        if 

head_addr, nstr = input().split()
n = int(nstr)
nodes = [input().split() for _ in range(n)]

for addr, val, parent in nodes:
    if addr == head_addr:
        head = LinkedNode(val)

# @hw code=end