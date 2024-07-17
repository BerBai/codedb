/*
 * @Author: ber bai5775@outlook.com
 * @Date: 2024-07-17 16:24:22
 * @LastEditors: ber bai5775@outlook.com
 * @LastEditTime: 2024-07-17 16:55:20
 * @FilePath: \.leetcode\2.两数相加.java
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(-1);
        ListNode p = head;
        int carry = 0;
        while(l1 != null || l2 != null || carry != 0) {
            int val = carry;
            if(l1!=null) {
                val = val + l1.val;
                l1 = l1.next;
            }
            if(l2!=null) {
                val = val + l2.val;
                l2 = l2.next;
            }
            carry = val/10;
            val = val%10;
            p.next = new ListNode(val);
            p = p.next;
        }

        return head.next;
    }
}
// @lc code=end

