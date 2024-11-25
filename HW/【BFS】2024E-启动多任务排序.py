#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-启动多任务排序
# 

# @hw code=start
from collections import deque

ss = input().split()

dit = {}
for s in ss:
    b, a = s.split('->')
    if b not in dit:
        dit[b] = []
    if a not in dit:
        dit[a] = [b]
    else:
        dit[a].append(b)

arr = {}
for k in dit:
    if k not in arr:
        arr[k] = 0
    for v in dit[k]:
        if v not in arr:
            arr[v] = 1
        else:
            arr[v] += 1
# 入度为0的任务
queue = deque(task for task in arr if arr[task] == 0)

# 字典序小的先执行
queue = sorted(queue)

ans = []
while queue:
    cur = queue.popleft()
    ans.append(cur)
    if cur in dit:
        for v in dit[cur]:
            arr[v] -= 1
            if arr[v] == 0:
                queue.append(v)
print(' '.join(ans))
# @hw code=end