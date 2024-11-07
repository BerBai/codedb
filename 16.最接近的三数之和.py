#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if i == 0 or nums[i]!=nums[i-1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == target:
                        return sum
                    elif sum > target:
                        k -= 1
                    else:
                        j += 1
        return ans


# @lc code=end

