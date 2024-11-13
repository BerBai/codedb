def solution(n: int, nums: list) -> int:
    # 移除重复元素
    nums.sort(reverse = True)
    tmps = []
    for num in nums:
        if num not in tmps:
            tmps.append(num)
    # 按照题意筛选结果
    if len(tmps) >= 3:
        return tmps[2]
    return max(tmps)

if __name__ == '__main__':
    print(solution(3, [3, 2, 1]) == 1)
    print(solution(2, [1, 2]) == 2)
    print(solution(4, [2, 2, 3, 1]) == 1)