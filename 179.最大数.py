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
        # 先将字符重复10次，在按字典序降序排序 避免3 30，出现 303 这样的情况
        ans.sort(key=lambda x: x*10, reverse=True)
        # 转成int 去除000的情况 转成str得到答案
        return str(int(''.join(ans)))
# @lc code=end

