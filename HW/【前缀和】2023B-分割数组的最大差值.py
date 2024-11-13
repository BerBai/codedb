#
# @hw id=2023B lang=python3
#
# 分割数组的最大差值
#

# @hw code=start
n = int(input())
nums = list(map(int, input().split()))

lsum = 0
rsum = sum(nums)
ans = 0
for i, num in enumerate(nums):
    lsum += num
    rsum -= num
    ans = max(ans, abs(lsum - rsum))
print(ans)
# @hw code=end