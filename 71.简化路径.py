#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dstr = ''
        pstr = ''

        for c in path:
            
            if c == '.':
                dstr += c
            elif c == '/':
                if dstr == '..':
                    # 移除上一个目录 or 根目录
                    stack.pop()
                    stack.pop()
                elif dstr == '.':
                    # 保持当前目录
                    pass
                else:
                    # 新目录
                    stack.append(dstr)
                dstr = ''
                if pstr != '':
                    stack.append(pstr)
                pstr = ''
                if len(stack) == 0 or stack[-1] != '/':
                    stack.append('/')

            elif c.isalpha():
                pstr += c
        # if dstr == '..':
        #     # 移除上一个目录 or 根目录
        #     stack.pop()
        #     stack.pop()
        if pstr != '':
            stack.append(pstr)

        # 移除末尾的/
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()

        return ''.join(stack)
# @lc code=end

