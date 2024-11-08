#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = []
        for num in nums:
            ans.append(str(num))
        # 先将字符重复10次，在按字典序降序排序
        ans.sort(key=lambda x: x*10, reverse=True)
        return str(int(''.join(ans)))
# @lc code=end

