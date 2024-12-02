#
# @hw id=2024E lang=python3
#
# 【回溯】2024E-第N个排列
#
# @hw code=start
def cal(nums, current, result, k):
    if len(nums) == 0:
        result.append(current)
        return

    for i in range(len(nums)):
        num = nums[i]
        new_nums = nums[:i] + nums[i+1:]
        cal(new_nums, current + str(num), result, k)
        if len(result) == k:
            return

n = int(input().strip())
k = int(input().strip())

nums = [i+1 for i in range(n)]
result = []

cal(nums, "", result, k)

# 已经是有序的数组了
# result.sort()
print(result[k-1])
# @hw code=end