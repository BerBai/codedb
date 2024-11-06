#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        hashtable = {}
        for i in range(n1):
            if s[i] in hashtable:
                hashtable[s[i]] += 1
            else:
                hashtable[s[i]] = 1
        for i in range(n2):
            if t[i] in hashtable:
                hashtable[t[i]] -= 1
            if t[i] not in hashtable or hashtable[t[i]] < 0:
                return False
        return True
# @lc code=end

