/*
 * @Author:  ber bai5775@outlook.com
 * @Date: 2024-07-19 15:51:35
 * @LastEditors:  ber bai5775@outlook.com
 * @LastEditTime: 2024-07-23 10:27:10
 * @FilePath: 3096.得到更多分数的最少关卡数目.cpp
 * @Description: 
 * 
 * Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=3096 lang=cpp
 *
 * [3096] 得到更多分数的最少关卡数目
 */

// @lc code=start
class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        int n = possible.size();
        // 把列表*2去简化计算
        int tot = accumulate(possible.begin(), possible.end(), 0) * 2 - n;
        int a = 0;
        for (int i = 0; i < n - 1; i++) {
            if(possible[i]==1) a = a + 1;
            else a = a - 1;
            if (2 * a > tot) {
                return i + 1;
            }
        }
        return -1;
    }
};
// @lc code=end

