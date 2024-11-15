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
    return 


n, m = map(int, input().split())
arr = list(map(int, input().split()))


# @hw code=end