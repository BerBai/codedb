#
# @hw id=2024E lang=python3
#
# 【回溯】2024E-字符串拼接
#
# @hw code=start
from collections import Counter

# 回溯的函数
# path是列表或者字符串均可，这里path选择字符串
def dfs(cnt, path, n):
    global ans
    # path长度已经为n，找到了一个答案
    if len(path) == n:
        ans += 1
        return
    # 横向遍历，考虑字符k以及其剩余个数v
    for k, v in cnt.items():
        # 如果剩余个数为0，或者k和path前一个字符一样，则直接跳过k
        if v == 0 or (path and k == path[-1]):
            continue
        # 状态更新：选择k，所以k的的剩余个数-1
        cnt[k] -= 1
        # 回溯：path的末尾要加上k这个字符来作为新的path
        dfs(cnt, path + k, n)
        # 回滚：把选择的这个k还回去，所以k的剩余个数+1
        cnt[k] += 1

# 有可能存在输入非法的情况，所以使用try-except语句
try:
    # 输入字符串s，答案字符的长度n
    s, n = input().split()
    n = int(n)
    # 使用哈希表统计s种每一个字符出现的次数
    # 显然，s中字符的出现顺序不重要
    cnt = Counter(s)
    # 如果s中的字符出现非小写字母的情况（非法输入），输出0
    # 只有全为小写字母，才可以进行回溯过程
    if all("a" <= k <= "z" for k in cnt):
        ans = 0
        dfs(cnt, "", n)
        print(ans)
    else:
        print(0)
except:
    print(0)

# @hw code=end