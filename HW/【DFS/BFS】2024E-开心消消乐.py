#
# @hw id=2024E lang=python3
#
# 【【DFS/BFS】2024E-开心消消乐
#

# @hw code=start
from collections import deque

def find(n, m, arr):
    queue = deque()
    vis = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and arr[i][j] == 1:
                queue.append([i, j])
                cnt += 1
                arr[i][j] = 0
                bfs(queue, vis)
    return cnt

def bfs(queue, vis):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    while queue:
        i, j = queue.popleft()
        for x, y in directions:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and vis[ni][nj] == 0 and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                vis[ni][nj] = 1
                queue.append([ni, nj])


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = find(n, m, arr)
print(ans)
# @hw code=end