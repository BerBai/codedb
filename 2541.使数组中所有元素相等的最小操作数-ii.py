#
# @lc app=leetcode.cn id=2541 lang=python3
#
# [2541] 使数组中所有元素相等的最小操作数 II
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sum = 0
        ans = 0
        for a, b in zip(nums1, nums2):
            a -= b
            # 边界考虑
            if k != 0:
                if a % k != 0:
                    return -1
                # 正负相抵，判断是否成对
                sum += a // k
                if a > 0:
                    # 这里也是 计算次数 正负相抵
                    ans += a // k
            # 边界考虑 k == 0，a != 0 则不满足
            elif a != 0:
                return -1
        return -1 if sum != 0 else ans
# @lc code=end

