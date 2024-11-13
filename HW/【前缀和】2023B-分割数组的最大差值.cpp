/*
 * @hw id=2023B lang=cpp
 *
 * 分割数组的最大差值
 */

// @hw code=start
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int nums[n];
    int lsum = 0, rsum = 0, ans = 0;
    for(int i=0;i<n;i++) {
        cin >> nums[i];
        rsum += nums[i];
    }
    for(int i=0;i<n;i++) {
        lsum += nums[i];
        rsum -= nums[i];
        ans = max(ans, abs(lsum - rsum));
    }
    cout << ans << endl;
    return 0;
}
// @hw code=end