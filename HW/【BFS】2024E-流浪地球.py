#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-流浪地球
#

# @hw code=start
n, m = map(int, input().split())
arr = {}
for i in range(m):
    k, v = map(int, input().split())
    if k not in arr:
        arr[k] = [v]
    else:
        arr[k].append(v)

queue = arr[0]

vis = []
time = 0
while len(queue) > 0:

    time += 1
    k = len(queue)
    while k > 0:
        k -= 1
        cur = queue.pop(0)
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