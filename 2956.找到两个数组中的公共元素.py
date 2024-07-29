#
# @lc app=leetcode.cn id=2956 lang=python3
#
# [2956] 找到两个数组中的公共元素
#

# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [sum(x in set2 for x in nums1),
                sum(x in set1 for x in nums2)]
# @lc code=end

