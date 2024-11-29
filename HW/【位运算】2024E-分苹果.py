#
# @hw id=2024D lang=python3
#
# 【位运算】2024E-分苹果
#

# @hw code=start

def cal_a(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

n = int(input())
nums = list(map(int, input().split()))

need_a = cal_a(nums)

nums.sort()

if need_a != 0:
    print(-1)
else:
    print(sum(nums[1:]))
# @hw code=end