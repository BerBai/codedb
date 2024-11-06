#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable and i - hashtable[nums[i]] <= k:
                return True
            hashtable[nums[i]] = i
        return False

# @lc code=end

