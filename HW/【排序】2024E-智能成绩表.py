#
# @hw id=2024E lang=python3
#
# 【排序】2024E-智能成绩表
#

# @hw code=start
import sys

n, m = map(int, input().split())
sc = input().split()
arr = []
i = 0
sort_by = None
for line in sys.stdin:
    line = line.strip()
    if i < n:
        arr.append(line.split())
    else:
        # 出错点1：处理多行输入。这一行可能没有输入！！
        sort_by = line
    i += 1
    

nums = []
for i in range(n):
    total = 0
    tmp_arr = [arr[i][0]]
    for j in range(1, m + 1):
        tmp = int(arr[i][j])
        total += tmp
        tmp_arr.append(tmp)
    tmp_arr.append(total)
    nums.append(tmp_arr)

if sort_by not in sc:
    nums.sort(key= lambda x: (-x[-1], x[0]))
else:
    idx =  sc.index(sort_by)
    nums.sort(key=lambda x: (-x[idx + 1], x[0]))

print(' '.join([item[0] for item in nums]))

# @hw code=end