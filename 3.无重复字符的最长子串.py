#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        r, l = 0, 0
        while(r < len(s)):
            if s[r] not in s[l:r]:
                r += 1
            else:
                ans = max(ans, r-l)
                l = s.index(s[r], l)
                l += 1
                r += 1
        ans = max(ans, r-l)
        return ans


# @lc code=end

