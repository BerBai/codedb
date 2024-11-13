def solution(n: int) -> int:
    tmp = n
    ans = 0
    while tmp//2 > 0:
        ans += tmp // 2
        tmp = tmp // 2 + tmp % 2
    return ans

if __name__ == '__main__':
    print(solution(7) == 6)
    print(solution(14) == 13)
    print(solution(1) == 0)