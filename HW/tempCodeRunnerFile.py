
n, m = map(int, input().split())
sc = input().split()
arr = [input().split() for _ in range(n)]
sort_by = input()

nums = []
for i in range(n):
    total = 0
    tmp_arr = [arr[i][0]]
    for j in range(1, m + 1):
        tmp = int(arr[i][j])
        total += tmp
        tmp_arr.append(tmp)
    tmp_arr.append(total)
    nums.append(tmp_arr)

if sort_by not in sc:
    nums.sort(key= lambda x: (-x[-1], x[0]))
else:
    idx =  sc.index(sort_by)
    nums.sort(key=lambda x: (-x[idx + 1], x[0]))

print(' '.join([item[0] for item in nums]))