def solution(values: list) -> int:
    ans = 0
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, values[i] + values[j] + i - j)
    return ans

if __name__ == '__main__':
    print(solution(values=[8, 3, 5, 5, 6]) == 11)
    print(solution(values=[10, 4, 8, 7]) == 16)
    print(solution(values=[1, 2, 3, 4, 5]) == 8)