#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-流浪地球
#

# @hw code=start
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

arr.sort(key=lambda x: x[0])

queue = deque()
for t, i in arr:
    if t == arr[0][0]:
        queue.append(i)

vis = []
time = 0
while len(queue) > 0:
    time += 1
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
    if time in arr:
        for num in arr[time]:
            if num not in vis and num not in queue:
                queue.append(num)
    if len(queue) + len(vis) == n:
            break
print(len(queue))
print(' '.join([str(num) for num in queue]))
# @hw code=end