#
# @hw id=2024E lang=python3
#
# 最短木板长度
#

# @hw code=start
def insertSort(nums, arr, num, l, r):
    if l == r:
        if arr[l] > num:
            return l
        else:
            return l + 1
    mid = (l + r) // 2
    if arr[mid] > num:
        return insertSort(arr, num, l, mid)
    else:
        return insertSort(arr, num, mid + 1, r)


n = int(input())
arr = [""] * n

for i in range(n):
    arr[i] = input()
for item in arr:
    num = int(item[:-1])
    unit = item[-1]
    tmp = 0
    if unit == "G":
        tmp = num * 1024
    elif unit == "T":
        tmp = num * 1024 * 1024
    else:
        tmp = num
    


# @hw code=end