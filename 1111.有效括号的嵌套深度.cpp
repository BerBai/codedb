/*
 * @lc app=leetcode.cn id=1111 lang=cpp
 *
 * [1111] 有效括号的嵌套深度
 */

// @lc code=start
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int deep = 0;
        vector<int> ans;
        for(char&c : seq) {
            if(c == '(') {
                deep++;
                ans.push_back(deep%2);
            } else {
                ans.push_back(deep%2);
                deep--;
            }
        }
        return ans;
    }
};
// @lc code=end

