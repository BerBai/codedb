#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            ans[num] = stack[-1] if stack else -1
            stack.append(num)
        return [ans[num] for num in nums1]
# @lc code=end

