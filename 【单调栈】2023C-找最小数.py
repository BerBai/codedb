#
# @hw id=2023C lang=python3
#
# 找最小数
#

# @hw code=start
s = list(input())
n = int(input())
stack = list()

for c in s:
    while(len(stack) > 0 and c < stack[-1] and n > 0):
        stack.pop()
        n -= 1
    stack.append(c)

print("".join(stack[0:len(stack)-n]))
# @hw code=end