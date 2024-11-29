#
# @hw id=2024E lang=python3
#
# 【前缀和】2024E-分割数组的最大差值
#

# @hw code=start

n = int(input())
nums = list(map(int, input().split()))

pre_sum = [0] * (n + 1)

max_ans = 0
total = sum(nums)
for i in range(n):
    # 出错点1：前缀和！！ presum[i+1] = presum[i] + nums[i]
    # 细节细节，不能浪费时间
    pre_sum[i + 1] = pre_sum[i] + nums[i]
    right_sum = total - pre_sum[i + 1]
    max_ans = max(max_ans, abs(pre_sum[i + 1] - right_sum))

print(max_ans)
# @hw code=end