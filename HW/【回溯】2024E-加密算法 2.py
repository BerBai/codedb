#
# @hw id=2024E lang=python3
#
# 【回溯】2024E-加密算法
#
# @hw code=start

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


# 构建回溯函数，各个参数的含义为
# grid：         原二维矩阵
# M：            原二维矩阵的大小M
# check_list：   大小和grid一样的检查列表，用于判断某个点是否已经检查过
# x,y：          当前在grid中的点的坐标
# s：            待搜索的明文
# s_idx：        待搜索的明文此时遍历到的索引位置
# path：         当前路径
def backtracking(grid, M, check_list, x, y, s, s_idx, path):
    # 声明全局变量isFind
    global isFind
    # 如果在之前的回溯中已经找到了最小字典序的密文，直接返回
    if isFind:
        return
    # 若此时s_idx等于s的长度-1，即len(s)-1
    # 说明s中的所有数字都在grid中找到了
    # 修改isFind为True，输出答案，同时终止递归
    if s_idx == len(s) - 1:
        isFind = True
        print(" ".join(f"{item[0]} {item[1]}" for item in path))
        return
    # 遍历四个方向，获得点(x,y)的近邻点(nx,ny)
    for dx, dy in DIRECTIONS:
        nx, ny = x+dx, y+dy
        # (nx,ny)必须满足以下三个条件，才可以继续进行回溯函数的递归调用
        # 1. 不越界；2. 尚未检查过；
        # 3.在grid中的值grid[nx][ny]为s的下一个字符s[s_idx+1]
        if 0 <= nx < M and 0 <= ny < M and check_list[nx][ny] == False and grid[nx][ny] == s[s_idx+1]:
            # 状态更新：将点(nx,ny)在check_list中的状态更新为True，更新path末尾
            check_list[nx][ny] = True
            path.append((nx, ny))
            # 回溯：将点(nx,ny)传入回溯函数中，注意此时s_idx需要+1
            backtracking(grid, M, check_list, nx, ny, s, s_idx+1, path)
            # 回滚：将点(nx,ny)在check_list中的状态重新修改回False，将path末尾的函数弹出
            check_list[nx][ny] = False
            path.pop()

# 输入明文长度N
N = int(input())
# 输入待查找的明文
s = input().split()
# 输入密码本的行数列数M
M = int(input())
# 构建密码本二维网格
grid = list()
for _ in range(M):
    grid.append(input().split())

# 构建全局变量isFind，初始化为False
isFind = False

# 构建大小和grid一样的检查数组check_list
# 用于避免出现重复检查的情况
check_list = [[False] * M for _ in range(M)]
# 双重遍历整个二维网格grid
for i in range(M):
    for j in range(M):
        # 找到点(i,j)等于s的第一个数字
        # 则点(i,j)可以作为递归的起始位置
        if grid[i][j] == s[0]:
            # 将点(i,j)在check_list中设置为已检查过
            check_list[i][j] = True
            # 回溯函数递归入口，path初始为储存点(i,j)
            backtracking(grid, M, check_list, i, j, s, 0, [(i, j)])
            # 将点(i,j)在check_list中重置为未检查过，因为本次回溯不一定找到答案
            check_list[i][j] = False
            # 如果在回溯中，全局变量isFind被改为True，说明找到了明文，直接退出循环
            if isFind:
                break
    # 关于i的循环同理，找到明文之后直接退出循环
    if isFind:
        break

# 如果最终没找到明文，输出error
if not isFind:
    print("error")

# @hw code=end