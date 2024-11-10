def solution(m: int, w: list) -> int:
    menus = {}
    ans = 0
    for item in w:
        if item <= m:
            menus[item] = menus.get(item, 0) + 1
            ans = max(ans, menus[item])    
    return ans

if __name__ == '__main__':
    print(solution(6, [2, 3, 3, 6, 6, 6, 9, 9, 23]) == 3)
    print(solution(4, [1, 2, 4, 4, 4]) == 3)
    print(solution(5, [5, 5, 5, 5, 6, 7, 8]) == 4)