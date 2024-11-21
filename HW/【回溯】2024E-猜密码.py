#
# @hw id=2024E lang=python3
#
# 猜密码
# 注意对输出的处理 思考如何快速排序！
#
# @hw code=start
nums = list(map(int, input().split(',')))
n = int(input())

m = len(nums)

ans = []
def calPwd(i, arr):
    if len(arr) >= n:
        tmp = arr.copy()
        tmp.sort()
        key = ','.join(map(str, tmp))
        ans.append(key)
    while i < m:
        arr.append(nums[i])
        calPwd(i+1, arr)
        arr.pop()
        i += 1

if n > m:
    print("None")
else:
    calPwd(0, [])

ans.sort()
for num in ans:
    print(num)
# @hw code=end