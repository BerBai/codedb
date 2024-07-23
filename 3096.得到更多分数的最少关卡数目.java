/*
 * @Author:  ber bai5775@outlook.com
 * @Date: 2024-07-23 09:34:41
 * @LastEditors:  ber bai5775@outlook.com
 * @LastEditTime: 2024-07-23 10:29:49
 * @FilePath: 3096.得到更多分数的最少关卡数目.java
 * @Description: 
 * 
 * Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=3096 lang=java
 *
 * [3096] 得到更多分数的最少关卡数目
 */

// @lc code=start
class Solution {
    public int minimumLevels(int[] possible) {
        int sum = 0, a = 0,cur=0;
        for(int p:possible) {
            if(p==1) sum = sum + 1;
            else sum = sum - 1;
        }
        for(int p : possible) {
            cur = cur+1;
            if(cur != possible.length)
                if(p==1) {
                    a = a+1;
                    sum = sum-1;
                } else {
                    a = a-1;
                    sum = sum+1;
                }
            if(a>sum) return cur;
        }
        return -1;
    }
}
// @lc code=end

