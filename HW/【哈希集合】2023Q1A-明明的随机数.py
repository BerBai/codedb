#
# @hw id=2023Q1A lang=python3
#
# 明明的随机数
#

# @hw code=start
n = int(input())
numset = set()
for i in range(n):
    numset.add(int(input()))

numlist = list(numset)
numlist.sort()

for num in numlist:
    print(num)
# @hw code=end