#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ws = {}
        for bill in bills:
            if bill == 5:
                ws[5] = ws.get(5, 0) + 1
            elif bill == 10:
                if ws.get(5, 0) > 0:
                    ws[5] -= 1
                    ws[10] = ws.get(10, 0) + 1
                else:
                    return False
            else:
                if ws.get(5, 0) > 0 and ws.get(10, 0) > 0:
                    ws[5] -= 1
                    ws[10] -= 1
                elif ws.get(5, 0) >= 3:
                    ws[5] -= 3
                else:
                    return False
        return True
# @lc code=end

