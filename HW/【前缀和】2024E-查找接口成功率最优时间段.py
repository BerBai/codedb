#
# @hw id=2024E lang=python3
#
# 查找接口成功率最优时间段
# 是求最长的平均时间段，长度相同时输出多个
#

# @hw code=start
n = int(input())
nums = list(map(int, input().split()))

m = len(nums)
preSum = [0] * (m + 1)

ans = {}

for i in range(m):
    preSum[i + 1] = preSum[i] + nums[i]

# 使用滑动窗口优化
for i in range(m):
    for j in range(i, m):
        subSum = preSum[j + 1] - preSum[i]  # 子数组和
        cnt = j - i + 1
        if subSum / cnt <= n:
            if cnt in ans:
                ans[cnt].append(f'{i}-{j}')
            else:
                ans[cnt] = [f'{i}-{j}']

maxL = max(ans.keys())

print(' '.join(ans[maxL]))



