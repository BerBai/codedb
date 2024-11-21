#
# @hw id=2024E lang=python3
#
# 找到它
#
# @hw code=start
def findTarget(matrix, target, n, m):
    step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(i, j, idx):
        if idx == len(target):
            return True
        for x, y in step:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == target[idx]:
                if dfs(ni, nj, idx + 1):
                    return True
        return False

    # 字符不重复 找到开始字符 开始搜索
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target[0]:
                if dfs(i, j, 1):
                    # 均从 1 开始
                    return i + 1, j + 1

    return "NO"

n, m = map(int, input().split())
target = input()
matrix = [input().strip() for _ in range(n)]

res = findTarget(matrix, target, n, m)
if res == 'NO':
    print(res)
else:
    print(res[0], res[1])
# @hw code=end