#
# @hw id=2024E lang=python3
#
# 德州扑克
#

# @hw code=start
# 导入所需的模块
import sys

def find_longest_subarray_length(numbers, target_sum):
    start = 0  # 初始化起始指针
    current_sum = 0  # 当前窗口的和
    max_length = -1  # 最长子序列的长度，初始为-1

    # 遍历数组，end为结束指针
    for end in range(len(numbers)):
        current_sum += numbers[end]  # 将当前元素加入窗口和

        # 当当前和大于目标和时，移动start指针缩小窗口
        while current_sum > target_sum and start <= end:
            current_sum -= numbers[start]  # 从窗口和中减去start指针指向的元素
            start += 1  # 移动start指针

        # 如果当前和等于目标和，更新最长子序列长度
        if current_sum == target_sum:
            max_length = max(max_length, end - start + 1)

    return max_length  # 返回结果

def main():
    # 读取5行输入，每行包括牌大小和花色
    cards = []
    for _ in range(5):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        rank, suit = line.split()
        cards.append((rank, suit))

    # 定义牌大小映射
    rank_map = {'J':11, 'Q':12, 'K':13, 'A':14}

    # 转换牌大小为数值
    numeric_cards = []
    for rank, suit in cards:
        if rank in rank_map:
            numeric_rank = rank_map[rank]
        else:
            numeric_rank = int(rank)
        numeric_cards.append((numeric_rank, suit))

    # 按照数值升序排序
    numeric_cards.sort(key=lambda x: x[0])

    # 初始化变量
    same_color = True  # 同花
    dragon = True  # 顺子
    four_kind = False  # 四条
    three_kind = False  # 三条
    two_kind = False  # 对子

    # 统计每种牌大小的出现次数
    rank_counts = {}
    for i in range(5):
        rank, suit = numeric_cards[i]
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

        if i < 4:
            next_rank = numeric_cards[i+1][0]
            next_suit = numeric_cards[i+1][1]
            # 判断顺子
            if dragon and (rank + 1) != next_rank:
                dragon = False
            # 判断同花
            if same_color and suit != next_suit:
                same_color = False

    # 特殊处理A2345
    if numeric_cards[0][0] == 2 and numeric_cards[1][0] == 3 and numeric_cards[2][0] == 4 and numeric_cards[3][0] == 5 and numeric_cards[4][0] == 14:
        dragon = True

    # 判断四条、三条和对子
    for count in rank_counts.values():
        if count == 4:
            four_kind = True
        elif count == 3:
            three_kind = True
        elif count == 2:
            two_kind = True

    # 判断牌型
    if dragon and same_color:
        result = 1  # 同花顺
    elif four_kind:
        result = 2  # 四条
    elif three_kind and two_kind:
        result = 3  # 葫芦
    elif same_color:
        result = 4  # 同花
    elif dragon:
        result = 5  # 顺子
    elif three_kind:
        result = 6  # 三条
    else:
        result = -1  # 无符合牌型

    # 输出结果
    print(result)

if __name__ == "__main__":
    main()


# @hw code=end
