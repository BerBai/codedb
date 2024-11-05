#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0]*len(nums1)
        k = 0
        for num in nums1:
            i = nums2.index(num)
            for j in range(i, len(nums2)):
                if nums2[j] > num:
                    ans[k] = nums2[j]
                    break
            if ans[k] == 0:
                ans[k] = -1
            k += 1
        return ans
# @lc code=end

