#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特殊情况处理 无需转换
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        i, j = 0, 0
        while i < len(s):
            while i < len(s) and j < numRows:
                ans[j].append(s[i])
                i += 1
                j += 1
            # 注意这里的边界条件，numRows=1时会死循环，需特殊处理
            j -= 2
            while i < len(s) and j >= 0:
                ans[j].append(s[i])
                i += 1
                j -= 1
            j += 2
        return "".join(["".join(item) for item in ans])
# @lc code=end

