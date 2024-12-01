from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dt = {}
for t, i in arr:
    if t not in dt:
        dt[t] = [i]
    else:
        dt[t].append(i)

time = 0
queue = deque()
vis = []
while time < n:
    if time in dt:
        for i in dt[time]:
            if i not in vis and i not in queue:
                queue.append(i)
    tn = len(queue)
    while tn:
        i = queue.popleft()
        vis.append(i)
        l = (i - 1 + n) % n
        r = (i + 1) % n
        if l not in vis and l not in queue:
            queue.append(l)
        if r not in vis and r not in queue:
            queue.append(r)
        tn -= 1
    if len(vis) + len(queue) == n:
        break
    time += 1
queue.sort()
print(len(queue))
print(' '.join(queue))
        