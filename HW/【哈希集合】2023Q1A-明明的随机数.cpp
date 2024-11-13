/*
 * @hw id=2023Q1A lang=cpp
 *
 * 明明的随机数
 */

// @hw code=start
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    set<int> numset;
    for(int i=0;i<n;i++) {
        int num;
        cin >> num;
        numset.insert(num);
    }
    vector<int> numlist(numset.begin(), numset.end());
    sort(numlist.begin(), numlist.end());
    for(int num : numlist) {
        cout << num << endl;
    }
    return 0;
}
// @hw code=end