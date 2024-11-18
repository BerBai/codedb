#
# @hw id=2024E lang=python3
#
# 玩牌高手
#

# @hw code=start
nums = list(map(int, input().split(',')))

n = len(nums)
# 0-n
dp = [0] * (n + 1)
for i in range(n):
    if i < 3:
        if nums[i] + dp[i] < 0:
            dp[i + 1] = 0
        else:
            dp[i + 1] = nums[i] + dp[i]
    else:
        dp[i + 1] = max(dp[i] + nums[i], dp[i - 2])
print(dp[n])
# @hw code=end