#
# @lc app=leetcode.cn id=134 lang=python
#
# [134] 加油站
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        i = 0
        while i < n:
            sumGas, sumCost = 0, 0
            # 走过的加油站数量
            count = 0
            while count < n:
                # 环 
                j = (i + count) % n
                sumGas += gas[j]
                sumCost += cost[j]
                # 总花费大于总油量 出发点无法走完环
                if sumCost > sumGas:
                    break
                # 增加计数
                count += 1
            # 走完一圈 i下标既是可以走完环的出发点
            if count == n:
                return i
            else:
                i = i + count + 1
        return -1
# @lc code=end

