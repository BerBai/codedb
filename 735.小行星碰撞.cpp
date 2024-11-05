/*
 * @lc app=leetcode.cn id=735 lang=cpp
 *
 * [735] 小行星碰撞
 */

// @lc code=start
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (int a : asteroids){
            while(!stack.empty()) {
                if((a < 0 && stack.back() < 0) || (a > 0 && a > 0 && stack.back() > 0) || (a > 0 && stack.back() < 0)) {
                    stack.push_back(a);
                    break;
                } else {
                    int b = stack.back();
                    stack.pop_back();
                    if (abs(a) > abs(b)) {
                        // 继续比较stack中行星
                        continue;
                    } else if (abs(a) < abs(b)) {
                        // 保持stack中行星
                        stack.push_back(b);
                        break;
                    } else {
                        // 标记下行星爆炸相抵
                        a = 0;
                        break;
                    }
                }
            }
            // stack为空 且 行星未爆炸相抵 则将行星加入stack中
            if(stack.empty() && a!= 0) {
                stack.push_back(a);
            }
            
        }
        return stack;
    }
};
// @lc code=end

