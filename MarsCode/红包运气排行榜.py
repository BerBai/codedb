def solution(n: int, s: list, x: list) -> list:
    ans = {}
    # 存在一个人多次抢红包的情况
    for i in range(n):
        if s[i] not in ans:
            ans[s[i]] = [x[i], i]
        else:
            ans[s[i]][0] += x[i]
    # 将字典的值转换为列表并排序
    sorted_values = sorted(ans.items(), key=lambda item: (-item[1][0], item[1][1]))
    
    # 提取排序后的名字
    sorted_names = [name for name, _ in sorted_values]
    
    return sorted_names

if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])