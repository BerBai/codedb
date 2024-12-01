#
# @hw id=2024E lang=python3
#
# 【mem】2024E-分披萨
#

# @hw code=start

# 区间 [l, r] 里，“吃货”能分得的最大披萨大小的总和, t剩余数
def cal_max(l, r, t):
    global arr

    if t <= 1:
        return 0
    
    if mem[l][r][t] != -1:
        return mem[l][r][t]

    # 馋货选最大的
    if arr[l] < arr[r]:
        r = (r + 1) % n
    else:
        l = (l - 1 + n) % n
    
    # 吃货的两种选择
    left = arr[l] + cal_max((l - 1 + n) % n, r, t - 2)
    right = arr[r] + cal_max(l, (r + 1) % n, t - 2)

    mem[l][r][t] = max(left, right)
    return mem[l][r][t]

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 0
mem = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
for i in range(n):
    ans = max(ans, arr[i] + cal_max((i - 1 + n) % n, (i + 1) % n, n - 1))

print(ans)
# @hw code=end