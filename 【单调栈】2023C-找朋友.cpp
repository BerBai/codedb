/*
 * @hw id=2023C lang=cpp
 *
 * 找朋友
 */

// @hw code=start
#include<iostream>
#include<vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for(int i=0;i<n;i++) {
        cin >> height[i];
    }

    vector<int> stack;
    vector<int> ans(n, 0);

    for(int i=0;i<n;i++) {
        int h = height[i];
        while(stack.size() != 0 && h > height[stack.back()]) {
            int top = stack.back();
            stack.pop_back();
            ans[top] = i;
        }
        stack.push_back(i);
    }
    for(int i=0;i<n;i++) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}
// @hw code=end