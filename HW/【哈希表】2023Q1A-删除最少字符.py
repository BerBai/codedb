#
# @hw id=2023Q1A lang=python3
#
# 删除最少字符
#

# @hw code=start
s = input()
cnt = [float('inf')] * 26
for c in s:
    i = ord(c) - ord('a')
    if cnt[i] == float('inf'):
            cnt[i] = 0
    cnt[i] += 1
mn = min(cnt)
ans = ''
for c in s:
    i = ord(c) - ord('a')
    if cnt[i] > mn:
        ans += c
if ans == '':
    print('empty')
else:
    print(ans)
# @hw code=end