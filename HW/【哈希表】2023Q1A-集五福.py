#
# @hw id=2023Q1A lang=python3
#
# 集五福
#

# @hw code=start
team = input().split(",")
cnt = [0, 0, 0, 0, 0]
for p in team:
    for i, n in enumerate(p):
        cnt[i] += int(n)
print(min(cnt))
# @hw code=end