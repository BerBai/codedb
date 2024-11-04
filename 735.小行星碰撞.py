#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 小行星碰撞
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack:
                if (stack[-1] > 0 and a > 0) or (stack[-1] < 0 and a < 0) or (stack[-1] < 0 and a > 0):
                    stack.append(a)
                    break
                elif (stack[-1] > 0 and a < 0):
                    b = stack.pop()
                    if abs(a) == abs(b):
                        a = 0
                        break
                    elif abs(a) > abs(b):
                        continue
                    else:
                        stack.append(b)
                        break
            if not stack and a != 0:
                stack.append(a)

        return stack

'''
下面把题目意思弄错了，理解成正负总会碰撞，
其实是一条无限的线，两头相反的方向永远不会碰撞
稍微修改下条件就可以解决
'''

"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack:
                if (stack[-1] > 0 and a > 0) or (stack[-1] < 0 and a < 0):
                    stack.append(a)
                    break
                elif (stack[-1] > 0 and a < 0) or (stack[-1] < 0 and a > 0):
                    b = stack.pop()
                    if abs(a) == abs(b):
                        a = 0
                        break
                    elif abs(a) > abs(b):
                        continue
                    else:
                        stack.append(b)
                        break
            if not stack and a != 0:
                stack.append(a)

        return stack
"""
# @lc code=end

