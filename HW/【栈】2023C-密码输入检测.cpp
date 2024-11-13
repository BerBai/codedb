/*
 * @hw id=2023C lang=cpp
 *
 * 密码输入检测
 */

// @hw code=start
#include<iostream>
#include<vector>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    vector<char> stack;
    for (char c : s) {
        if(c == '<' && stack.size() >= 1) {
            stack.pop_back();
        } else if(c!='<') {
            stack.push_back(c);
        }
    }

    int flag = 0;
    for (char c : stack) {
        if(isupper(c)) {
            flag |= 0b0001;
        } else if(islower(c)) {
            flag |= 0b0010;
        } else if(isdigit(c)) {
            flag |= 0b0100;
        } else if(!isspace(c) && !isalnum(c)) {
            flag |= 0b1000;
        }
    }

    string ans;
    for(char c : stack) {
        ans += c;
    }
    
    if(flag == 0b1111 && stack.size() >= 8) {
        cout << ans << ",true" << endl;
    } else {
        cout << ans << ",false" << endl;
    }
    return 0;
}
// @hw code=end