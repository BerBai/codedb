#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1 and num not in ans:
                    ans.append(num)
        else:
            for num in nums1:
                if num in nums2 and num not in ans:
                    ans.append(num)
        return ans


# @lc code=end

