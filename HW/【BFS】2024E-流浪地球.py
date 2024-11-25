#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-流浪地球
#

# @hw code=start
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dt = {}
for t, i in arr:
    if t not in dt:
        dt[t] = [i]
    else:
        dt[t].append(i)

vis = []
time = 0
queue = deque()
while time < n:
    # 点火 入队
    if time in dt:
        for i in dt[time]:
            if i not in vis and i not in queue:
                queue.append(i)
    
    # 同一时间触发的出队
    k = len(queue)
    while k > 0:
        k -= 1
        cur = queue.popleft()
        vis.append(cur)
        l = (cur - 1 + n) % n
        r = (cur + 1) % n
        if l not in vis and l not in queue:
            queue.append(l)
        if r not in vis and r not in queue:
            queue.append(r)
    
    if len(queue) + len(vis) == n:
            break
    time += 1
print(len(queue))
# 输入需要升序排序
queue = sorted(queue)
print(' '.join([str(num) for num in queue]))
# @hw code=end