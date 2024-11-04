#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numStr = ""
        for ch in s:
            if ch.isdigit():
                numStr = numStr + ch
            elif ch == '[':
                stack.append(numStr)
                numStr = ""
                stack.append(ch)
            elif ch == ']':
                tmpStr = ""
                while stack[-1]!= '[':
                    tmpStr = stack.pop() + tmpStr

                stack.pop()
                num = int(stack.pop())
                stack.append(tmpStr*num)
            else:
                stack.append(ch)
        return "".join(stack)
# @lc code=end

