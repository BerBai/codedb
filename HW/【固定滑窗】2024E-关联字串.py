#
# @hw id=2024E lang=python3
#
# 关联子串
#

# @hw code=start
target, s = input().split()

def cal_cnt(s):
    cnt = {}
    for i in s:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    return cnt

l, r = 0, len(target)
tarCnt = cal_cnt(target)
while r <= len(s):
    cnt = cal_cnt(s[l:r])
    if cnt == tarCnt:
        print(l)
        exit()
    l += 1
    r += 1
print(-1)
# @hw code=end