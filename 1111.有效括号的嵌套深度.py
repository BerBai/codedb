#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        deep = 0
        ans = []
        for c in seq:
            if c == '(':
                deep += 1
                ans.append(deep%2)
            else:
                ans.append(deep%2)
                deep -= 1
        return ans
# @lc code=end

