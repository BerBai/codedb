#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temperature = temperatures[i]
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)
        return ans
# @lc code=end

