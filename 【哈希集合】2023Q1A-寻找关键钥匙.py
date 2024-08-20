#
# @hw id=2023Q1A lang=python3
#
# 寻找关键钥匙
#

# @hw code=start
k = input()
boxes = input().split()

ans = -1
set_k = set(k)
for i, s in enumerate(boxes):
    set_s = {c.lower() for c in s if c.isalpha()}
    if set_k == set_s:
        ans = i + 1
        break
print(ans)
# @hw code=end