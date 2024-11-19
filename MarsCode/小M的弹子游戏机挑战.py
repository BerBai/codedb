def solution(n, m, array):
    # dpi,j表示当前位置能得到的最大值 为了便于计算从下往上计算 分两种情况讨论
    dp = [[0] * m for _ in range(n)]
    # 初始化 底部为当前值 -1为0
    dp[n-1] = [item if item != -1 else 0 for item in array[-1]]

    for i in range(n-2,-1,-1):
        for j in range(m):
            # 钉子 计算左下 右上最大值
            if array[i][j] == -1:
                # 注意边界
                if j > 0:
                    dp[i][j] = dp[i+1][j-1]
                if j < m-1:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1])
            elif array[i][j] >= 0:
                # 正值 相加即可
                dp[i][j] = array[i][j] + dp[i+1][j]
    # 最上层中最大值 即为出发点（最大得分）
    return max(dp[0])


if __name__ == "__main__":
    # Add your test cases here
    print(solution(13, 2, [[2,-1],[3,1],[4,4],[1,2],[4,1],[-1,1],[3,1],[0,4],[3,4],[0,4],[1,1],[4,0],[1,-1]]) == 28)
    print(solution(4, 3, [[-1, 0, -1], [0, -1, 0], [50, 100, 70], [80, 200, 50]]) == 130)
