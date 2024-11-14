#
# @hw id=2024E lang=python3
#
# 箱子之形摆放
#

# @hw code=start
inarr = input().split(' ')
n = int(inarr[1])
s = inarr[0]
tmp = [[] for _ in range(n)]

i = 0
j = 0
while i < len(s):
    while j < n and i < len(s):
        tmp[j].append(s[i])
        j += 1
        i += 1
    j -= 1
    while j >= 0 and i < len(s):
        tmp[j].append(s[i])
        j -= 1
        i += 1
    j += 1
for item in tmp:
    print(''.join(item))

# @hw code=end