from collections import Counter

def solution(n, max, array):
    # 牌面值映射：A=1, K=13, Q=12, J=11, ..., 2=2
    value_map = {1: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: '10', 9: '9', 8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2'}
    
    # 统计每张牌出现的次数
    count = Counter(array)
    
    # 可能的葫芦组合
    full_houses = []
    
    # 寻找三张相同的牌和两张相同的牌
    for value, cnt in count.items():
        if cnt >= 3:  # 有三张相同的牌
            # 寻找剩下的两张牌
            for value2, cnt2 in count.items():
                if value != value2 and cnt2 >= 2:  # 有两张相同的牌
                    # 计算牌面值之和
                    total_value = value * 3 + value2 * 2
                    if total_value <= max:
                        full_houses.append((value, value2))
    
    # 如果没有找到合法的葫芦，返回 "0, 0"
    if not full_houses:
        return [0, 0]
    
    # 按照规则：先按三张相同牌的大小排序，再按两张相同牌的大小排序 1最大
    full_houses.sort(key=lambda x: (x[0] == 1, x[0], x[1] == 1, x[1]), reverse=True)
    
    # 返回最大的葫芦
    return [full_houses[0][0], full_houses[0][1]]
    
if __name__ == "__main__":
    # Add your test cases here
    print(solution(31, 42, [3,3,11,12,12,2,13,5,13,1,13,8,8,1,8,13,12,9,2,11,3,5,8,11,1,11,1,5,4,2,5]) == [1, 13])
    print(solution(37, 93, [6,5,5,2,5,9,6,6,10,3,9,5,7,12,8,2,3,7,7,11,8,8,9,11,10,7,3,3,10,4,11,11,9,1,1,8,2]) == [11, 1])
    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]) == [8, 5])
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]) == [6, 9])
    print(solution(9, 40, [1, 11, 13, 12, 7, 8, 11, 5, 6]) == [0, 0])
