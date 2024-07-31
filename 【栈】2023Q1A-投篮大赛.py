#
# @hw id=2023Q1A lang=python3
#
# 投篮大赛
#

# @hw code=start
ops = input().split(" ")

stack = list()
isErr = False

for s in ops:
    if s!="D" and s!="C" and s!="+":
        stack.append(int(s))
    elif s=="D" and len(stack)>=1:
        stack.append(stack[-1]*2)
    elif s=="+" and len(stack)>=2:
        stack.append(stack[-1] + stack[-2])
    elif s=="C" and len(stack)>=1:
        stack.pop()
    else:
        isErr = True
        break

print(-1 if isErr else sum(stack))
# @hw code=end