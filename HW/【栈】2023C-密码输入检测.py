#
# @hw id=2023C lang=python3
#
# 密码输入检测
#

# @hw code=start
stack = list()
s = input()
for c in s:
    if c == '<' and len(stack) >= 1:
        stack.pop()
    elif c != '<':
        stack.append(c)

flag = 0
if any(c.isupper() for c in stack):
    flag |= 0b0001
if any(c.islower() for c in stack):
    flag |= 0b0010
if any(c.isdigit() for c in stack):
    flag |= 0b0100
if any(not c.isalnum() and not c.isspace() for c in stack):
    flag |= 0b1000

if flag == 0b1111 and len(stack) >= 8:
    print("".join(stack)+",true")
else:
    print("".join(stack)+",false")
        
# @hw code=end