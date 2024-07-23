'''
Author:  ber bai5775@outlook.com
Date: 2024-07-18 08:39:21
LastEditors:  ber bai5775@outlook.com
LastEditTime: 2024-07-23 10:29:28
FilePath: 2.两数相加.py
Description: 

Copyright (c) 2024 by bai5775@outlook.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = head = ListNode()
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next
            carry = val//10
            val = val%10
            p.next = ListNode(val)
            p = p.next
        return head.next
# @lc code=end

