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
cnt = cal_cnt(s[l:r])
while r <= len(s):
    if cnt == tarCnt:
        print(l)
        exit()
    cnt[s[l]] -= 1
    if cnt[s[l]] == 0:
        del cnt[s[l]]

    if r < len(s) and s[r] not in cnt:
        cnt[s[r]] = 1
    elif r < len(s):
        cnt[s[r]] += 1
    
    l += 1
    r += 1

print(-1)
# @hw code=end