#
# @hw id=2024E lang=python3
#
# 项目排期
#

# @hw code=start
import heapq

ms = list(map(int, input().split()))
n = int(input())

ms.sort(reverse = True)
ans = [0]*n
heapq.heapify(ans)
i = 0
for task in ms:
    # 获取当前工作量最少的开发人员
    min_worker = heapq.heappop(ans)
    # 将任务分配给这个开发人员
    min_worker += task
    # 将更新后的工作量重新放回堆中
    heapq.heappush(ans, min_worker)

print(max(ans))
# @hw code=end
