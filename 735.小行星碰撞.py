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
            if not stack:
                stack.append(a)
            else:
                while stack:
                    if (stack[-1] > 0 and a > 0) or (stack[-1] < 0 and a < 0):
                        stack.append(a)
                        break
                    elif (stack[-1] > 0 and a < 0) or (stack[-1] < 0 and a > 0):
                        b = stack.pop()
                        a = a if abs(a) > abs(b) else b
        
        

        return stack
# @lc code=end

