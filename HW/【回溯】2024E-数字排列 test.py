#
# @hw id=2024E lang=python3
#
# 【回溯】2024E-数字排列
#
# @hw code=start
from collections import Counter

def dfs():
    global nums, n, replace_map, res_list

nums = list(map(int, input().strip().split()))
n = 0
cnts = Counter(nums)
if len(cnts) < len(nums):
    print(-1)
    exit()
for num in nums:
    n = max(n, num)
    if not 0 <= num <= 9:
        print(-1)
        exit()
replace_map = {2: 5, 5: 2, 6: 9, 9: 6}
res_list = []

# @hw code=end