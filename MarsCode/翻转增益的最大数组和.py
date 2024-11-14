def solution(N, data_array):
    # 计算原始数组的最大子数组和
    max_sum = kadane(data_array)
    
    # 考虑翻转操作的影响
    for i in range(N):
        for j in range(i, N):
            # 翻转子数组 data_array[i:j+1]
            reversed_subarray = data_array[i:j+1][::-1]
            # 计算翻转后的数组的最大子数组和
            max_sum = max(max_sum, kadane(data_array[:i] + reversed_subarray + data_array[j+1:]))
    
    return max_sum

def kadane(array):
    # Kadane算法实现
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == "__main__":
    array1 = [-85, -11, 92, 6, 49, -76, 28, -16, 3, -29, 26, 37, 86, 3, 25, -43, -36, -27, 45, 87, 91, 58, -15, 91, 5, 99, 40, 68, 54, -95, 66, 49, 74, 9, 24, -84, 12, -23, -92, -47, 5, 91, -79, 94, 61, -54, -71, -36, 31, 97, 64, -14, -16, 48, -79, -70, 54, -94, 48, 37, 47, -58, 6, 62, 19, 8, 32, 65, -81, -27, 14, -18, -34, -64, -97, -21, -76, 51, 0, -79, -22, -78, -95, -90, 4, 82, -79, -85, -64, -79, 63, 49, 21, 97, 47, 16, 61, -46, 54, 44]
    print(solution(5, [1,2,3,-1,4]) == 10 )
    print(solution(5, [-1,-2,-3,-4,-5]) == -1 )
    print(solution(100, array1) == 1348)