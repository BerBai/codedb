#
# @hw id=2024E lang=python3
#
# 【位运算】2024E-响应报文时间
#

# @hw code=start

def cal_resp_time(T, M):
    if M < 128:
        return T + M
    else:
        mant = M & 0b00001111
        exp = (M & 0b01110000) >> 4
        return (mant | 0x10) << (exp + 3)


C = int(input())
# [T, M]
arr = [list(map(int, input().split())) for _ in range(C)]

min_reps_time = float('inf')
for T, M in arr:
    min_reps_time = min(min_reps_time, cal_resp_time(T, M))

print(min_reps_time)
# @hw code=end