#
# @hw id=2024E lang=python3
#
# 找到它
#
# @hw code=start
n, m = map(int, input().split())
target = input()
mapc = [[_ for _ in range(m)] for _ in range(n)]

for i in range(n):
    mapc[i] = list(input())


step = [(-1, 0), (1, 0),(0, -1),(0, 1)]

def calBack(i, j, arr, idxarr, isVis):
    if mapc[i][j] == target[len(arr)]:
        # 只标记出发点 防止重复
        if len(arr) == 0:
            isVis[i][j] = True
        arr.appeng(mapc[i][j])
        idxarr.append((i, j))

    if len(arr) == len(target):
        print(f'{idxarr[0][0]} {idxarr[0][1]}')
        exit()

    for s in step:
        x, y = i + s[0], j + s[1]
        if x < 0 or x >= n or y < 0 or y >= m or isVis[x][y]:
            continue
        else:
            calBack(x, y, arr, idxarr, isVis)
            arr.pop()
            idxarr.pop()
if len(target) > n * m:
    print("NO")
else:
    isVis = [[False for _ in range(m)] for _ in range(n)]
    arr = []
    idxarr = []
    calBack(0,0,arr,idxarr,isVis)
    print("NO")

# @hw code=end