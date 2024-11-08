#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 长度增加1 防止出现整个数组为答案的情况
        ans = len(nums)+1
        l, r = 0, 0
        sum = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                ans = min(ans, r-l+1)
                sum -= nums[l]
                l += 1
            r += 1
        return 0 if ans == len(nums)+1 else ans
# @lc code=end

