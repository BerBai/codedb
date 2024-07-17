/*
 * @Author: ber bai5775@outlook.com
 * @Date: 2024-07-17 17:14:03
 * @LastEditors: ber bai5775@outlook.com
 * @LastEditTime: 2024-07-17 17:27:13
 * @FilePath: \.leetcode\2.两数相加.c
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
 */
/*
 * @lc app=leetcode.cn id=2 lang=c
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = NULL;
    struct ListNode* p = NULL;
    head = malloc(sizeof(struct ListNode));
    head->val = 0;
    head->next = NULL;
    p = head;
    int carry = 0;
    while(l1!=NULL||l2!=NULL||carry!=0) {
        int val = carry;
        if(l1!=NULL) {
            val = val + l1->val;
            l1 = l1->next;
        }
        if(l2!=NULL) {
            val = val + l2->val;
            l2 = l2->next;
        }
        carry = val/10;
        val = val%10;
        struct ListNode* tmp;
        tmp = malloc(sizeof(struct ListNode));
        tmp->val = val;
        tmp->next = NULL;
        p->next = tmp;
        p = p->next;
    }
    return head->next;
}
// @lc code=end

