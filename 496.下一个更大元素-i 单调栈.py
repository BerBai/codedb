#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)

        

# @lc code=end

