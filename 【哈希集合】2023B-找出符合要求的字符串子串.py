#
# @hw id=2023B lang=python3
#
# 找出符合要求的字符串子串
#

# @hw code=start
s1 = set(input())
s2 = set(input())

ans = [c for c in s1 if c in s2]
ans.sort()
print("".join(ans))
# @hw code=end