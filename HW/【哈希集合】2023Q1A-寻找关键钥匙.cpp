/*
 * @hw id=2023Q1A lang=cpp
 *
 * 寻找关键钥匙
 */

// @hw code=start
#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    string k;
    cin >> k;
    vector<string> boxes;
    string box;
    while (cin >> box) {
        boxes.push_back(box);
    }
    set<char> set_k(k.begin(), k.end());
    int ans = -1;
    for (int i = 0; i < boxes.size(); i++) {
        set<char> set_s;
        for (char c : boxes[i]) {
            if (isalpha(c)) {
                set_s.insert(tolower(c));
            }
        }
        if (set_k == set_s) {
            ans = i + 1;
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
// @hw code=end