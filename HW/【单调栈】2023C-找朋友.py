#
# @hw id=2023C lang=python3
#
# 找朋友
#

# @hw code=start
n = int(input())
height = list(map(int, input().split()))

stack = list()

ans = [0] * n
for i, h in enumerate(height):
    while len(stack) > 0 and h > height[stack[-1]]:
        top = stack.pop()
        ans[top] = i
    stack.append(i)

print(" ".join(map(str, ans)))
# @hw code=end