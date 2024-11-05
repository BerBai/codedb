#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 保存未找到下一日更高温的下标
        stack = []
        # 初始化未0 没有更高温的为0
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # 找到栈顶位置的下一个更高温 出栈计算距离
                j = stack.pop()
                ans[j] = i - j
            # 将当前位置入栈
            stack.append(i)
        return ans
# @lc code=end

