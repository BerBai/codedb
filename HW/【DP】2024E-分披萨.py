#
# @hw id=2024E lang=python3
#
# 【DP】2024E-分披萨
#

# @hw code=start
def max_lr(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if arr[l] > arr[r]:
        l = (l + 1) % n
    else:
        r = (r + n - 1) % n
    
    if l == r:
        dp[l][r] = arr[l]
    else:
        # 取左边
        left = arr[l] + max_lr((l + 1) % n, r)
        # 取右边
        right = arr[r] + max_lr(l, (r + n - 1) % n)
        dp[l][r] = max(left, right)
    return dp[l][r]
    

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

# dp[l][r] 表示l-r区间取得的最大值
dp = [[-1] * n for _ in range(n)]
ans = 0
for i in range(n):
    ans = max(ans, max_lr((i + 1) % n, (i + n - 1) % n) + arr[i])

print(ans)
# @hw code=end