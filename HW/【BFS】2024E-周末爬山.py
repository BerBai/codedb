#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-周末爬山
# 注意输出格式  考虑起点是最高峰的情况

# @hw code=start
from collections import deque

m, n, k = map(int, input().split())
motries = [list(map(int, input().split())) for _ in range(m)]

dic = [(-1, 0), (1, 0), (0, -1), (0, 1)]

step = 0
min_step = 0
max_height = motries[0][0]
vis = [[0] * n for _ in range(m)]

queue = deque()
queue.append([0, 0])
vis[0][0] = 1


while queue:
    step += 1
    l = len(queue)
    while l > 0:
        l -= 1
        ci, cj = queue.popleft()
        for x, y in dic:
            ni, nj = ci + x, cj + y
            if 0 <= ni < m and 0 <= nj < n and not vis[ni][nj] and abs(motries[ni][nj] - motries[ci][cj]) <= k:
                vis[ni][nj] = 1
                queue.append([ni, nj])
                
                if motries[ni][nj] > max_height:
                    min_step = step
                    max_height = motries[ni][nj]

print(f'{max_height} {min_step}')

# @hw code=end