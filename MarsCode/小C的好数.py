def solution(n: int) -> int:
    if n <= 100:
        return n
    ans = 100
    for i in range(101, n + 1):
        tmp = i
        cs = {}
        while tmp > 0:
            cs[tmp % 10] = cs.get(tmp % 10, 0) + 1
            tmp = tmp // 10
        if len(cs) <= 2:
            ans += 1
    return ans

if __name__ == '__main__':
    print(solution(110) == 102)
    print(solution(1000) == 352)
    print(solution(1) == 1)