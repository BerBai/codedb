#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-BOSS的收入
# 

# @hw code=start
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 构图
dit = {}
# 记录节点收入
values = {}
# 记录节点入度
cnts = {}

for j, i, c in arr:
    if i not in dit:
        dit[i] = [j]
    if j not in dit:
        dit[j] = []
    values[j] = c

vis = [0] * n

def dfs(cur):
    if vis[cur] == 1:
        return
    vis[cur] = 1
    for v in dit[cur]:
        d


# @hw code=end