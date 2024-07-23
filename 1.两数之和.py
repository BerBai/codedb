'''
Author:  ber bai5775@outlook.com
Date: 2024-07-18 08:39:21
LastEditors:  ber bai5775@outlook.com
LastEditTime: 2024-07-23 10:28:11
FilePath: 1.两数之和.py
Description: 

Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
# @lc code=end

