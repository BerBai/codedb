#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        n1 = len(nums1)
        n2 = len(nums2)
        i1 = i2 = 0
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                if not ans or nums1[i1] != ans[-1]:
                    ans.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return ans

# @lc code=end

