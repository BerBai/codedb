def solution(n: int) -> int:
    if n <= 100:
        return n
    ans = 100
    for i in range(101, n + 1):
        tmp = i
        digits = set(str(i))
        if len(digits) <= 2:
            ans += 1
    return ans

if __name__ == '__main__':
    print(solution(110) == 102)
    print(solution(1000) == 352)
    print(solution(1) == 1)