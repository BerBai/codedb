#
# @hw id=2024E lang=python3
#
# 【回溯】2024E-数字排列
#
# @hw code=start
from collections import Counter

def dfs(path, used):
    global nums, n, replace_map, res_list
    
    if path:
        res_list.append(int(path))
    
    if len(path) == len(nums):
        return
    
    for num in nums:
        if num in used:
            continue
        used.add(num)
        dfs(path + str(num), used)
        # 如果可被替换，且两者均未使用
        if num in replace_map and replace_map[num] not in used:
            dfs(path + str(replace_map[num]), used)

        used.remove(num)

nums = list(map(int, input().strip().split(',')))
n = 0
cnts = Counter(nums)
# 出错点2：不合规输入条件包括2,5和6,9同时出现
if len(cnts) < len(nums) or (2 in cnts and 5 in cnts) or (6 in cnts and 9 in cnts):
    print(-1)
    exit()
for num in nums:
    n = max(n, num)
    # 出错点1： 注意题意的不合规输入 1-9 不包括0
    if not 1 <= num <= 9:
        print(-1)
        exit()
replace_map = {2: 5, 5: 2, 6: 9, 9: 6}
res_list = []

dfs('', set())
if not res_list:
    print(-1)
    exit()

res_list.sort()
nth = min(n, len(res_list))
print(res_list[n-1])

# @hw code=end