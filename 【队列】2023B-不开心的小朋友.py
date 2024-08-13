#
# @hw id=2023B lang=python3
#
# 不开心的小朋友
#

# @hw code=start
n = int(input())
cs = input().split()
wq = list()
state = {}
playNum = 0
angryNum = 0 

for c in cs:
    if c not in state:
        # 0 是否出现 1 是否在玩 2 是否离开
        state[c] = [False, False, False]
    # 第一次出现
    if not state[c][0]:
        # 标记出现
        state[c][0] = True
        if playNum < n:
            # 有空位
            playNum += 1
            state[c][1] = True
        else:
            wq.append(c)
    else:
        # 第二次出现
        state[c][2] = True
        if state[c][1]:
            playNum -= 1
            while playNum < n and len(wq) > 0:
                nc = wq.pop(0)
                if not state[nc][2]:
                    state[nc][1] = True
                    playNum += 1
        else:
            angryNum += 1
print(angryNum)

# @hw code=end