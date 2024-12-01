#
# @hw id=2024E lang=python3
#
# VLAN 资源池
# 细节细节！！

# @hw code=start
vs = input().split(',')
ns = input().split(',')

v = []
s = []
for i in vs:
    if '-' in i:
        v.append(list(map(int, i.split('-'))))
    else:
        v.append((int(i), int(i)))

for i in ns:
    if '-' in i:
        s.append(list(map(int, i.split('-'))))
    else:
        s.append((int(i), int(i)))

v.sort(key=lambda x: (x[0], x[1]))
s.sort(key=lambda x: (x[0], x[1]))

ans = []

k = 0
p = 0
while p < len(s) and k < len(v):
    i, j = s[p]
    if i == v[k][0]:
        if j < v[k][1]:
            v[k][0] = j + 1
            p += 1
        elif j > v[k][1]:
            s[p][0] = v[k][1] + 1
            k += 1
        else:
            p += 1
            k += 1

    elif v[k][0] < i <= v[k][1]:
        if v[k][0] == i-1:
            ans.append(f'{v[k][0]}')
        else:
            ans.append(f'{v[k][0]}-{i-1}')
        
        if j < v[k][1]:
            v[k][0] = j + 1
            p += 1
        elif j > v[k][1]:
            k += 1
            i = v[k][1] + 1
        else:
            p += 1
            k += 1
    else:
        if v[k][0] == v[k][1]:
            ans.append(f'{v[k][0]}')
        else:
            ans.append(f'{v[k][0]}-{v[k][1]}')
        k += 1
while k < len(v):
    if v[k][0] == v[k][1]:
        ans.append(f'{v[k][0]}')
    else:
        ans.append(f'{v[k][0]}-{v[k][1]}')
    k += 1  

print(','.join(ans))

# @hw code=end