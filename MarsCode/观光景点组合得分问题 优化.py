def solution(values: list) -> int:
    # values[i] + i 
    # values[j] - j
    # 可以通过维护一个变量来记录当前最大的 values[i] + i，
    # 然后在遍历 j 时，直接计算 (values[i] + i) + (values[j] - j) 
    # 并与当前最大值比较。

    ans = 0
    max_i = values[0] # values[i] + i
    for j in range(1, len(values)):
        ans = max(ans, max_i + values[j] - j)
        max_i = max(max_i, values[j] + j)
    return ans

if __name__ == '__main__':
    print(solution(values=[8, 3, 5, 5, 6]) == 11)
    print(solution(values=[10, 4, 8, 7]) == 16)
    print(solution(values=[1, 2, 3, 4, 5]) == 8)