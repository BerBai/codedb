#
# @hw id=2024E lang=python3
#
# 【DP】2024E-分披萨
#

# @hw code=start
from functools import cache

n = int(input())
pizza = list(int(input()) for _ in range(n))

# 对函数参数、返回值进行缓存
@cache
def f(l: int, r: int, t: int) -> int:
    """
    :param l: 左边界
    :param r: 右边界
    :param t: 剩余次数
    :return: 返回 “吃货” 最优选择时可以分到的披萨总和
    """
    global n, pizza
    if t <= 1:
        return 0

    l, r = (l + n) % n, r % n

    # “馋嘴”选择最大的一块
    if pizza[l] >= pizza[r]:
        l = (l - 1 + n) % n
    else:
        r = (r + 1) % n
	
    # “吃货”选择 pizza[l]
    s1 = pizza[l] + f(l - 1, r, t - 2)
    # “吃货”选择 pizza[r]
    s2 = pizza[r] + f(l, r + 1, t - 2)
    return max(s1, s2)

ans = 0
for i in range(n):
    ans = max(ans, pizza[i] + f(i-1, i + 1, n - 1))

print(ans)
# print(max(pizza[i] + f(i - 1, i + 1, n - 1) for i in range(n)))
# @hw code=end