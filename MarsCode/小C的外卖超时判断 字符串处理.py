def solution(t1: str, t2: str, t3: str) -> str:
    num1 = int(t1[:2])*100 + int(t1[3:5])
    num2 = int(t2[:2])*100 + int(t2[3:5])
    num3 = int(t3[:2])*100 + int(t3[3:5])

    # 处理跨天情况
    if int(t1[:2]) > int(t2[:2]) and int(t2[:2]) < int(t3[:2]):
        num2 += 2400

    # 判断是否超时
    if num3 - num2 > 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(solution("18:00", "19:05", "19:05") == 'No')
    print(solution("23:00", "00:21", "00:23") == 'Yes')
    print(solution("23:05", "00:05", "23:58") == 'No')