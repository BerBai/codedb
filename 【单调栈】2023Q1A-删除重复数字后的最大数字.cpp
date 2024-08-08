/*
 * @hw id=2023Q1A lang=cpp
 *
 * 删除重复数字后的最大数字
 */

// @hw code=start
#include<iostream>
#include<vector>
#include<map>
#include<set>

using namespace std;

int main() {
    string s;
    cin >> s;
    map<char, int> cnt;
    for (char c : s) {
        cnt[c] = cnt.find(c)!=cnt.end() ? cnt[c]+1 : 1;
    }
    set<char> used;
    vector<char> stack;
    for(char c : s) {
        if(used.find(c) != used.end()) {
            cnt[c]--;
        } else {
            while(stack.size()>0 && c > stack.back() && cnt[stack.back()]>1) {
                cnt[stack.back()]--;
                used.erase(stack.back());
                stack.pop_back();
            }
            stack.push_back(c);
            used.insert(c);
        }
    }
    for(char c : stack) {
        cout << c;
    }
    cout << endl;
}
// @hw code=end