/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j, n=nums.size();
        for(i=0;i<n;i++) {
            for(j=i+1;j<n;j++) {
                if(target == nums[i]+nums[j]) {
                    return {i,j};
                }
            }
        }
        return {};
    }
};
// @lc code=end

