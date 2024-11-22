def solution(n, k, data):
    # 贪心记录最小花费
    min_cost = 0
    # 因为要最小花费 所以往前获取食物的最小费用 长度保持在k 在往前够不着了
    food_queue = []
    
    for fc in data:
        food_queue.append(fc)
        # 如果长度大于k，将最先进入的站点价格删除 再往前已经够不着了
        if len(food_queue) > k:
            food_queue.pop(0)
        # 往前一步需要的食物 从前序最低价站点购买
        min_cost += min(food_queue)
    return min_cost

if __name__ == "__main__":

    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)
