#
# @hw id=2023B lang=python3
#
# 数字游戏
#

# @hw code=start
# (sum[j] - nums[i])  = 0
# sum[j] % target = sum[i] % target

n, m = map(int,input().split())
nums = list(map(int,input().split()))
sum = 0
sumSet = set()
sumSet.add(0)
flag = 0
for num in nums:
    sum += num
    if (sum % m) in sumSet:
        flag = 1
        break
    else:
        sumSet.add(sum % m)
print(flag)
# @hw code=end