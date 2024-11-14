#
# @hw id=2024E lang=python3
#
# 最大相连男生数
#

# @hw code=start
n, m = map(int, input().split(','))
maparr = [[] for _ in range(n)]
for i in range(n):
    maparr[i] = input().split(',')

step = [(0, 1), (1, 0), (1, 1), (-1, 1)]
max_boys = 0
for i in range(n):
    for j in range(m):
        # 如果当前是男生，检查所有四个方向
        if maparr[i][j] == 'M':
            for dx, dy in step:
                count = 1
                x, y = i + dx, j + dy
                # 一直检查直到越界或者不是男生
                while 0 <= x < n and 0 <= y < m and maparr[x][y] == 'M':
                    count += 1
                    x += dx
                    y += dy
                max_boys = max(max_boys, count)

print(max_boys)
# @hw code=end