/*
 * @hw id=2023B lang=cpp
 *
 * 数字游戏
 */

// @hw code=start
#include<iostream>
#include<set>
#include<vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int nums[n];
    for(int i=0;i<n;i++) {
        cin >> nums[i];
    }
    int sum = 0;
    set<int> sumSet;
    sumSet.insert(0);
    int flag = 0;
    for(int num : nums) {
        sum += num;
        if(sumSet.count(sum%m)) {
            flag = 1;
            break;
        }
        sumSet.insert(sum%m);
    }
    cout << flag << endl;
}
// @hw code=end