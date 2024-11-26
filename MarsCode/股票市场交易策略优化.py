def solution(stocks):
    n = len(stocks)
    if n == 0:
        return 0
    
    # 持有股票的最大收益
    buy = [0] * n
    # 不持有股票的最大收益
    sell = [0] * n
    
    # 初始状态
    buy[0] = -stocks[0]  # 第一天买入股票
    sell[0] = 0  # 第一天不持有股票
    
    for i in range(1, n):
        # 更新 buy[i]
        buy[i] = max(buy[i-1],  # 保持前一天的状态
                     # 前一天不持有股票且不在冷冻期，今天买入
                     (sell[i-2] if i >= 2 else 0) - stocks[i])
        
        # 更新 sell[i]
        sell[i] = max(sell[i-1],  # 保持前一天的状态
                      buy[i-1] + stocks[i])  # 前一天持有股票，今天卖出
    
    # 最终的最大利润是 sell 数组中的最大值
    return sell[-1]
    

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 2]) == 1 )
    print(solution([2, 1]) == 0 )
    print(solution([1, 2, 3, 0, 2]) == 3 )
    print(solution([2, 3, 4, 5, 6, 7]) == 5 )
    print(solution([1, 6, 2, 7, 13, 2, 8]) == 12 )