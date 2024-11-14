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

step = [[-1, 1], [0, 1], [1, -1], [1, 1]]
# 从[0,j]位置开始的最大相连男生数
cnt = [0] * m




# @hw code=end