#
# @hw id=2024E lang=python3
#
# 最短木板长度
#

# @hw code=start

def calMinLen(mid, n, m, arr):
    needLen = 0
    for num in arr:
        if num < mid:
            needLen += mid - num
        if needLen > m:
            return False
    return needLen <= m



n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 二分查找的界限
l, r = 1, max(arr) + m
while l < r:
    # 向上取整
    mid = (l + r + 1) // 2
    if calMinLen(mid, n, m, arr):
        # mid 是一个可能的答案，但是还需要向上继续查找
        l = mid
    else:
        # mid 不是一个可能的答案，需要继续向下查找
        r = mid - 1

print(l)

# @hw code=end