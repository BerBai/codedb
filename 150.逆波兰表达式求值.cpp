/*
 * @lc app=leetcode.cn id=150 lang=cpp
 *
 * [150] 逆波兰表达式求值
 */

// @lc code=start
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        int a,b;
        
        for(string c : tokens) {
            if(c=="+" || c=="-" || c=="/" || c=="*") {
                a = stack.back();
                stack.pop_back();
                b = stack.back();
                stack.pop_back();
                if(c=="+") {
                    stack.push_back(a + b);
                } else if(c=="-") {
                    stack.push_back(b - a);
                } else if(c=="/"){
                    stack.push_back(b / a);
                } else {
                    stack.push_back(b * a);
                }
            } else {
                stack.push_back(std::stoi(c));
            }
        }
        return stack.back();
    }
};
// @lc code=end

