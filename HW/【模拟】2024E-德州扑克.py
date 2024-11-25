#
# @hw id=2024E lang=python3
#
# 德州扑克
#

# @hw code=start

value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

arr = [list(input().split()) for _ in range(5)]

c_cnts = {}
cnts = {}

for n, c in arr:
    if c not in c_cnts:
        c_cnts[c] = 1
    else:
        c_cnts[c] += 1
    if n not in cnts:
        cnts[n] = 1
    else:
        cnts[n] += 1
        
ns = sorted(cnts.keys())

if len(c_cnts) == 1:
    if value_map[ns[-1]] - value_map[0] == 4:
    	print(1)
        exit()
if len(cnts) == 2:
    if max(cnts.values) == 4:
        print(2)
        exit()
    else:
        print(3)
        exit()
if len(c_cnts) == 1:
    print(4)
    exit()
if len(c_cnts) == 5:
    if value_map[ns[-1]] - value_map[ns[0]] == 4:
    	print(5)
        exit()
if len(cnts) == 3 and max(cnts.values()) == 3:
    print(6)
    exit()
# @hw code=end
