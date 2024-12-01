#
# @hw id=2024E lang=python3
#
# 【DFS/BFS】2024E-树状结构查询
#

# @hw code=start
# 1.处理数据
# 2.两个出发点
# 3.记录可达2 点 两人并集
from collections import deque

def bfs(n, m, start, map_arr):
    queue = deque()
    queue.append(start)
    vis = [[False] * m for _ in range(n)]
    dirc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    save_points = []
    while queue:
        i, j = queue.popleft()
        for x, y in dirc:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and map_arr[ni][nj] != 1 and not vis[ni][nj]:
                if map_arr[ni][nj] == 3:
                    save_points.append([ni, nj])
                queue.append([ni, nj])
                vis[ni][nj] = True
    return save_points

n, m = map(int, input().strip().split())
map_arr = [list(map(int, input().strip().split())) for _ in range(n)]


points = []
for i in range(n):
    for j in range(m):
        if map_arr[i][j] == 2:
            tmp = bfs(n, m, [i, j], map_arr)
            points.append(tmp)

ans = 0
for i in points[0]:
    if i in points[1]:
        ans += 1

print(ans)


# @hw code=end