#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                k = len(nums) - 1
                for j in range(i+1, len(nums)):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        # 双指针
                        while j < k and nums[i] + nums[j] + nums[k] > 0:
                            k -= 1
                        # 如果j\k指针重合，不存在，跳出本回合循环
                        if j == k:
                            break
                        if nums[i] + nums[j] + nums[k] == 0:
                            ans.append([nums[i], nums[j], nums[k]])
        return ans
# @lc code=end

