#
# @hw id=2024E lang=python3
#
# 找到它
#
# @hw code=start
def find_word(matrix, word, N, M):
    # 方向数组，分别表示上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 检查当前位置是否能继续匹配单词
    def dfs(i, j, idx):
        if idx == len(word):  # 如果已经找到完整的单词
            return True
        
        # 试探四个方向
        for di, dj in directions:
            ni, nj = i + di, j + dj
            # 检查新位置是否越界以及是否匹配字母
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == word[idx]:
                # 继续搜索
                if dfs(ni, nj, idx + 1):
                    return True
        return False

    # 遍历整个矩阵寻找起始点
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == word[0]:  # 找到匹配的第一个字母
                if dfs(i, j, 1):  # 继续从这个位置往四个方向搜索
                    return i + 1, j + 1  # 返回1-based坐标

    return "NO"

n, m = map(int, input().split())
target = input()
matrix = [input().strip() for _ in range(n)]
res = find_word(matrix, target, n, m)
if res == 'NO':
    print(res)
else:
    print(res[0], res[1])

# @hw code=end