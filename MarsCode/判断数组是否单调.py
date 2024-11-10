def solution(nums: list) -> bool:
    isInc = False
    isDec = False
    for i in range(1, len(nums)):
        if not isInc and not isDec:
            isInc = nums[i-1] < nums[i]
            isDec = nums[i-1] > nums[i]

        if isInc and nums[i-1] > nums[i]:
            return False
        if isDec and nums[i-1] < nums[i]:
            return False
    return True

if __name__ == '__main__':
    print(solution(nums=[1, 2, 2, 3]) == True)
    print(solution(nums=[6, 5, 4, 4]) == True)
    print(solution(nums=[1, 3, 2, 4, 5]) == False)