#
# @hw id=2024D lang=python3
#
# 【位运算】2024E-分苹果
# A 要平分，则两堆异或结果相等，相等则所有相异或=0

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

# 如果a异或后不等于0，则无法得到结果
if need_a != 0:
    print(-1)
else:
    print(sum(nums[1:]))
# @hw code=end