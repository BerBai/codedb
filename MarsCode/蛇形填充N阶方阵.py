def solution(n: int) -> list:
    # 用0表示未访问
    ans = [[0] * n for _ in range(n)]
    # 下 左 上 右
    step = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    i, j = 0, n - 1
    # 先往下填充
    stepI = 0
    for num in range(1, n * n + 1):
        ans[i][j] = num
        x, y = step[stepI]
        nextI = i + x
        nextJ = j + y
        # 调转方向
        if not (0 <= nextI < n and 0 <= nextJ < n and ans[nextI][nextJ] == 0):
            stepI = (stepI + 1) % 4
            x, y = step[stepI]
            nextI = i + x
            nextJ = j + y
        i, j = nextI, nextJ
    return ans

if __name__ == '__main__':
    print(solution(4) == [[10, 11, 12, 1], [9, 16, 13, 2], [8, 15, 14, 3], [7, 6, 5, 4]])
    print(solution(5) == [[13, 14, 15, 16, 1], [12, 23, 24, 17, 2], [11, 22, 25, 18, 3], [10, 21, 20, 19, 4], [9, 8, 7, 6, 5]])
    print(solution(3) == [[7, 8, 1], [6, 9, 2], [5, 4, 3]])