#
# @hw id=2024D lang=python3
#
# 山脉的个数
#

# @hw code=start
def solution(arr) -> int:
    ans = []
    for i in range(1, len(arr)-1):
        # 边界特殊情况处理
        if i == 1 and arr[i-1] > arr[i]:
            ans.append(i)
        if i == len(arr) - 2 and arr[i] < arr[i+1]:
            ans.append(i)

        # 一般情况处理
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            ans.append(i)
    return len(ans)

print(solution([3,2,1]) == 1 )
print(solution([0,1,0]) == 1 )
print(solution([0,1,1,0,2,1,2]) == 2 )
print(solution([2, 3, 3, 2, 1]) == 0 )
# @hw code=end

