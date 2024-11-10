def solution(n: int, a: list, x: int, y: int) -> bool:
    for i in range(1, n):
        if (a[i-1] == x and a[i] == y) or (a[i-1] == y and a[i] == x):
            return True
    return False
    
if __name__ == '__main__':
    print(solution(4, [1, 4, 2, 3], 2, 4) == True)
    print(solution(5, [3, 4, 5, 1, 2], 3, 2) == False)
    print(solution(6, [6, 1, 5, 2, 4, 3], 5, 2) == True)