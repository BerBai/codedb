#
# @hw id=2023Q1A lang=python3
#
# 括号检查
#

# @hw code=start
s = input()
isErr = False
depth, maxDepth = 0, 0
if len(s) % 2 == 1:
    isErr = True
else:
    stack = list()
    for c in s:
        if(c == '(' or c == '{' or c == '['):
            stack.append(c)
            depth += 1
            maxDepth = max(depth, maxDepth)
        else:
            if len(stack) == 0:
                isErr = True
                break
            cl = stack.pop()
            depth -= 1
            if (c == ')' and cl != '(') or (c == '}' and cl != '{') or (c == ']' and cl != '['):
                isErr = True
                break
    if len(stack) > 0:
        isErr = True
print(0 if isErr else maxDepth)
# @hw code=end