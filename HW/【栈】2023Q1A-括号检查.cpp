/*
 * @hw id=2023Q1A lang=cpp
 *
 * 括号检查
 */

// @hw code=start
#include <iostream>
#include <vector>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    bool isErr = false;
    int depth = 0;
    int maxDepth = 0;
    if(s.length() % 2 == 1) {
        isErr = true;
    } else {
        vector<char> stack;
        for(char c : s) {
            if(c=='(' || c=='[' || c=='{') {
                stack.push_back(c);
                depth++;
                maxDepth = max(maxDepth, depth);
            } else {
                if(stack.empty()) {
                    isErr = true;
                    break;
                }
                char cl = stack.back();
                stack.pop_back();
                depth--;
                if(c == ')') {
                    isErr = cl!='('?true:false;
                } else if(c == '}') {
                    isErr = cl!='{'?true:false;
                } else if(c == '[') {
                    isErr = cl!='['?true:false;
                }
                if(isErr) {
                    break;
                }
            }
        }
        if(!stack.empty()) {
            isErr = true;
        }
    }
    cout << (isErr?0:maxDepth) << endl;
    return 0;
}
// @hw code=end