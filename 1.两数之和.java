/*
 * @Author:  ber bai5775@outlook.com
 * @Date: 2024-07-16 11:03:21
 * @LastEditors:  ber bai5775@outlook.com
 * @LastEditTime: 2024-07-23 10:28:01
 * @FilePath: 1.两数之和.java
 * @Description: 
 * 
 * Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> numMap = new HashMap<>();
        for(int i=0;i<nums.length;i++) {
            int tmp = target-nums[i];
            if(numMap.containsKey(tmp)) {
                return new int[]{i,numMap.get(tmp)};
            }
            numMap.put(nums[i], i);
        }
        return null;
    }
}
// @lc code=end

