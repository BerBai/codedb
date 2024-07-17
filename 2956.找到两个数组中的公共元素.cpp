/*
 * @lc app=leetcode.cn id=2956 lang=cpp
 *
 * [2956] 找到两个数组中的公共元素
 */

// @lc code=start
class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(), m=nums2.size();
        vector<int> ans = {0,0};
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(nums1[i] == nums2[j]) {
                    ans[0]++;
                    break;
                }
            }
        }
        for(int j=0;j<m;j++) {
            for(int i=0;i<n;i++) {
                if(nums2[j] == nums1[i]) {
                    ans[1]++;
                    break;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

