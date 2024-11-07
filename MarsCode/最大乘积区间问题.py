def solution(n, data):
    tmp = data[0]
    l = r = 1
    ans = {}
    ans[tmp] = [l, r]
    for i in range(1, len(data)):
        if data[i-1] == 0:
            # 避免重复值
            if tmp not in ans:
                ans[tmp] = [l, r]
            tmp = data[i]
            l = r = i + 1
            
        elif tmp < tmp*data[i]:
            r = i + 1
            tmp = tmp * data[i]
            # 避免重复值
            if tmp not in ans:
                ans[tmp] = [l, r]
            
    # 加入末尾数 且 避免重复值
    if tmp not in ans:
        ans[tmp] = [l, r]

    key = max(ans)
    return ans[key]


if __name__ == "__main__":
    print(solution(1, [1024]) == [1, 1])
    print(solution(16, [0, 8, 64, 64, 16, 0, 16, 64, 512, 0, 0, 128, 4, 1, 1024, 0]) == [2, 5])
    print(solution(7, [1, 2, 4, 8, 0, 256, 0]) == [6, 6])
    print(solution(8, [1, 2, 4, 8, 0, 256, 512, 0]) == [6, 7])
    print(solution(7, [1, 2, 4, 8, 0, 256, 512]) == [6, 7])
