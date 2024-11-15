#
# @hw id=2024E lang=python3
#
# 最短木板长度
#

# @hw code=start

n, m = map(int, input().split())
arr = list(map(int, input().split()))

tmp = {}
minNum = int(1e6)
for num in arr:
    if num < minNum:
        minNum = num
    if num in tmp:
        tmp[num] += 1
    else:
        tmp[num] = 1

while m >= tmp[minNum]:
    m -= tmp[minNum]
    tmp[minNum + 1] += tmp[minNum]
    
    tmp[minNum] = 0
    minNum += 1

print(minNum)

# @hw code=end