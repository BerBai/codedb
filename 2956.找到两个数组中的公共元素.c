/*
 * @Author:  ber bai5775@outlook.com
 * @Date: 2024-07-16 17:12:39
 * @LastEditors:  ber bai5775@outlook.com
 * @LastEditTime: 2024-07-23 10:29:32
 * @FilePath: 2956.找到两个数组中的公共元素.c
 * @Description: 
 * 
 * Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=2956 lang=c
 *
 * [2956] 找到两个数组中的公共元素
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findIntersectionValues(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int* ans = malloc(sizeof(int)*2);
    memset(ans,0,sizeof(int) * 2);
    for(int i=0;i<nums1Size;i++) {
        for(int j=0;j<nums2Size;j++) {
            if(nums1[i] == nums2[j]) {
                ans[0]++;
                break;
            }
        }
    }
    for(int j=0;j<nums2Size;j++) {
        for(int i=0;i<nums1Size;i++) {
            if(nums2[j] == nums1[i]) {
                ans[1]++;
                break;
            }
        }
    }
    *returnSize = 2;
    return ans;
}
// @lc code=end

