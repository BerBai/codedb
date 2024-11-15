#
# @hw id=2024E lang=python3
#
# 磁盘容量
#

# @hw code=start
def calNum(s):
    tmp = 0
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            if c == "G":
                tmp += num * 1024
            elif c == "T":
                tmp += num * 1024 * 1024
            else:
                tmp += num
            num = 0
    return tmp

n = int(input())
arr = []

# 如何处理输入！ 思考清楚很重要
for i in range(n):
    s = input()
    num = calNum(s)
    arr.append((s, num))

arr = sorted(arr, key=lambda x:x[1])
for s, _ in arr:
    print(s)
# @hw code=end