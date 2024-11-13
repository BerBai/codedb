/*
 * @hw id=2023C lang=cpp
 *
 * 篮球游戏
 */

// @hw code=start
#include<iostream>
#include<vector>
#include<sstream>
using namespace std;

int main () {
    string s, sn, token;
    // cin >> s >> sn;
    getline(cin, s);
    getline(cin, sn);
    vector<string> ss, sns, q;
    stringstream ss1(s);
    stringstream ss2(sn);

    while(getline(ss1, token, ',')) {
        ss.push_back(token);
    }
    while(getline(ss2, token, ',')) {
        sns.push_back(token);
    }

    int i = 0;
    string ans;
    for(string si : ss) {
        q.push_back(si);
        while(q.size() > 0) {
            if(q[0] == sns[i]) {
                ans += "L";
                q.erase(q.begin());
                i++;
            } else if(q[q.size() - 1] == sns[i]) {
                ans += "R";
                q.pop_back();
                i++;
            } else {
                break;
            }
        }
    }
    if(ans.length() == sns.size()) {
        cout << ans << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}
// @hw code=end