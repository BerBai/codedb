from datetime import datetime, timedelta

def solution(t1: str, t2: str, t3: str) -> str:
    # 将时间字符串转换为 datetime 对象
    dt2 = datetime.strptime(t2, "%H:%M")
    dt3 = datetime.strptime(t3, "%H:%M")

    # 处理跨天情况
    if int(t1[:2]) > int(t2[:2]) and int(t2[:2]) < int(t3[:2]):
        dt2 += timedelta(days=1)
    
    # 计算时间差
    time_difference = dt3 - dt2

    # 判断是否超时
    if time_difference.total_seconds() > 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(solution("18:00", "19:05", "19:05") == 'No')
    print(solution("23:00", "00:21", "00:23") == 'Yes')
    print(solution("23:05", "00:05", "23:58") == 'No')