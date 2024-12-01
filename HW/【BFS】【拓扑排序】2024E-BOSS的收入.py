#
# @hw id=2024E lang=python3
#
# 【BFS】2024E-BOSS的收入
# 

# @hw code=start
from collections import defaultdict
n = int(input())

ids = set()
# 每个id的收入
id_income = {}
# 存储子id -> 父id
c_to_p = {}
# 拓扑图关系  父id -> 子id
p_to_c = defaultdict(list)

for _ in range(n):
    c_id, p_id, income = map(int, input().split())
    ids.add(c_id)
    ids.add(p_id)
    id_income[c_id] = income

    c_to_p[c_id] = p_id
    p_to_c[p_id].append(c_id)

# 递归实现求p_id的收入
def dfs(p_id, p_to_c, id_income):
    c = p_to_c[p_id]
    if not c:
        return
    for c_id in c:
        dfs(c_id, p_to_c, id_income)
        id_income[p_id] += id_income[c_id] // 100 * 15

for id in ids:
    if id not in c_to_p:
        id_income[id] = 0
        dfs(id, p_to_c, id_income)
        break

print(f'{id} {id_income[id]}')
# @hw code=end