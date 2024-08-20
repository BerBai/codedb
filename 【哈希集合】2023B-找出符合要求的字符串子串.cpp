/*
 * @hw id=2023B lang=cpp
 *
 * 找出符合要求的字符串子串
 */

// @hw code=start
#include<iostream>
#include<set>
#include<algorithm>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    set<char> set1(s1.begin(), s1.end());
    set<char> set2(s2.begin(), s2.end());
    string ans;
    for (char c : s1) {
        if (set2.find(c) != set2.end()) {
            ans += c;
        }
    }
    sort(ans.begin(), ans.end());
    cout << ans << endl;
    return 0;
}
// @hw code=end