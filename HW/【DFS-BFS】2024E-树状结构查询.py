#
# @hw id=2024E lang=python3
#
# 【DFS/BFS】2024E-树状结构查询
#

# @hw code=start
from collections import deque

# 思考清楚再做题，不要把简单问题复杂化！！
def bfs(query, node_map):
    queue = deque(query)
    ans = []
    while queue:
        cur = queue.popleft()
        if cur not in node_map:
            continue
        for node in node_map[cur]:
            ans.append(node)
            queue.append(node)
    return ans


n = int(input().strip())
node_map = {}
for _ in range(n):
    a, b = input().strip().split()
    if b not in node_map:
        node_map[b] = []
    node_map[b].append(a)

query = input().strip()

ans = bfs(query, node_map)

ans.sort()
for node in ans:
    print(node)

# @hw code=end