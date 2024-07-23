/*
 * @Author:  ber bai5775@outlook.com
 * @Date: 2024-07-23 10:20:36
 * @LastEditors:  ber bai5775@outlook.com
 * @LastEditTime: 2024-07-23 10:29:43
 * @FilePath: 3096.得到更多分数的最少关卡数目.c
 * @Description: 
 * 
 * Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=3096 lang=c
 *
 * [3096] 得到更多分数的最少关卡数目
 */

// @lc code=start
int minimumLevels(int* possible, int possibleSize) {
    int sum = 0, a = 0;
    for(int i=0;i<possibleSize;i++) {
        sum = possible[i] + sum;
    }
    sum = sum*2-possibleSize;
    for(int i=0;i<possibleSize-1;i++) {
        if(possible[i]==1) a = a + 1;
        else a = a - 1;
        if(a*2>sum) return i+1;
    }
    return -1;
}
// @lc code=end

