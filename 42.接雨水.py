#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                # 移除中间下标
                top = stack.pop()
                # 无左边 不能蓄水 栈至少两位元素
                if not stack:
                    break
                left = stack[-1]
                # 根据宽高计算
                ans += (i-left-1) * (min(height[i], height[left])-height[top])
            # 下标入栈
            stack.append(i)
        return ans
# @lc code=end

