/*
 * @hw id=2023Q1A lang=cpp
 *
 * 删除最少字符
 */

// @hw code=start
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int main()
{
    string s;
    cin >> s;
    vector<int> cnt(26, INT_MAX);
    for (char c : s)
    {
        int i = c - 'a';
        if (cnt[i] == INT_MAX)
        {
            cnt[i] = 0;
        }
        cnt[i] += 1;
    }
    int mn = *min_element(cnt.begin(), cnt.end());
    string ans;
    for (char c : s)
    {
        int i = c - 'a';
        if (cnt[i] > mn)
        {
            ans += c;
        }
    }
    if (ans.empty())
    {
        cout << "empty" << endl;
    }
    else
    {
    cout << ans << endl;
    }
    return 0;
}
// @hw code=end