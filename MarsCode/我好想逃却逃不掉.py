def solution(N, M, data):
    # 初始化visited数组，表示所有位置都未被访问
    visited = [[False] * M for _ in range(N)]
    
    # 定义一个队列用于BFS
    queue = []
    
    # 找到所有出口位置，并将其加入队列
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'O':
                queue.append((i, j))
                visited[i][j] = True
    
    # BFS遍历
    while queue:
        x, y = queue.pop(0)
        
        # 正向 可以求当前点能走到的位置
        # for dx, dy, direction in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
        # 检查四个方向的传送器(反向)
        for dx, dy, direction in [(-1, 0, 'D'), (1, 0, 'U'), (0, -1, 'R'), (0, 1, 'L')]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 判断当前位置（nx,ny）能否进入(x,y)
                if data[nx][ny] == direction or data[nx][ny] == '.':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    # 统计危险位置 未访问过的位置就是危险位置
    danger_count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                danger_count += 1
    
    return danger_count


if __name__ == "__main__":
    pattern = [ 
        [".", ".", ".", ".", "."], 
        [".", "R", "R", "D", "."], 
        [".", "U", ".", "D", "R"], 
        [".", "U", "L", "L", "."], 
        [".", ".", ".", ".", "O"] ]
    print(solution(5, 5, pattern) == 10)
