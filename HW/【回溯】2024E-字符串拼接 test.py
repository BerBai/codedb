#
# @hw id=2024E lang=python3
#
# 【回溯】2024E-字符串拼接
#
# @hw code=start
from collections import Counter

def dfs(cur_s):
    global ans, n, cnts
    if len(cur_s) == n:
        ans += 1
        return

    for k, v in cnts.items():
        if v == 0 or (cur_s and k == cur_s[-1]):
            continue
        cnts[k] -= 1
        dfs(cur_s + k)
        # 回溯
        cnts[k] += 1

s, n = input().strip().split()
n = int(n)

cnts = Counter(s)

# 处理非法字符
ans = 0
if all('a' <= k <= 'z' for k in cnts):
    dfs('')

print(ans)
# @hw code=end