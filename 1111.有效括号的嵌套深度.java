/*
 * @lc app=leetcode.cn id=1111 lang=java
 *
 * [1111] 有效括号的嵌套深度
 */

// @lc code=start
class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int len = seq.length();
        int ans[] = new int[len];
        int deep = 0;
        for(int i=0;i<len;i++) {
            if(seq.charAt(i)=='(') {
                deep++;
                ans[i] = deep%2;
            } else {
                ans[i] = deep%2;
                deep--;
            }
        }
        return ans;
    }
}
// @lc code=end

