#
# @hw id=2024E lang=python3
#
# 火星文计算2
#

# @hw code=start
def cal(x, y, op):
    if op == '$':
        return 2*x+y+3 
    elif op == '#':
        return 4*x+3*y+2 

s = input()
stack = []
flag = False
num = 0

# 字符处理技巧 便于处理最后一个数字 
s += " "

for c in s:
    if c.isdigit():
        num = num*10 + int(c)
    else:
        stack.append(num)
        num = 0
        if flag:
            b = stack.pop()
            a = stack.pop()
            stack.append(cal(a,b,'#'))
        flag = c == '#'

x = stack[0]
for y in stack[1:]:
    x = cal(x, y, '$')

print(x)

# @hw code=end