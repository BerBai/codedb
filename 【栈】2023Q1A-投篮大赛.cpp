/*
 * @hw id=2023Q1A lang=cpp
 *
 * 投篮大赛
 */

// @hw code=start
#include<iostream>
#include<vector>
using namespace std;

int main() {
    string s;
    vector<string> ops;
    vector<int> stack;
    bool isErr = false;
    while(getline(cin, s, ' ')) {
        ops.push_back(s);
    }
    for(string s : ops) {
        if(s!="D" && s!="C" && s!="+") {
            stack.push_back(stoi(s));
        } else if(s=="D" && stack.size() >= 1) {
            stack.push_back(stack.back()*2);
        } else if(s=="+" && stack.size() >= 2) {
            stack.push_back(stack.back() + stack[stack.size()-2]);
        } else if(s=="C" && stack.size() >= 1) {
            stack.pop_back();
        } else {
            isErr = true;
            break;
        }
    }
    int sum = 0;
    for(int i : stack) {
        sum += i;
    }
    cout << (isErr?-1:sum) << endl;
    return 0;
}
// @hw code=end