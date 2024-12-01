#
# @hw id=2024E lang=python3
#
# 【DFS/BFS】2024E-树状结构查询
#

# @hw code=start
"""
1.处理数据
2.找开始点
3.bfs 求目标位置信号
"""
from collections import deque

def bfs(n, m, start, map_arr, target):
    dirc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    queue.append(start)
    vis = [[False] * m for _ in range(n)]
    vis[start[0]][start[1]] = True
    ans = map_arr[start[0]][start[1]]
    while queue:
        l = len(queue)
        ans -= 1
        while l:
            i, j = queue.popleft()
            for x, y in dirc:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m and map_arr[ni][nj] != -1 and not vis[ni][nj]:
                    if target == [ni, nj]:
                        return ans
                    queue.append([ni, nj])
                    vis[ni][nj]= True
            l -= 1
    # 出错点：不可达情况下，根据题意返回。 切记不要自己定义！！ 注意审题
    return 0
            


n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
target = list(map(int, input().strip().split()))

map_arr = []
for i in range(n):
    j = (i + 1) * m
    map_arr.append(arr[i * m: j])

ans = -1
for i in range(n):
    for j in range(m):
        if map_arr[i][j] > 0:
            ans = bfs(n, m, [i, j], map_arr, target)
print(ans)
# @hw code=end