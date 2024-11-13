#
# @hw id=2023C lang=python3
#
# 篮球游戏
#

# @hw code=start
ss = input().split(",")
sns = input().split(",")
q = list()
i = 0
ans = str()

for s in ss:
    q.append(s)
    while(len(q) > 0):
        if q[0] == sns[i]:
            q = q[1:]
            i += 1
            ans += "L"
        elif q[-1] == sns[i]:
            q = q[:-1]
            i += 1
            ans += "R"
        else:
            break
if len(ans) == len(sns):
    print(ans)
else:
    print("NO")
# @hw code=end