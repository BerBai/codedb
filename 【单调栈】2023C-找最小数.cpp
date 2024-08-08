/*
 * @hw id=2023C lang=cpp
 *
 * 找最小数
 */

// @hw code=start
#include<iostream>
#include<vector>
using namespace std;

int main() {
    string s;
    int n;
    cin >> s >> n;

    vector<int> stack;
    for(char c : s) {
        while(!stack.empty() && c < stack.back() && n > 0) {
            stack.pop_back();
            n--;
        }
        stack.push_back(c);
    }
    string ans;
    for(int i=0;i<stack.size()-n;i++) {
        ans += stack[i];
    }
    cout << ans << endl;

}
// @hw code=end