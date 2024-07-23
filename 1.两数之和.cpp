/*
 * @Author:  ber bai5775@outlook.com
 * @Date: 2024-07-16 14:46:41
 * @LastEditors:  ber bai5775@outlook.com
 * @LastEditTime: 2024-07-23 10:27:57
 * @FilePath: 1.两数之和.cpp
 * @Description: 
 * 
 * Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j, n=nums.size();
        for(i=0;i<n;i++) {
            for(j=i+1;j<n;j++) {
                if(target == nums[i]+nums[j]) {
                    return {i,j};
                }
            }
        }
        return {};
    }
};
// @lc code=end

