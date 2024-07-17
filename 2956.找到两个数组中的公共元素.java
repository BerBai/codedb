/*
 * @lc app=leetcode.cn id=2956 lang=java
 *
 * [2956] 找到两个数组中的公共元素
 */

// @lc code=start
class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        int[] ans = new int[2];
        for(int x:nums1) {
            for(int y:nums2) {
                if(x==y){
                    ans[0]++;
                    break;
                }
            }
        }
        for(int y:nums2) {
            for(int x:nums1) {
                if(x==y) {
                    ans[1]++;
                    break;
                }
            }
        }
        return ans;
    }
}
// @lc code=end

