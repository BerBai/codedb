#
# @hw id=2024E lang=python3
#
# 货币兑换
#

# @hw code=start
n = int(input())
sarr = []
for i in range(n):
    sarr.append(input())

ans = 0
for s in sarr:
    num = 0
    tmp = ''
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            if c == 'C':
                ans += num * 100
            elif c == 'J':
                ans += num * 100 / 18.25
            elif c == 'H':
                ans += num * 100 / 1.23
            elif c == 'E':
                ans += num * 100 / 0.14
            elif c == 'G':
                ans += num * 100 / 0.12
            elif c == 'f':
                ans += num
            elif c == 'c':
                ans += num / 1.23
            elif c == 's':
                ans += num / 18.25
            elif c == 'e':
                ans += num / 0.14
            elif c == 'p':
                ans += num / 0.12
            num = 0
print(int(ans))

# @hw code=end