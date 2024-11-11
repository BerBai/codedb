#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        l = r = 0
        cur = 0
        max_ = 0
        while r < n:
            cur += customers[r]
            r += 1
            if r - l == minutes:
                max_ = max(max_, cur)
                cur -= customers[l]
                l += 1
        return ans + max_
# @lc code=end

