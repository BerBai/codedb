#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')
        stack = []
        for name in names:
            if name == '.':
                continue
            elif name == '..':
                if stack:
                    stack.pop()
            elif name:
                stack.append(name)
        return '/' + '/'.join(stack)
# @lc code=end

