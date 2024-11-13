#
# @lc app=leetcode.cn id=3261 lang=python3
#
# [3261] 统计满足 K 约束的子字符串数量 II
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        # 记录[l,r]区间0,1的个数
        cnt = [0, 0]
        # 表示s[0,i]中满足约束的个数
        prefix = [0] * (len(s) + 1)
        # 记录满足约束下标r，即r前满足约束
        right = [len(s)] * len(s)
        l, r = 0, 0
        while r < len(s):
            cnt[int(s[r])] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[int(s[l])] -= 1
                # 右端点r前满足约束
                right[l] = r
                l += 1
            # 计算[0, r]满足约束的子串数
            prefix[r+1] = prefix[r] + r - l + 1
            r += 1
        
        ans = []
        for l, r in queries:
            # 找出不满足约束的r下标
            p = min(right[l], r + 1)
            # [l, p-1]区间子串都满足约束
            part1 = (p - l + 1) * (p - l) // 2
            # 计算[p, r]区间满足约束的子串个数
            part2 = prefix[r + 1] - prefix[p]
            ans.append(part1 + part2)
        return ans
# @lc code=end

