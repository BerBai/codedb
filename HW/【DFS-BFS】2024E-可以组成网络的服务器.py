#
# @hw id=2024E lang=python3
#
# 【DFS/BFS】2024E-可以组成网络的服务器
# 

# @hw code=start
from collections import deque

def find(n, m, arr):
    queue = deque()
    vis = [[False] * m for _ in range(n)]
    max_m = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                queue.append([i, j])
                vis[i][j] = True
                mm = bfs(queue, n, m, arr, vis)
                max_m = max(max_m, mm)
    return max_m

def bfs(queue, n, m, arr, vis):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ma = 1
    while queue:
        i, j = queue.popleft()
        for x, y in directions:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj] and arr[ni][nj]:
                vis[ni][nj] = True
                ma += 1
                queue.append([ni, nj])
    return ma

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_m = find(n, m, arr)
print(max_m)
# @hw code=end