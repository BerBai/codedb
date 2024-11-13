/*
 * @hw id=2023Q1A lang=cpp
 *
 * 集五福
 */

// @hw code=start
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    vector<int> cnt(5, 0);
    int i=0;
    for(char c : s) {
        if(c == ',') i=0;
        else cnt[i++] += c-'0';
    }
    cout << *min_element(cnt.begin(), cnt.end()) << endl;
    return 0;
}
// @hw code=end