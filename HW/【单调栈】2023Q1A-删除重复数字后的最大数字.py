#
# @hw id=2023Q1A lang=python3
#
# 删除重复数字后的最大数字
#

# @hw code=start
s = list(input())
cnt = {}

for c in s:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

used = set()
stack = list()

for c in s:
    if c in used:
        cnt[c] -= 1
    else:
        while len(stack) > 0 and c > stack[-1] and cnt[stack[-1]] > 1:
            oldc = stack.pop()
            cnt[oldc] -= 1
            used.remove(oldc)
        used.add(c)
        stack.append(c)

print("".join(stack))
# @hw code=end