def solution(n: int, a: int, b: int) -> int:
    if n < abs(b - a) + 1:
        return -1
    # 二分查找区间
    l, r = max(a, b), max(a, b) + n - 1
    ans = 0
    while l < r:
        # mid 为最高高度
        mid = (l + r) // 2
        # 计算需要的桥墩
        need = abs(mid - a) + abs(mid - b) + 1
        if need <= n:
            l = mid + 1
            # 记录符合条件的高度
            ans = mid
        elif need > n:
            r = mid
    return ans

if __name__ == '__main__':
    print(solution(16, 13, 1) == 14)
    print(solution(9, 12, 2) == -1)
    print(solution(2, 1, 1) == 1)
    print(solution(3, 1, 1) == 2)
    print(solution(5, 3, 2) == 4)
    print(solution(5, 1, 100) == -1)
    print(solution(4, 1, 4) == 4)