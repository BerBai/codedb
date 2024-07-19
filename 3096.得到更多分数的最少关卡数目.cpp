/*
 * @lc app=leetcode.cn id=3096 lang=cpp
 *
 * [3096] 得到更多分数的最少关卡数目
 */

// @lc code=start
class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        int n = possible.size();
        int tot = accumulate(possible.begin(), possible.end(), 0) * 2 - n;
        int pre = 0;
        for (int i = 0; i < n - 1; i++) {
            pre += possible[i] == 1 ? 1 : -1;
            if (2 * pre > tot) {
                return i + 1;
            }
        }
        return -1;
    }
};
// @lc code=end

