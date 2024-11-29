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

head_addr, nstr = input().split()
n = int(nstr)
arr = [input().split() for _ in range(n)]

nodes = {}
nexts = {}
for addr, val, next in arr:
    if addr == head_addr:
        cur_key = addr
        head_key = addr
        
    nodes[addr] = LinkedNode(val)
    nexts[addr] = next


while(nexts[cur_key] != '-1'):
    nodes[cur_key].next = nodes[nexts[cur_key]]
    cur_key = nexts[cur_key]

l, f = nodes[head_key], nodes[head_key]
# 出错点1：快慢指针结束条件，需要判断当前 下一个节点
while f and f.next:
    l = l.next
    f = f.next.next

print(l.value)

# @hw code=end