#
# @hw id=2024D lang=python3
#
# 小明找位置
#

# @hw code=start

# 注意获取输入的格式
nums = list(map(int,input().split(',')))
num = int(input())

# 注意二分查找的写法
l, r = 0, len(nums) - 1
while l <= r: # 这里是 小于等于
    mid = (l + r) // 2
    if nums[mid] == num:
        print(mid+1)
        break
    elif nums[mid] < num:
        l = mid + 1
    else:
        r = mid - 1
print(l+1)

# @hw code=end