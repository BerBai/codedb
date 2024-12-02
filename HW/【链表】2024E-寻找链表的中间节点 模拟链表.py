#
# @hw id=2024E lang=python3
#
# 【链表】2024E-寻找链表的中间节点
#

# @hw code=start
head, n = input().strip().split()
n = int(n)

nodes = {}
for i in range(n):
    addr, data, next = input().strip().split()
    nodes[addr] = [data, next]

s, f = head, head
ans = nodes[s][0]
while f in nodes and nodes[f][1] in nodes:
    s = nodes[s][1]
    f = nodes[f][1]
    f = nodes[f][1]
    ans = nodes[s][0]

print(ans)
# @hw code=end