def solution(n, A, B, array_a):
    # 记忆搜索
    memo = {}

    def backtrack(index, sum_a, sum_b):
        if index == n:
            if (sum_a % 10 == A and sum_b % 10 == B):
                return 1
            return 0
        
        # 避免重复计算
        if (index, sum_a, sum_b) in memo:
            return memo[(index, sum_a, sum_b)]

        # 选择当前数字加入第一组
        count_a = backtrack(index + 1, sum_a + array_a[index], sum_b)
        # 选择当前数字加入第二组
        count_b = backtrack(index + 1, sum_a, sum_b + array_a[index])
        
        # 存储计算结果
        memo[(index, sum_a, sum_b)] = count_a + count_b
        return memo[(index, sum_a, sum_b)]

    ans = backtrack(0, 0, 0)

    # 计算特殊情况
    s = sum(array_a)
    if s%10 == A or s%10==B:
        ans += 1
    return ans
    

if __name__ == "__main__":
    print(solution(13, 8, 3, [21,9,16,7,9,19,8,4,1,17,1,10,16]) == 1 )
    print(solution(3, 3, 5, [1,1,1]) == 1 )
    print(solution(2, 1, 1, [1,1]) == 2 )
    print(solution(5, 3, 7, [2, 3, 5, 7, 9]) == 0 )