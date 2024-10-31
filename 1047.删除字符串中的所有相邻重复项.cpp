/*
 * @lc app=leetcode.cn id=1047 lang=cpp
 *
 * [1047] 删除字符串中的所有相邻重复项
 */

// @lc code=start
class Solution {
public:
    string removeDuplicates(string s) {
        if(s.length() < 2) {
            return s;
        }
        vector<char> stack;
        // stack.push_back(s[0]);
        for (char c : s) {
            if(stack.size() == 0){
                stack.push_back(c);
                continue;
            }
            char tmp = stack.back();
            if(tmp == c) {
                stack.pop_back();
            } else {
                stack.push_back(c);
            }
        }
        string ans = "";
        for(char c : stack) {
            ans+=c;
        }
        return ans;
    }
};
// @lc code=end

