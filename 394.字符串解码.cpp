/*
 * @lc app=leetcode.cn id=394 lang=cpp
 *
 * [394] 字符串解码
 */

// @lc code=start
class Solution {
public:
    string decodeString(string s) {
        vector<string> stack;

        string numstr = "";
        for(char c : s) {
            // if处理再仔细一点
            if(c <= '9' && c >= '0') {
                numstr = numstr + c;
            } else if(c == '[') {
                stack.push_back(numstr);
                numstr = "";
                stack.push_back("[");
            } else if(c == ']') {
                string tmp = "";
                while(stack.back() != "[") {
                    tmp = stack.back() + tmp;
                    stack.pop_back();
                }
                stack.pop_back();
                int num = stoi(stack.back());
                stack.pop_back();
                while(num--) {
                    stack.push_back(tmp);
                }  
            } else {
                stack.push_back(string(1, c));
            }
        }
        string ans = "";
        for(string s : stack) {
            ans = ans + s;
        }
        return ans;
    }
};
// @lc code=end

