/*
 * @Author: ber bai5775@outlook.com
 * @Date: 2024-07-17 17:05:04
 * @LastEditors: ber bai5775@outlook.com
 * @LastEditTime: 2024-07-17 17:10:21
 * @FilePath: \.leetcode\2.两数相加.cpp
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode();
        ListNode* p = head;
        int carry = 0;
        while(l1!=nullptr||l2!=nullptr||carry!=0) {
            int val = carry;
            if(l1!=nullptr) {
                val = val + l1->val;
                l1 = l1->next;
            }
            if(l2!=nullptr) {
                val = val + l2->val;
                l2 = l2->next;
            }
            carry = val/10;
            val = val%10;
            p->next = new ListNode(val);
            p = p->next;
        }
        return head->next;
    }
};
// @lc code=end

