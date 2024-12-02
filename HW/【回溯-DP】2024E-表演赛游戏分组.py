#
# @hw id=2024E lang=python3
#
# 【回溯/DP】2024E-表演赛游戏分组
#
# @hw code=start
import sys

ans = sys.maxsize

def dfs(idx, cur_total, cnt):
    global nums, total, target, ans

    # 优化 减枝
    if cur_total > target:
        return

    if cnt == 5:
        ans = min(ans, abs(total - 2 * cur_total))
        return
    
    if idx == 10:
        return
    # 分到当前组
    dfs(idx + 1, cur_total + nums[idx], cnt + 1)
    # 不发到当前组
    dfs(idx + 1, cur_total, cnt)


nums = list(map(int, input().strip().split()))
total = 0
for num in nums:
    total += num
target = total // 2

dfs(0, 0, 0)

print(ans)

# @hw code=end