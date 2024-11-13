def solution(m, n, target, array):
    # 初始化字母差异值字典
    diff_dict = {
        'A': {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': float('inf')},
        'B': {'A': 1, 'B': 0, 'C': 1, 'D': float('inf'), 'E': float('inf')},
        'C': {'A': 2, 'B': 1, 'C': 0, 'D': 1, 'E': float('inf')},
        'D': {'A': 3, 'B': float('inf'), 'C': 1, 'D': 0, 'E': 1},
        'E': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 1, 'E': 0}
    }
    ans = {}
    # 初始化最小差异值和最佳匹配士兵
    min_diff = float('inf')
    best_match = None
    
    # 遍历每个候选士兵
    for soldier in array:
        total_diff = 0
        incompatible = False
        
        # 计算每个维度的差异值
        for i in range(m):
            diff = diff_dict[target[i]][soldier[i]]
            if diff == float('inf'):
                incompatible = True
                break
            total_diff += diff
        
        # 如果存在不相容性格类型，跳过该士兵
        if incompatible:
            continue
        
        # 更新最小差异值和最佳匹配士兵
        if total_diff <= min_diff:
            min_diff = total_diff
            best_match = soldier
            # 最佳人选存在多个，记录
            if total_diff not in ans:
                ans[total_diff] = []
            ans[total_diff].append(''.join(soldier))
    # 如果best_match为空，则表示不存在最佳匹配士兵
    return ' '.join(ans[min_diff]) if best_match else 'None'


if __name__ == "__main__":
    # Add your test cases here
    matrix = [
        # ["A", "B", "C", "D", "E", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["B", "B", "B", "B", "B", "B"],
        ["A", "B", "D", "D", "E", "B"],
    ]
    print(solution(6, 3,"ABCDEA", matrix) == "ABDDEB")
    matrix = ["ACDC","BBDC","EBCB","BBBB"]
    print(solution(4, 4,"AEBC", matrix) == "None")
